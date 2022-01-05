import redis
import requests
import streamlit as st

# r_front = redis.Redis()

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
        res = requests.post('http://starwars-image-classifier_backend:8080/predict', files=files, timeout=12)
        img_path = res.json()
        st.header(f"Predicted Character: {img_path.get('character')}")
        st.image(image, use_column_width=True)

# Hide Streamlit's footer
hide_footer_style = """
    <style>
    .reportview-container .main footer {visibility: hidden;}    
    </style>
    """
st.markdown(hide_footer_style, unsafe_allow_html=True)

# Add personal footer
footer = """
<style>
.footer {
font-family:sans-serif;
position: fixed;
left: 0;
bottom: 0;
width: 100%;
color: tomato;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by <a text-align: center;' href="https://github.com/exequielmoneva" target=”_blank”>
Exequiel Moneva</a></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

# Hide Main Menu
hide_menu = """
<style>
#MainMenu{
    visibility:hidden;
}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)
