import cv2
import numpy as np
import io

from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse
from utils import tilt_shift, pixelation

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}


@app.get("/hi/{name}")
async def say_hello(name: str):
    return {"message": f"Hi {name}"}


@app.post("/miniature")
async def miniature(file: UploadFile):
    data = await file.read()

    np_array = np.fromstring(data, np.uint8)
    img_np = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    miniatured_image = tilt_shift(img_np)

    _, miniatured_image_encoded = cv2.imencode('.jpg', miniatured_image)

    return StreamingResponse(io.BytesIO(miniatured_image_encoded.tobytes()), media_type="image/jpeg")


@app.post("/pixelate/{width}/{height}")
async def pixelate(file: UploadFile, width: int, height: int):
    data = await file.read()

    np_array = np.fromstring(data, np.uint8)
    img_np = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    pixelated_image = pixelation(img_np, width, height, 10)

    _, pixelated_image_encoded = cv2.imencode('.jpg', pixelated_image)

    return StreamingResponse(io.BytesIO(pixelated_image_encoded.tobytes()), media_type="image/jpeg")
