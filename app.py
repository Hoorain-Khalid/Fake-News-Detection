import streamlit as st
import joblib
import requests
from bs4 import BeautifulSoup

# Load the trained model
model = joblib.load("fake_news_model.pkl")

# App title
st.title("📰 Fake News Detector")
st.write("Check whether a news article is Fake or Real by entering text or a URL.")

# Option: Text or URL
option = st.radio("Choose Input Type:", ["Enter Text", "Enter URL"])

input_text = ""

# --- If user selects Text input ---
if option == "Enter Text":
    input_text = st.text_area("✍️ Paste News Content Here")

# --- If user selects URL input ---
if option == "Enter URL":
    url = st.text_input("🔗 Paste Article URL Here")

    if url:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract article text
            paragraphs = soup.find_all("p")
            input_text = ' '.join([para.get_text() for para in paragraphs])
            st.success("✅ Article text extracted from URL.")
        except:
            st.error("⚠️ Could not extract article text. Try another URL.")

# Predict Button
if st.button("Detect Fake News"):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter some text or a valid URL.")
    else:
        prediction = model.predict([input_text])[0]
        if prediction == 0:
            st.error("❌ This news is likely *FAKE*.")
        else:
            st.success("✅ This news is likely *REAL*.")

