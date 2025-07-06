# -*- coding: utf-8 -*-

import os

print("models directory exists:", os.path.exists("Fake_News_Detection.ipynb"))
print("Contents of models/:", os.listdir('folder path'))

# app.py

import streamlit as st
import joblib
import re
import string

#model = joblib.load("fake_news_model.pkl")
#vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Load model and vectorizer
model = joblib.load("models/fake_news_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Text cleaning
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

# Streamlit UI
st.title("📰 Fake News Detector")
st.write("Enter a news article below to check whether it's Fake or Real.")

user_input = st.text_area("News content:")

if st.button("Predict"):
    cleaned = clean_text(user_input)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]

    if prediction == 1:
        st.error("🚨 This news is **FAKE**.")
    else:
        st.success("✅ This news is **REAL**.")