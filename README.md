## ANPR  [Yolov8, FastAPI, PaddleOCR]

## Run Locally

Clone the project

```bash
  git clone https://github.com/Willissarino/anpr_yolov8.git
```

Go to the project directory // Install paddle_openvino & yolov8 seperately

```bash
  cd ultralytics
  cd paddle_openvino
```

Install dependencies

```bash
  pip install -e.
  pip install "fastapi[all]"
```

Start the server

```bash
  uvicorn main:app --reload
```
