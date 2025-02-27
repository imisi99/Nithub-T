import streamlit as st
import requests

st.header("Sentiment Analysis System")
st.write("This will detect the sentiment of the text it can be positive, negative, or neutral")
text = st.text_input("Enter the text you want to analyze", key="text")
data = {"text": text}
if st.button("Analyze"):
    response = requests.get("https://sentiment-api-uf2f.onrender.com/label", json=data)
    sentiment = response.json()["sentiment"]
    st.write(sentiment)

st.write(" Note: Since the backend is hosted on Render, the API might experience a cold start delay when accessed for the first time after a period of inactivity.")
st.write(" This means the server might take a few seconds to wake up before responding to requests.")
