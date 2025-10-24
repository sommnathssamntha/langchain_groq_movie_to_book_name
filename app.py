import streamlit as st
import requests


st.title("🎬 Movie to Book Inference")

movie_title = st.text_input("Enter a movie title:")
if st.button("Get Book Name"):
    response = requests.post("http://localhost:8000/get_book_name/invoke",
                             json={"input": {"title": movie_title}})
    st.write(response.json()["output"])