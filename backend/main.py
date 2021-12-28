import uuid

import cv2
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import numpy as np
from PIL import Image

import config
import inference

app = FastAPI()

classifier = config.build_model()


@app.get("/")
async def read_root():
    return {"message": "Welcome from the API"}


@app.post("/predict")
async def get_image(file: UploadFile = File(...)):
    # image = np.array(Image.open(file.file))
    image = inference.image_loader(file.file)
    # image = Image.open(file.file)
    output = inference.predict(classifier, image)
    name = f"/storage/{str(uuid.uuid4())}.jpg"
    cv2.imwrite(name, np.array(Image.open(file.file)))
    return {"name": name, "character": output}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
