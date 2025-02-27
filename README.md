This is a sentiment analysis system designed to classify sentences into different sentiment categories.  
The system is built by scraping sentences from the web, manually annotating them, and training a machine learning model on the labeled data.

Accessing the System

    API Endpoint: The sentiment analysis model is accessible through a FastAPI-based REST API.
    Web Interface: A Streamlit-based UI allows for interactive sentiment predictions.
access the [api](https://sentiment-api-uf2f.onrender.com/docs) or [web](https://sentiment-analysis-s.streamlit.app) version

 Note: Since the backend is hosted on Render, the API might experience a cold start delay when accessed for the first time after a period of inactivity.   
 This means the server might take a few seconds to wake up before responding to requests.