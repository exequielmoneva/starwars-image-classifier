from typing import Union

import torch
from torch.jit import RecursiveScriptModule
from torchvision import transforms

IMSIZE = 256
LOADER = transforms.Compose([transforms.Scale(IMSIZE), transforms.ToTensor()])

CLASS_NAMES = ['Admiral Ackbar',
               'Admiral Piett',
               'Anakin Skywalker',
               'BB-8',
               'Bail Organa',
               'Bib Fortuna',
               'Boba Fett',
               'Bodhi Rook',
               'C-3PO',
               'Captain Phasma',
               'Cassian Andor',
               'Chewbacca',
               'Dark Sidious',
               'Darth Maul',
               'Darth Vader',
               'Finn (FN-2187)',
               'General Grievous',
               'General Hux',
               'Grand Moff Tarkin',
               'Greedo',
               'Han Solo',
               'Jabba the Hutt',
               'Jango Fett',
               'Jar Jar Binks',
               'Jyn Erso',
               'K-2SO',
               'Kenobi',
               'Kylo Ren',
               'Lando Calrissian',
               'Luke Skywalker',
               'Mace Windu',
               'Maz Kanata',
               'Nien Nunb',
               'Obi-Wan',
               'Orson Krennic',
               'Padme Amidala',
               'Poe Dameron',
               'Princess Leia Organa',
               "Qi'ra",
               'Qui-Gon Jinn',
               'R2-D2',
               'Rey',
               'Rose Tico',
               'Saw Gerrera',
               'Supreme Leader Snoke',
               'Tobias Beckett',
               'Vice-Admiral Holdo',
               'Watto',
               'Wedge Antilles',
               'Wicket W. Warrick',
               'Yoda']


def build_model():
    """
    Load the model for inference
    :return: Loaded Pytorch model
    """
    model_ft = torch.load("backend/model/entire_model.pt")
    model_ft.eval()

    return model_ft
