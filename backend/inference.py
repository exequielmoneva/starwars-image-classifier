import os

import torch
from PIL import Image
from typing import Optional, IO

import config

loader = config.LOADER


def image_loader(image_file: Optional[IO]) -> list:
    """
    Loads image, returns tensor
    :param image_file: String
    :return: Torch tensor
    """
    picture = Image.open(image_file)
    picture = loader(picture).float()
    picture = torch.autograd.Variable(picture, requires_grad=True)
    picture = picture.unsqueeze(0)
    return picture


def predict(model, img: list) -> str:
    """

    :param model: Pytorch model
    :param img: Torch tensor
    :return: Name of the predicted character
    """
    was_training = model.training
    model.eval()

    with torch.no_grad():
        output = model(img)
        prediction = int(torch.max(output.data, 1)[1].numpy())
        model.train(mode=was_training)

    return config.CLASS_NAMES[prediction]
