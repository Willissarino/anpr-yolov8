FROM nvidia/cuda:12.0.1-cudnn8-runtime-ubuntu22.04
FROM python:3.9

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python3.9 && \
    apt-get install -y python3-pip && \
    apt-get install -y libgl1 && \
    python -m pip install --upgrade pip && \
    pip install "fastapi[all]"

COPY . .

WORKDIR /app/ultralytics
RUN pip install -e .

WORKDIR /app/paddle_openvino
RUN pip install -e .

EXPOSE 8000

WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
