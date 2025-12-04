import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


st.title("Bar Chart")
st.write("Kelompok : 1")
st.markdown('''
    - Pramana Rahmansah Putra (0110122051)
''')


#data
data = {
    'jurusan' : ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science'],
    'Jumlah Mahasiswa' : [120, 150, 100, 80]
    }
df = pd.DataFrame(data)

#Streamlit Bar Chart
st.title('Basic Bar Chart - Jumlah Mahasiswa per Jurusan')
st.bar_chart(df.set_index('jurusan'))

st.title("Basic Bar Chart Menggunakan Matplotlib")
fig, ax = plt.subplots()
ax.bar(data['jurusan'], data['Jumlah Mahasiswa'], color = 'skyblue')
ax.set_title = ('Jumlah Mahasiswa Per Jurusan')
ax.set_xlabel = ('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

st.pyplot(fig)

#Kustomisasi Matplotlob bar chart
st.title("Basic Bar Chart Menggunakan Matplotlib")
fig, ax = plt.subplots()
colors = ['blue', 'green', 'orange', 'red']
bars = ax.bar(df['jurusan'], df['Jumlah Mahasiswa'], color =colors)
ax.set_title = ('Jumlah Mahasiswa Per Jurusan')
ax.set_xlabel = ('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')
for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5, str(bar.get_height()), ha ='center')

st.pyplot(fig)

#Multiple bar chart
st.title('Multiple Bar Chart')

#Data Tambahan
data_2023 = [120, 150, 100, 80]
data_2024 = [140, 160, 110, 90]

x = range(len(data['jurusan']))
width   = 0.4

fig, ax = plt.subplots()
ax.bar(x, data_2023, width=width, label='2023', color = 'skyblue')
ax.bar([p + width/2 for p in x], data_2024, width=width, label='2024', color='orange')
ax.set_title = ('Jumlah Mahasiswa Per Jurusan')
ax.set_xlabel = ('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')
ax.set_xticks([p + width /2 for p in x])
ax.set_xticklabels(data['jurusan'])
ax.legend()


st.pyplot(fig)