import streamlit as st 
import pandas as pd # untuk mengelola data dalam bentuk tabel(dataframe)
import numpy as np # untuk membuat data numerik acak 
import altair as alt #untuk membuat chart

st.title("Praktikum Streamlit")
st.subheader("Bagian 2 - data Element")
st.markdown("""
1. Muhammad Al Faruq - 0110122057
1. Kays Elhaq Rabbani - 0110222218
1. Ahmad Fauzi Nugroho - 0110222293
""")

#DataFrame : Struktur  data berbentuk tabel (baris dan kolom) yang disediakan oleh library pandas

st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

#menampilkan dataframe
st.dataframe(df)

#Highlight Nilai minimum
st.subheader("Highlight Minimum Value di DataFrame")

# highlight nilai terkecil disetiap kolom dataframe
#aixs=0 bekerja perkolom
st.dataframe(df.style.highlight_min(axis=0))

#Tabel Statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

st.table(df)

#Metrics: komponen tampilan angka penting
st.subheader("Metrics")
#Menampilkan metrik tunggal (nilai utama + perubahan nilai)

#Mettics Tunggal
st.metric(label="Temperature", value="31 C", delta="1.2 C") #kenaikan 1.2 C

#delta_color digunakan untuk memberi warna sesuai arah perubahan
# - "normal" (default): naik lanjut hijau, turun lanjut merah
# - "inverse": kebalikannya (naik lanjut merah)
# - "off": tidak menampilkan warna perubahan

#definisikan variable metrics
col1, col2, col3 = st.columns(3)

#menampilkan indikator
col1.metric("Curah Hujan", "100 cm", "10 cm") # naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse") #naik tapi buruk
col3.metric(label="pelanggan", value=100, delta=10, delta_color="off") #netral (tidak baik, tidak buruk)

#menampilkan metril tambahan dengan nilai kosong atau nol
st.metric(label="Speed", value=None, delta=0) #kosong #naik baik karena di setting default
st.metric("Trees", "91456", "-1132649") #Penurunan

# Membuat DataFrame dengan 30 baris dan 10 kolom berisi angka acak
df = pd.DataFrame(
    np.random.rand(30, 10),
    columns=['col_no %d' % i for i in range(10)]
)

# Menampilkan beberapa data sekaligus dengan st.write
st.write('Here is our Data', df, 'Data is in dataframe format.\n', "\nWrite is Super function")

# Defining random Values for Chart
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b']
)

# Defining Chart
chart = alt.Chart(df).mark_bar().encode(
    x='a',
    y='b',
    tooltip=['a', 'b']
)

# Defining Chart in write() function
st.write(chart)

# Math calculations with no functions defined
"Adding 5 & 4 =", 5 + 4

# Displaying Variable 'a' and its value
a = 5
'a', a

# Markdown with Magic
"""
# Magic Feature
Markdown working without defining its function explicitly.
"""

# Dataframe using magic
import pandas as pd
df = pd.DataFrame({'col': [1, 2]})
'dataframe', df