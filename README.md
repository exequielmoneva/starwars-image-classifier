# Star Wars image classifier

### A Computer Vision model capable of recognize a Star Wars character from a given picture. 

# Stack of the project:
 - FastAPI
 - Streamlit
 - Pytorch

# About the model
### This Machine Learning model has been built using Pytorch and the Transfer learning technique over the [VGG16 Convolutional Network.](https://neurohive.io/en/popular-networks/vgg16/)

### My Jupyter Notebooks can be found within this repo, inside the "notebooks" folder.

# Requirements
 - Docker
 - Python 3.7 or later

# Installation
Inside the root folder of the project, run the following command

```sh
> docker-compose build
```

Then start the project with the following command

```sh
> docker-compose up
```

Now, you should be able to test the webapp at:

```
http://localhost:8501/
```
