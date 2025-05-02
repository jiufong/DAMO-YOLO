FROM nvidia/cuda:12.8.1-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y \
    python3.10 python3-pip python3-dev git curl libgl1-mesa-glx libglib2.0-0\
    && rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1

WORKDIR /

COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

COPY damo /opt/ml/code/damo
COPY tools /opt/ml/code/tools
COPY tools/train.py /opt/ml/code/train.py
COPY inputs /opt/ml/code/inputs

WORKDIR /opt/ml/code

ENV PYTHONPATH=/:${PYTHONPATH}
ENV SAGEMAKER_PROGRAM=train.py
