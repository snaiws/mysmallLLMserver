
from vllm import AsyncLLMEngine, AsyncEngineArgs, SamplingParams

class VLLMModel:
    def __init__(self, model_name, model_path, model_params):
        self.model_name = model_name
        self.model_path = model_path
        self.model_params = model_params
        self.model = None

    # vLLM 엔진 설정 및 초기화
    async def initialize_engine(self):

        # vLLM 엔진 인자 설정 - 요청하신 형식과 유사하게 설정
        engine_args = AsyncEngineArgs(
            model=self.model_name,
            download_dir=self.model_path,
            **self.model_params
        )
        
        self.model = AsyncLLMEngine.from_engine_args(engine_args)
    async def generate(self,
                       prompt,
                        request_id,
                        sampling_params,
                       ):

        sp = SamplingParams(**sampling_params)

        # start the generation
        results_generator = self.model.generate(
            prompt,
            sp,
            request_id)  

        final_output = None
        async for request_output in results_generator:
            final_output = request_output

        return final_output.outputs[0].text
    
    

