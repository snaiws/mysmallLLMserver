
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field



# 요청 모델 정의
class GenerationRequest(BaseModel):
    prompt: str = "안녕"
    sampling_params:dict = {"max_tokens":2000}

class GenerationResponse(BaseModel):
    id: str
    text: str
    usage: Dict[str, int]