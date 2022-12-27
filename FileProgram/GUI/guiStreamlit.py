from Algorithm.checking import cek_kalimat

import sys
sys.path.append("C:\Python311\Lib\site-packages\streamlit")
import streamlit as st

def runStreamlit():
    st.write("""
    # Application of CFG in Syntactic Parsing
    Simple Application for Checking *Standard Sentence Pattern* for Fulfill The Final Project of the "Teori Bahasa dan Automata" Subject at Teknik Informatika Udayana University's Lectures.
    _____________________________________
    Kelompok 1
    Kameliya Putri (2108561019)
    Yehezkiel Batara Lumbung (21018561048)
    Ketut Agus Cahyadi Nanda (2108561079)
    I Gede Ngurah Arya Wira Putra (2108561119)
    """)

    input = st.text_input("Input the String that you want to check:")
    cek = st.button("Check It!")

    if cek:
        if cek_kalimat(input) == 1:
            st.success("It's Standard Sentence! Congratulations...")
        else:
            st.error("Unfortunately, Your String is non-Standard. Try Again!")