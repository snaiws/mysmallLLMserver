FROM nvidia/cuda:12.5.1-cudnn-devel-ubuntu22.04

# 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    git \
    wget \
    curl \
    # python3 \
    # python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Python 환경 설정
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TORCH_COMPILE_STROBELIGHT=0

# # 작업 디렉토리 설정
WORKDIR /workspace/Projects
COPY . .
# 필요한 Python 패키지 설치
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:/root/.local/bin:${PATH}"
RUN uv sync && uv add uvicorn


# CMD ["uv", "run", "python", "src/app.py"]
# CMD ["tail", "-f", "/dev/null"]