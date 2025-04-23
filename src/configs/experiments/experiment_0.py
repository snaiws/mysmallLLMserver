from dataclasses import dataclass, field

from .base import Experiment, register  # 별도 파일에 선언된 dataclass


@register
@dataclass    
class MK1(Experiment):
    '''
    실험 파라미터
    chain / data / prompt / RAG / model로 나누어 관리
    '''
    exp_name :str = "MK1"

    # model 파라미터
    # model_name : str = "NCSOFT/Llama-VARCO-8B-Instruct"
    model_name : str = "yanolja/EEVE-Korean-10.8B-v1.0"
    
    model_params : dict = field(default_factory=lambda: 
        {
            "tensor_parallel_size" : 1,
            "trust_remote_code":True,
            "max_model_len":4096,
            "dtype":"float16",
            "quantization":"bitsandbytes",
            "load_format":"bitsandbytes",
            "gpu_memory_utilization":0.9,
        }
    )    
    sampling_params : dict = field(default_factory=lambda: 
        {
            # "n":1
            # "best_of": None
            # "realn": None
            "max_tokens": 2000
            # "min_tokens": 0
            
            # 샘플링 제어
            # "temperature": 1.0
            # "top_p": 1.0
            # "top_k": -1
            # "min_p": 0.0
            
            # 반복 제어
            # "presence_penalty": 0.0
            # "frequency_penalty":0.0
            # "repetition_penalty": 1.0
            
            # 종료 조건
            # "stop": None
            # "stop_token_ids":None
            # "ignore_eos": False
            # "include_stop_str_in_output": False
            # # "allstop_token_ids": (0)
            
            # 토큰화 관련
            # "detokenize": True
            # "skip_special_tokens":True
            # "spaces_between_special_tokens":True
            # "truncate_prompt_tokens": None
            
            # 결과 제어
            # # "output_kind": RequestOutputKind.CUMULATIVE
            # "output_text_buffer_length": 0
            # "logprobs": None
            # "prompt_logprobs":  None
            
            # 고급 제어
            # "seed":None
            # "logits_processors": None
            # # "guided_decoding":  None
            # "logit_bias": None
            # "allowed_token_ids": None
            # "extra_args":  None
            # "bad_words": None
            # # "badwords_token_ids":None
        }
    )