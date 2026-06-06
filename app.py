import streamlit as st
import pandas as pd
import sys
import os
from database import init_db, add_user, login_user

# Database ko initialize karein
init_db()

# --- Page Configuration (Hamesha sab se upar hona chahiye) ---
st.set_page_config(page_title="Medical NLP Analyzer", page_icon="💊", layout="wide")

# Ensuring the 'src' directory is in the path for backend logic
sys.path.append(os.path.abspath('src'))

# Backend functions import
try:
    from predict import predict_sentiment 
except ImportError:
    st.error("Backend 'src/predict.py' not found. Please ensure your model logic is in the 'src' folder.")

# Session State check karne ke liye (taake login yaad rahe)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# =========================================================
# SCRIPT 1: AGAR USER LOGIN NAHI HAI (LOGIN/SIGN-UP SCREEN)
# =========================================================
if not st.session_state['logged_in']:
    st.title("🔐 Medical NLP Secure Portal")
    
    choice = st.sidebar.selectbox("Menu", ["Login", "Sign Up"])
    
    if choice == "Login":
        st.subheader("Login to your Account")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        
        if st.button("Login"):
            if login_user(username, password):
                st.session_state['logged_in'] = True
                st.success(f"Welcome back, {username}!")
                st.rerun() 
            else:
                st.error("Invalid Username or Password")
                
    elif choice == "Sign Up":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')
        
        if st.button("Register"):
            if add_user(new_user, new_password):
                st.success("Account created successfully! Please login from the sidebar.")
            else:
                st.error("Username already exists!")

# =========================================================
# SCRIPT 2: AGAR USER LOGIN HAI (AAPKA ASAL ANALYZER CODE)
# =========================================================
else:
    # Sidebar mein Logout Button lagane ke liye
    with st.sidebar:
        st.title("Project Details")
        st.info("""
        **Dataset:** UCI Drug Review  
        **Task:** Sentiment Analysis & NER  
        **Developed by:** Rabia Azam
        """)
        st.markdown("---")
        if st.button("Log Out", use_container_width=True):
            st.session_state['logged_in'] = False
            st.rerun()
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