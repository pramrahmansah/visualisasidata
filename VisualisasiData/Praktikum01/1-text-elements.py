import streamlit as st

#text element
#header - Membuat tulisan header
st.title("Praktikum1")
#st.header("Ini Header") 
st.subheader("Text Elements")
# st.text("Ini Text Biasa Tanpa Format")
st.markdown("""
1. Pramana Rahmansah Putra - 010122051
2. Roza Kurniawan Nur Wakid - 0110222124
3. IMAD HASAN AQIL - 0110222166            
""")
# st.caption("Ini Caption")



# Bagian Menampilkan Rumus (Latex)
st.latex(r'''\cos^\theta = 1-2\sin^2\theta ''') # Rumus Trigonometri

st.latex(r''' (a+b)^2 +b^2 + 2ab ''') #rumus kuadrat binominal

# Bagian Menampilkan  Kode Program
st.header("Displaying Code")
st.subheader("Python Code")

code = '''
def hello():
    print("Hello,Streamlit)
'''

#st.code untuk menampilkan potongan kode dengan format rapi dansytax highlighting
st.code(code, language='python')


st.subheader("Java Code")
st.code("""
    public class GFG {
        public static void main(String arg[]) {
            System.out.printIn{"Hello World!);
        }
    }
""", language='java')


st.subheader("Javascript Code")
st.code("""
<script>
try {
      addalert("Welcome Guest1"); //kesalahan ketik addalaert sengaja dibuat untuk menimbulkan error
        }
catch(err) {
        document.getElementById("demo").innerHTML - err.message; //
        menampilkan pesan error dielemen HTML dengan id 'demo'
        }
        </script>        
""", language='javascript')
#kode ini menunjukan contoh bagaimana menangani kode error (exception) di Javascript 
#hasilnya tidak dijalankan di streamlit, tapi 