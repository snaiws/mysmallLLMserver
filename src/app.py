import os
import argparse
import traceback

from fastapi import FastAPI, HTTPException
import uvicorn

from core.model_inference import VLLMModel
from configs import Configs, GenerationRequest, GenerationResponse
from utils import setup_logging



parser = argparse.ArgumentParser()
parser.add_argument("--version", required=True, help="버전을 입력하세요")
args = parser.parse_args()

version = args.version

app = FastAPI(title=version)
configs = Configs(version)
env = configs.env
exp = configs.exp

logger = setup_logging(env.PATH_LOG_DIR)
model_path = os.path.join(env.PATH_MODEL_DIR, exp.model_name)

# 애플리케이션 시작 시 엔진 초기화
@app.on_event("startup")
async def startup_event():
    try:
        global llm_engine
        llm_engine = VLLMModel(exp.model_name, model_path, exp.model_params)
        response = await llm_engine.initialize_engine()
        logger.info("모델초기화")
    except Exception as e:
        e = traceback.format_exc()
        logger.error(f"모델초기화에러/{e}")


@app.post("/generate", response_model=GenerationResponse)
async def generate_text(request: GenerationRequest):
    try:
        logger.debug(f"{request.prompt}")
        request_id = f"cmpl-{hash(request.prompt) % 10000}"

        generated_text = await llm_engine.generate(
            prompt=request.prompt,
            request_id = request_id,
            sampling_params= request.sampling_params
            )
        # 토큰 사용량 계산 (근사치)
        prompt_tokens = len(request.prompt.split())
        completion_tokens = len(generated_text.split())
        
        response = GenerationResponse(
            id=request_id,
            text=generated_text,
            usage={
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": prompt_tokens + completion_tokens
            }
        )
        logger.debug(f"{response.id}/{response.text}/{response.usage}")
        return response
    except Exception as e:
        e = traceback.format_exc()
        logger.error(f"생성응답에러/{e}")
        raise HTTPException(status_code=500, detail=f"생성 오류: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model": exp.model_name}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=int(env.PORT), reload=False)