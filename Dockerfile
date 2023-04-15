FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update
RUN apt-get install -y libgl1
RUN apt-get install -y libglib2.0-0
RUN pip3 install --upgrade pip
RUN pip3 install "fastapi[all]"

COPY . .

WORKDIR /app/ultralytics
RUN pip install -e .

WORKDIR /app/paddle_openvino
RUN pip install -e .

# Clean up
RUN apt-get clean

EXPOSE 8000

WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
