import streamlit as st

st.set_page_config(
    page_title="Streamlit Házi App",
    layout="wide",
)

st.title("👋 Üdvözlet a Házimban!👋")

st.markdown("""
Ez egy **egyszerű** alkalmazás, amelyet a [Streamlit](https://streamlit.io/) hoztam létre.
A Streamlit lehetővé teszi, hogy megcsináljam a házim!
""")

nev = st.text_input("Mi a neved?")
if nev:
    st.write(f"Szia, {nev}! Üdvözöllek az alkalmazásomban")