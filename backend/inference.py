import io
import os

import cv2 as cv
import torch
from PIL import Image

from backend import config

loader = config.LOADER


def image_loader(image_name):
    """
    Loads image, returns tensor
    :param image_name: string
    :return: torch tensor
    """
    picture = Image.open(image_name)
    picture = loader(picture).float()
    picture = torch.autograd.Variable(picture, requires_grad=True)
    picture = picture.unsqueeze(0)
    return picture


def predict(model, img):
    was_training = model.training
    model.eval()

    with torch.no_grad():
        output = model(img)
        prediction = int(torch.max(output.data, 1)[1].numpy())
        model.train(mode=was_training)

    return config.CLASS_NAMES[prediction]


"""path = [path for path in os.listdir("pred")
        if not path.endswith(".ipynb") and not path.endswith(".ipynb_checkpoints")][0]
imagen = cv.imread(os.path.join(r"pred", path))
image = image_loader(os.path.join(r"pred", path))
predict(classifier, image, imagen)
os.remove(os.path.join(r"pred", path))"""
