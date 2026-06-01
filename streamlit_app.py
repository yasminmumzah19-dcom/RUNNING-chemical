import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Audit Kompatibilitas Bahan Kimia",
    page_icon="🧪",
    layout="centered"
)

st.title("🧪 Aplikasi Audit Kompatibilitas Penyimpanan Bahan Kimia")

st.write("""
Aplikasi ini digunakan untuk memeriksa apakah dua kelompok bahan kimia
aman disimpan berdekatan dalam laboratorium.
""")

st.sidebar.header("Informasi")
st.sidebar.write("Audit Kompatibilitas Penyimpanan Bahan Kimia")

kelompok = [
    "Flammable",
    "Corrosive",
    "Oxidizing",
    "Toxic"
]

bahan1 = st.selectbox(
    "Pilih Kelompok Bahan Kimia Pertama",
    kelompok
)

bahan2 = st.selectbox(
    "Pilih Kelompok Bahan Kimia Kedua",
    kelompok
)

aturan = {

("Flammable","Oxidizing"):
"Bahaya Kebakaran",

("Oxidizing","Flammable"):
"Bahaya Kebakaran",

("Corrosive","Flammable"):
"Reaksi Berbahaya",

("Flammable","Corrosive"):
"Reaksi Berbahaya",

("Oxidizing","Corrosive"):
"Perlu Pemisahan",

("Corrosive","Oxidizing"):
"Perlu Pemisahan",

("Toxic","Corrosive"):
"Risiko Gas Beracun",

("Corrosive","Toxic"):
"Risiko Gas Beracun"
}

if st.button("Audit Penyimpanan"):

    if bahan1 == bahan2:

        st.success(
            "✅ Kelompok bahan sama, umumnya dapat disimpan dalam area yang sama dengan prosedur yang sesuai."
        )

    elif (bahan1,bahan2) in aturan:

        pesan = aturan[(bahan1,bahan2)]
