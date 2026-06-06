import streamlit as st
import pandas as pd
import os
from database import init_db, add_user, login_user

# Database ko initialize karein
init_db()

# --- Page Configuration ---
st.set_page_config(page_title="Medical NLP Analyzer", page_icon="💊", layout="wide")

# Backend functions direct import
try:
    from src.predict import predict_sentiment 
except ImportError:
    st.error("Backend 'src/predict.py' not found. Please ensure your model logic is in the 'src' folder.")

# --- MEDICAL ENTITY EXTRACTION LOGIC ---
def extract_medical_entities(text):
    # Common medical keywords dictionaries for matching
    diseases_keywords = [
        "asthma", "migraine", "headache", "back pain", "pain", "dizzy", "dizziness", 
        "nausea", "nauseous", "blood pressure", "hypertension", "depression", 
        "anxiety", "insomnia", "cough", "fever", "flu", "allergy", "diabetes"
    ]
    drugs_keywords = [
        "medication", "medicine", "drug", "pill", "dose", "treatment", "aspirin", 
        "ibuprofen", "paracetamol", "albuterol", "metformin", "xanax", "lipitor"
    ]
    
    found_entities = []
    text_lower = text.lower()
    
    # Extract Diseases
    for disease in diseases_keywords:
        if disease in text_lower:
            # Capitalize first letters for clean look
            found_entities.append({"Entity": disease.title(), "Type": "Disease / Symptom"})
            
    # Extract Drugs
    for drug in drugs_keywords:
        if drug in text_lower:
            found_entities.append({"Entity": drug.title(), "Type": "Drug / Treatment"})
            
    return found_entities

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
                st.session_state['username'] = username
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
    # Sidebar mein Details
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
        st.write("v1.1.0 | Feature Active")

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

                # 2. Real Medical Entity Extraction (Active Feature)
                with col2:
                    st.markdown("### 🔍 Medical Entities Extracted")
                    entities = extract_medical_entities(user_input)
                    
                    if entities:
                        # Convert list to pandas DataFrame for beautiful table display
                        df_entities = pd.DataFrame(entities)
                        st.dataframe(df_entities, use_container_width=True, hide_index=True)
                    else:
                        st.info("No specific medical entities (Drugs/Diseases) detected in the text.")
                    
            st.divider()
            st.balloons()
        else:
            st.warning("Action Required: Please enter some text to analyze.")

    # --- Footer ---
    st.markdown("<br><hr><center>Developed by Rabia Azam</center>", unsafe_allow_html=True)