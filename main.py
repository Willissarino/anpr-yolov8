from ultralytics import YOLO
from PIL import Image
from fastapi import FastAPI, File
from starlette.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from config import get_image_from_bytes

import cv2
import json
import numpy as np

# Load Model
model = YOLO("yolo-model/anpr_v8.pt")

app = FastAPI(title="YOLOV8 API")

origins = [
    "http://localhost",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
     CORSMiddleware,
     allow_origins=origins,
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
)

@app.post("/img-to-json")
async def detect_img_return_json(file: bytes = File(...)):
    input_image = get_image_from_bytes(file)
    results = model(input_image,save_crop=False,save=False,detect_plate=True)
    
    for r in results:
        coords = r.boxes.xyxy.tolist() # Coordinates
        conf = r.boxes.conf.tolist() # Confidence score
        names = r.names # Class Names
        num_plate = r.num_plate # Number Plates
        
    
    # Define a list of dictionaries for each coordinate in the 'coords' list
    result_list = []
    for i, coord in enumerate(coords):
        result_dict = {
            "num": i,
            "xmin": coord[0],
            "ymin": coord[1],
            "xmax": coord[2],
            "ymax": coord[3],
            "confidence": conf[i],
            "class": names[0],
            "num_plate": num_plate[i]
        }

        result_list.append(result_dict)

# Return the result list as a dictionary with key 'result'
    return {"result": result_list}
