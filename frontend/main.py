import requests
import streamlit as st
from PIL import Image

# https://discuss.streamlit.io/t/version-0-64-0-deprecation-warning-for-st-file-uploader-decoding/4465
st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("Star Wars character classifier")
st.markdown(
    "Upload an image of your favourite character and and the Machine Learning model will try to guess the name!"
)

# displays a file uploader widget
image = st.file_uploader("Choose an image")

# displays a button
if st.button("Predict"):
    if image is not None:
        files = {"file": image}
        # files = {"file": Image.open(image)}
        res = requests.post(f"http://127.0.0.1:8080/predict", files=files, timeout=3)
        img_path = res.json()
        # image = Image.open(img_path.get("name"))
        st.header(f"Predicted Character: {img_path.get('character')}")
        # st.image(image, width=500)