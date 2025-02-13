from anc.data.anc_processor import Processor
from anc.data.processors.tokenizer import HFPretrainedTokenizer
import logging
import torch
import json
from typing import List, Tuple


class FakeOpt:
    def __init__(self, hf_model_name, prompt_style, add_bos):
        self.hf_model_name = hf_model_name
        self.prompt_style = prompt_style
        self.prefix_template = ""
        self.delimiter = ""
        self.add_bos = add_bos


def setup_separate_prompt(opt):
    if opt.prompt_style == 'sunhao_old':
        opt.prefix_template = '### {role}:'
        opt.delimiter = '\n\n'
    # elif opt.prompt_style == 'chatml':
    #     opt.prefix_template = '<|im_start|> {role}\n'
    #     opt.delimiter = '<|im_end|>\n'
    elif opt.prompt_style == 'chatml2':
        opt.prefix_template = '<|im_start|>{role}\n'
        opt.delimiter = '<|im_end|>\n'
    elif opt.prompt_style == 'chatml_non_special': # used when <|im_end|> is not a special token
        opt.prefix_template = '<|im_start|> {role}\n'
        opt.delimiter = ' <|im_end|>\n'
    elif opt.prompt_style == 'llama3':
        opt.prefix_template = '<|start_header_id|>{role}<|end_header_id|>\n\n'
        opt.delimiter = '<|eot_id|>'
    else:
        # Use chatml2 by default
        opt.prefix_template = '<|im_start|>{role}\n'
        opt.delimiter = '<|im_end|>\n'

    opt.delimiter = opt.delimiter.replace('\\n', '\n')
    logging.info(f'Using dialog template:\n{opt.prefix_template}content{opt.delimiter}')


class SFTProcessor(Processor):
    def __init__(
        self,
        hf_model_name,
        prompt_style,
        max_seq_len,
        add_bos,
        batch_size,
        micro_batch_size,
        ceil_to_nearest=False,
        pad_label_id=None,
        cu_seqlen_use_old_pack=False
    ):
        self.opt = FakeOpt(hf_model_name, prompt_style, add_bos)
        setup_separate_prompt(self.opt)
        self.tokenizer = HFPretrainedTokenizer(self.opt)
        self.max_seq_len = max_seq_len
        self.batch_size = batch_size
        self.micro_batch_size = micro_batch_size
        assert self.micro_batch_size == 1
        self.micro_batch = []
        self.pad_seq_length_to_mult = 16
        self.ceil_to_nearest = ceil_to_nearest
        self.pad_label_id = pad_label_id if pad_label_id is not None else self.tokenizer.end_token_id
        self.pad_token_id = self.tokenizer.end_token_id
        self.cu_seqlen_use_old_pack = cu_seqlen_use_old_pack

    def transform(self, item, is_last_sample=False):
        if not all(turn['role'] and turn['content'] and type(turn['role']) is str and type(turn['content']) is str for turn in item['messages']):
            return
        context = [(turn['role'].strip(), turn['content']) for turn in item['messages']]
        last_turn_mask_flag = item.get('last_turn_mask', False) or item.get('loss_on_last_turn', False)
        no_mask_flag = item.get('no_mask', False)
        context_vec, loss_mask = self._encode_one(context, last_turn_mask_flag, no_mask_flag)
        # append one more token at the end of each sequence since nemo would truncate one
        # context_vec.append(self.tokenizer.end_token_id)
        # loss_mask.append(0)
        yield from [{"input_ids": context_vec, "loss_mask": loss_mask}]

    def _encode_one(self, context, last_turn_mask_flag, no_mask_flag):
        context_vec, loss_mask = self._build_chitchat_prompt(
            context,
            self.opt.delimiter,
            loss_on_last_turn=last_turn_mask_flag,
            no_query_mask=no_mask_flag,
        )
        if self.opt.add_bos and context_vec[0] != self.tokenizer.start_token_id:
            assert type(self.tokenizer.start_token_id) is int
            context_vec.insert(0, self.tokenizer.start_token_id)
            loss_mask.insert(0, 0)
        return context_vec, loss_mask

    def _build_chitchat_prompt(
        self,
        context: List[Tuple[str, str]], 
        dialog_sep: str=None, 
        loss_on_last_turn=False, 
        no_query_mask=False, 
        add_generation_suffix=False, 
        **kwargs
    ):
        
        assert not (loss_on_last_turn and no_query_mask)
        if dialog_sep is None:
            dialog_sep: str = self.opt.delimiter

        def _encode_one(prefix: str, content: str, suffix: str, is_output: bool = False):
            if is_output or no_query_mask:
                encoded_role, encoded_content, encoded_suffix = (
                    self.tokenizer.txt2vec(prefix), 
                    self.tokenizer.txt2vec(content + suffix),
                    []
                )
            else:
                encoded_role, encoded_content, encoded_suffix = (
                    [],
                    self.tokenizer.txt2vec(prefix + content + suffix),
                    []
                )
            return encoded_role, encoded_content, encoded_suffix

        idxs_encoded = []
        idxs_mask = []

        prefix_template: str = self.opt.prefix_template
        # sep_ids = self.tokenizer.txt2vec(dialog_sep)

        for i, (role, content) in enumerate(context):
            suffix_sep = dialog_sep # if i < len(context) - 1 or add_generation_suffix else ""
                
            if role == 'assistant':
                # response turn
                encoded_role, encoded_content, encoded_suffix = _encode_one(prefix_template.format(role=role), content, suffix_sep, is_output=True)
                content_mask = [int(not loss_on_last_turn or i == len(context) - 1)] * len(encoded_content)
            else:
                if role not in ('user', 'human', 'system', 'document', 'memory', 'function', 'ipython', 'tool', 'tool_calls'):
                    logging.warn(f"Found unknown role={role}")
                encoded_role, encoded_content, encoded_suffix = _encode_one(prefix_template.format(role=role), content, suffix_sep)
                content_mask = [int(no_query_mask)] * len(encoded_content)

            idxs_encoded.extend(encoded_role + encoded_content + encoded_suffix)
            idxs_mask.extend([0] * len(encoded_role) + content_mask + [0] * len(encoded_suffix))

        if add_generation_suffix:
            idxs_encoded.extend(self.tokenizer.txt2vec(prefix_template.format(role='assistant')))
            idxs_mask.extend([0] * (len(idxs_encoded) - len(idxs_mask)))

        assert len(idxs_encoded) == len(idxs_mask)
        return idxs_encoded, idxs_mask
    
    def get_token_length_fn(self, item):
        return len(item['input_ids'])

    def _compose_one_sequence(self, items):
        input_ids = []
        loss_mask = []
        labels = []
        position_ids = []
        cu_seqlens = []
        cur_seqlen = 0
        if not isinstance(items, list):
            items = [items]
        for item in items:
            input_ids += item['input_ids']
            labels += item['input_ids'][1:] + [self.pad_label_id]
            loss_mask += item['loss_mask'][1:] + [0]
            cu_seqlens.append(cur_seqlen)
            cur_seqlen += len(item['input_ids'])
            position_ids += list(range(len(item['input_ids'])))
        cu_seqlens.append(cur_seqlen)
        token_count = len(input_ids)

        res = {}
        res['tokens'] = torch.LongTensor(input_ids)
        res['labels'] = torch.LongTensor(labels)
        res['loss_mask'] = torch.LongTensor(loss_mask)
        res['position_ids'] = torch.LongTensor(position_ids)
        res['token_count'] = token_count
        res['cu_seqlens'] = cu_seqlens
        return res

    def _collate_item(self, item, max_length, pad_id):
        item = torch.nn.functional.pad(item, (0, max_length - item.shape[0]), value=pad_id)
        return item

    def create_batch(self, items):
        res = {}
        max_token_count = max([i['token_count'] for i in items])
        if self.ceil_to_nearest:
            max_token_count = self._ceil_to_nearest(max_token_count, self.pad_seq_length_to_mult)
        for k in items[0]:
            if k == 'tokens':
                res[k] = torch.stack([self._collate_item(item[k], max_token_count, self.pad_token_id) for item in items])
            elif k == 'labels':
                res[k] = torch.stack([self._collate_item(item[k], max_token_count, self.pad_label_id) for item in items])
            elif k in {'loss_mask', 'position_ids'}:
                res[k] = torch.stack([self._collate_item(item[k], max_token_count, 0) for item in items])
            elif k == 'token_count':
                res[k] = [item['token_count'] for item in items]
            elif k == 'cu_seqlens':
                for item in items:
                    if item[k][-1] < max_token_count:
                        if self.cu_seqlen_use_old_pack:
                            item[k][-1] = max_token_count
                        else:
                            item[k].append(max_token_count)
                    item[k] = torch.IntTensor(item[k])
                max_seq_count = max(len(item[k]) for item in items)
                res[k] = torch.stack([self._collate_item(item[k], max_seq_count + 1, -1) for item in items])
        res['attention_mask'] = torch.LongTensor([1] * len(items))
        res['cu_seqlens_argmin'] = torch.argmin(res['cu_seqlens'], dim=1, keepdim=True)
        seqlens = res['cu_seqlens'][:, 1:] - res['cu_seqlens'][:, :-1]
        max_seqlen, _ = seqlens.max(dim=1, keepdim=True)
        res['max_seqlen'] = max_seqlen
        # create cu_seqlens_unpadded, since we didn't pad any token between sequences during the sequence composing
        # we simply clone the cu_seqlens and cu_seqlens_argmin here
        res['cu_seqlens_unpadded'] = res['cu_seqlens'].clone()
        res['cu_seqlens_unpadded_argmin'] = res['cu_seqlens_argmin'].clone()
        return res

    def _ceil_to_nearest(self, n, m):
        return (n + m - 1) // m * m
    
    def batch_transform(self, list_of_items, is_last_batch=False):
        for items in list_of_items:
            one_sequence = self._compose_one_sequence(items)
            self.micro_batch.append(one_sequence)
            if len(self.micro_batch) == self.batch_size:
                one_batch = self.create_batch(self.micro_batch)
                self.micro_batch = []
                yield one_batch
        if is_last_batch:
            if self.micro_batch:
                one_batch = self.create_batch(self.micro_batch)
                self.micro_batch = []
                yield one_batch

    def __getstate__(self):
        return self.__dict__
    
    def __setstate__(self, states):
        self.__dict__.update(states)


class PPOProcessor:
    def __init__(self, cfg, tokenizer, collate_fn):
        self.tokenizer = tokenizer
        self.add_eod = cfg.model.data.get("append_eod", False)
        seq_length = cfg.model.data.seq_length
        if "length_params" in cfg.model.ppo:
            max_sample_length = seq_length - cfg.model.ppo.length_params.max_length
        else:
            max_sample_length = seq_length // 2
        self.max_sample_length = max_sample_length
        self.collate_fn = collate_fn

    def transform(self, sample, is_last_sample=False):
        text = sample["text"]
        text_ids = self.tokenizer.text_to_ids(text)
        if len(text_ids) > 0 and self.add_eod:
            text_ids.append(self.tokenizer.eos_id)
        if len(text_ids) > self.max_sample_length:
            return
        sample_tensor = torch.tensor(text_ids, dtype=torch.int64)
        output = {
            "text": sample_tensor,
            "length": sample_tensor.shape[0],
            "loss_multiplier": True,
        }
        return [output]
    
    def batch_transform(self, items, is_last_batch=False):
        return [self.collate_fn(items)]


class DPOProcessor(SFTProcessor):
    def __init__(
        self,
        hf_model_name,
        prompt_style,
        max_seq_len,
        add_bos,
        batch_size,
        micro_batch_size,
        ceil_to_nearest=False,
        ensure_common_tokens=False,
        default_chosen_reward=1.0,
        default_rejected_reward=0.0,
        pad_label_id=-100,
        pad_reward_id=-1000,
        cu_seqlen_use_old_pack=False,
    ):
        super().__init__(hf_model_name, prompt_style, max_seq_len, add_bos, batch_size, micro_batch_size, ceil_to_nearest, pad_label_id)
        self.ensure_common_tokens = ensure_common_tokens
        self.default_chosen_reward = default_chosen_reward
        self.default_rejected_reward = default_rejected_reward
        self.pad_reward_id = pad_reward_id
    
    def decode_fn(self, line):
        session = json.loads(line)
        edited, chosen, rejected = session.get('edited', None), session.get('chosen', None), session.get('rejected', None)
        responses = []
        output = []
        if edited and edited.get('content'):
            responses.append(edited['content'])
        if chosen and chosen.get('content'):
            responses.append(chosen['content'])
        if rejected and rejected.get('content'):
            responses.append(rejected['content'])
        if len(responses) < 2:
            return output
        if session['messages'][-1]['role'] == 'assistant':
            return output

        for i_yw in range(len(responses) - 1):
            for i_yl in range(i_yw + 1, len(responses)):
                if responses[i_yw] != responses[i_yl]:
                    output.append({
                        'messages': session['messages'],
                        'responses': [responses[i_yw], responses[i_yl]],
                        'ranks': [0, 1],
                    })
        return output

    def mask_common_token(self, yw_text_vec, yw_loss_mask, yl_text_vec, yl_loss_mask):
        for i in range(min(len(yw_text_vec), len(yl_text_vec))):
            if yw_loss_mask[i] == yl_loss_mask[i] == 0:
                continue
            if yw_text_vec[i] == yl_text_vec[i]:
                yw_loss_mask[i] = yl_loss_mask[i] = -1
            else:
                break

        for i in range(1, min(len(yw_text_vec), len(yl_text_vec))):
            if yw_loss_mask[-i] == yl_loss_mask[-i] == 0:
                continue
            if yw_text_vec[-i] == yl_text_vec[-i]:
                yw_loss_mask[-i] = yl_loss_mask[-i] = -1
            else:
                break

    def get_token_length_fn(self, item):
        return len(item['yw_input_ids']) + len(item['yl_input_ids'])

    def transform(self, item, is_last_sample=False):
        context = [(turn['role'], turn['content']) for turn in item['messages']]
        responses = item['responses']
        ranks = item['ranks']
        yw_idx, yl_idx = 0, 1
        assert ranks[yw_idx] < ranks[yl_idx]
        yw, yl = responses[yw_idx], responses[yl_idx]
        yw_context_vec, yw_loss_mask = self._encode_one(context + [('assistant', yw)], True, False)
        yl_context_vec, yl_loss_mask = self._encode_one(context + [('assistant', yl)], True, False)
        if self.ensure_common_tokens:
            self.mask_common_token(yw_context_vec, yw_loss_mask, yl_context_vec, yl_loss_mask)
        yield from [
            {
                "yw_input_ids": yw_context_vec,
                "yw_loss_mask": yw_loss_mask,
                "yl_input_ids": yl_context_vec,
                "yl_loss_mask": yl_loss_mask,
                "chosen_reward": item.get("chosen_reward", self.default_chosen_reward),
                "rejected_reward": item.get("rejected_reward", self.default_rejected_reward)
            }
        ]

    def _compose_one_sequence(self, items):
        if not isinstance(items, list):
            items = [items]
        res = super()._compose_one_sequence(items)
        res['rewards'] = torch.FloatTensor([i['reward'] for i in items])
        loss_mask = res.pop('loss_mask')
        # nemo aligner use label < -1 as the loss mask
        # so we create the masked label inadvance here
        res['labels'][loss_mask==0] = self.pad_label_id
        return res

    def create_batch(self, items):
        res = super().create_batch(items)
        max_num_sequences = max(len(item['rewards']) for item in items)
        res['rewards'] = torch.stack([self._collate_item(item['rewards'], max_length=max_num_sequences, pad_id=self.pad_reward_id) for item in items])
        # nemo dpo needs input_ids instead of tokens
        res['input_ids'] = res.pop('tokens')
        return res

    def batch_transform(self, list_of_items, is_last_batch=False):
        for items in list_of_items:
            recreated_items = []
            if not isinstance(items, list):
                items = [items]
            for item in items:
                recreated_items.append(
                    {
                        'input_ids': item['yw_input_ids'],
                        'loss_mask': item['yw_loss_mask'],
                        'reward': item['chosen_reward'],
                    }
                )
                recreated_items.append(
                    {
                        'input_ids': item['yl_input_ids'],
                        'loss_mask': item['yl_loss_mask'],
                        'reward': item['rejected_reward'],
                    }
                )
            one_sequence = self._compose_one_sequence(recreated_items)
            self.micro_batch.append(one_sequence)
            if len(self.micro_batch) == self.batch_size:
                one_batch = self.create_batch(self.micro_batch)
                self.micro_batch = []
                yield one_batch
        if is_last_batch:
            if self.micro_batch:
                one_batch = self.create_batch(self.micro_batch)
                self.micro_batch = []
                yield one_batch
