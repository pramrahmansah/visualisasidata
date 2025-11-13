import streamlit as st
from PIL import Image

img = Image.open("Assets/animal1.jpg")

st.title("Spaced-Out Columns")

for _ in range(2):
    cols = st.columns((3, 1, 2, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)
