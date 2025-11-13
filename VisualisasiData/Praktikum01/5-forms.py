import streamlit as st
from datetime import datetime

st.title("Contoh Form Input Data")

# Membuat Form
with st.form("form_input"):
    name = st.text_input("Nama Lengkap")
    age = st.number_input("Umur", min_value=1, max_value=100, step=1)
    gender = st.radio("Jenis Kelamin", ('Laki-laki', 'Perempuan'))
    tanggal_lahir = st.date_input("Tanggal Lahir")
    waktu_input = st.time_input("Waktu Input", value=datetime.now().time())
    warna_favorit = st.color_picker("Pilih warna favorit")
    file_upload = st.file_uploader("Upload file (opsional)")
    
    # Tombol Submit
    submitted = st.form_submit_button("Kirim")

if submitted:
    st.success("Data berhasil dikirim!")
    st.write("**Data yang kamu isi:**")
    st.write(f"Nama: {name}")
    st.write(f"Umur: {age}")
    st.write(f"Jenis Kelamin: {gender}")
    st.write(f"Tanggal Lahir: {tanggal_lahir}")
    st.write(f"Waktu Input: {waktu_input}")
    st.write(f"Warna Favorit: {warna_favorit}")
