
import streamlit as st

st.title("Buttons dan Sliders")

# Tombol (Button)
if st.button("Klik Saya"):
    st.write("Tombol telah ditekan!")

# Checkbox
agree = st.checkbox("Setuju dengan syarat dan ketentuan")
if agree:
    st.write("Terima kasih telah menyetujui!")

# Radio Button
genre = st.radio(
    "Pilih genre favoritmu:",
    ('Action', 'Comedy', 'Drama')
)
st.write(f"Genre yang dipilih: {genre}")

# Selectbox (Drop-Down)
option = st.selectbox(
    "Pilih bahasa pemrograman:",
    ('Python', 'Java', 'C++', 'JavaScript')
)
st.write(f"Kamu memilih: {option}")

# Multiselect
options = st.multiselect(
    "Pilih hobi kamu:",
    ['Membaca', 'Olahraga', 'Gaming', 'Musik']
)
st.write(f"Hobi yang dipilih: {options}")

# Slider
nilai = st.slider("Pilih angka:", 0, 100, 25)
st.write(f"Nilai yang dipilih: {nilai}")

