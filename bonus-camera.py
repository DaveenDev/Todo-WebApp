import streamlit as st
from PIL import Image

def convert_tograyscale(image):
    img = Image.open(image)
    gray_img = img.convert("L")
    return gray_img


uploaded_image = st.file_uploader("Upload Image")

if uploaded_image:
    grayed_img = convert_tograyscale(uploaded_image)
    st.image(grayed_img)


with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    grayed_img = convert_tograyscale(camera_image)
    st.image(grayed_img)


