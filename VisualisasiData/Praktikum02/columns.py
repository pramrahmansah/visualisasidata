import streamlit as st
col1, col2 = st.columns(2)

col1.write("First Column")
col1.image("Assets/animal.jpg")

col2.write("Second Column")
col2.image("Assets/animal1.jpg")
