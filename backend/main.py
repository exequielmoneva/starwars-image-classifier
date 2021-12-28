import uvicorn
from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile

import config
import inference

app = FastAPI()

classifier = config.build_model()


@app.get("/health")
async def read_root():
    """
    Health endpoint
    :return: Status message
    """
    return {"message": "API is up"}


@app.post("/predict")
async def get_image(file: UploadFile = File(...)) -> dict:
    """
    Receives the image for the prediction
    :param file:
    :return:
    """
    image = inference.image_loader(file.file)
    output = inference.predict(classifier, image)

    return {"character": output}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
