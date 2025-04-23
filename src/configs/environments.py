import os
from dataclasses import dataclass

from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

@dataclass
class EnvDefineUnit:
    '''
    환경변수
    나중에 바뀌는 서버환경마다 적응시킬 수 있을까
    '''
    PATH_DATA_DIR : str = os.getenv("PATH_DATA_VIRTUAL", "")
    PATH_MODEL_DIR : str = os.getenv("PATH_MODEL_VIRTUAL", "")
    PATH_LOG_DIR : str = os.getenv("PATH_LOG_VIRTUAL", "")
    DEBUG_MODE : str = os.getenv("DEBUG_MODE", "false").lower() == "true"
    PORT : str = os.getenv("PORT_APP")
    