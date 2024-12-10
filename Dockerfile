FROM nvidia/cuda:12.2.2-base-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

# NVIDIA GPG 키 및 저장소 설정 추가
RUN apt-get update && apt-get install -y wget
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
RUN dpkg -i cuda-keyring_1.0-1_all.deb

# 기본 패키지 설치 (python3 관련 패키지 추가)
RUN apt-get update && apt-get install -y \
    libglib2.0-0 libsm6 libxrender-dev libxext6 \
    nano mc glances vim git \
    python3 python3-pip python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Python 심볼릭 링크 생성
RUN ln -sf /usr/bin/python3 /usr/bin/python

# PyTorch 및 필요한 Python 패키지 설치
RUN pip3 install torch torchvision torchaudio
RUN pip3 install numpy pandas matplotlib opencv-python

WORKDIR /workspace
COPY . /workspace

RUN chmod 777 preprocess_data.sh
RUN chmod 777 train.sh
RUN chmod 777 predict_submission.sh

ENV PYTHONPATH=.

CMD ["/bin/bash"]
