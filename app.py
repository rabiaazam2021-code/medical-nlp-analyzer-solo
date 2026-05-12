import streamlit as st
import pandas as pd
import sys
import os

# Ensuring the 'src' directory is in the path for backend logic
sys.path.append(os.path.abspath('src'))

# Backend functions import
try:
    from predict import predict_sentiment 
except ImportError:
    # Adding a more helpful error for solo setup
    st.error("Backend 'src/predict.py' not found. Please ensure your model logic is in the 'src' folder.")

# --- Page Configuration ---
st.set_page_config(page_title="Medical NLP Analyzer", page_icon="💊", layout="wide")

# --- Sidebar ---
with st.sidebar:
    st.title("Project Details")
    st.info("""
    **Dataset:** UCI Drug Review  
    **Task:** Sentiment Analysis & NER  
    **Developed by:** Rabia Azam
    """)
    st.markdown("---")
    st.write("v1.0.0 | Independent Project")

# --- Main UI ---
st.title("💊 Medical NLP Analyzer")
st.markdown("An AI-driven tool to analyze patient feedback and extract medical insights.")

# Input Section
st.subheader("Patient Feedback Analysis")
user_input = st.text_area(
    "Enter review text here:", 
    placeholder="e.g., 'The treatment was effective, but I felt slightly dizzy...'", 
    height=150
)

# Analysis Logic
if st.button("Run AI Analysis"):
    if user_input:
        col1, col2 = st.columns(2)
        
        with st.spinner('AI is processing the text...'):
            # 1. Sentiment Analysis
            try:
                sentiment_result = predict_sentiment(user_input)
                
                with col1:
                    st.markdown("### 📊 Sentiment Result")
                    if "positive" in sentiment_result.lower():
                        st.success(f"Outcome: {sentiment_result}")
                    elif "negative" in sentiment_result.lower():
                        st.error(f"Outcome: {sentiment_result}")
                    else:
                        st.warning(f"Outcome: {sentiment_result}")
            except Exception as e:
                st.error(f"Prediction Error: {e}")

            with col2:
                st.markdown("### 🔍 Medical Entities")
                # Placeholder for Entity Extraction
                st.info("Extracting drug names and medical conditions...")
                st.write("Entity extraction module is active.")
                
        st.divider()
        st.balloons()
    else:
        st.warning("Action Required: Please enter some text to analyze.")

# --- Footer ---
st.markdown("<br><hr><center>Developed by Rabia Azam</center>", unsafe_allow_html=True)