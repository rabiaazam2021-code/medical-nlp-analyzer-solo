# 💊 Medical NLP Analyzer - Secure AI Portal

Medical NLP Analyzer is a secure web application built using **Python** and **Streamlit**. It allows healthcare professionals, researchers, or developers to analyze patient reviews, clinical notes, and drug feedback in real-time. The application evaluates the sentiment of the text and extracts critical medical entities (such as Drugs, Treatments, Diseases, and Symptoms) into a clean, structured table.

---

## 🚀 Key Features

* **🔐 Secure User Authentication:** Integrated Login and Sign-Up management system powered by an SQLite database (`users.db`) using secure SHA-256 password hashing.
* **📊 AI Sentiment Analysis:** Real-time prediction of patient feedback (Positive, Negative, Neutral) with responsive UI micro-interactions (Balloons effect on positive results).
* **🔍 Named Entity Recognition (NER):** Automated extraction and classification of key medical terms (Drugs, Treatments, Diseases, and Symptoms) displayed in an interactive table.
* **🎨 Premium UI/UX:** Responsive sidebar for project telemetry and account management, wide-screen responsive layout, and beautiful styling.
* **🛠️ Production Ready:** Clean code structure following standard directory layouts, easy to expand or connect with larger medical LLMs.

---

## 📁 Project Structure

```text
medical-nlp-analyzer2/
│
├── app.py                 # Main entry point for the Streamlit web interface
├── main.py                # System entry controller
├── database.py            # SQLite database logic and SHA-256 secure authentication
├── requirements.txt       # Python dependency tracking file
├── users.db               # Local SQLite database file (auto-generated)
└── src/
    └── predict.py         # AI Sentiment Analysis core model logic
    Installation & Setup Guide
Follow these simple steps to set up and run the project on your local machine:

1. Prerequisites
Make sure you have Python 3.8 or higher installed on your system. You can check your version by running:
python --version
2. Clone or Extract the Project
Extract the downloaded zip file into your preferred workspace directory.

3. Install Dependencies
Open your terminal/command prompt inside the project folder (medical-nlp-analyzer2) and run the following command to install the required libraries:
pip install -r requirements.txt
4. Run the Application
Start the Streamlit server locally by executing:
streamlit run app.py
Once executed, a local browser window will automatically open at http://localhost:8501 showing the secure portal
📦 Required Libraries (Dependencies)
The project relies on the following open-source libraries:

streamlit - For building the interactive web dashboard.

pandas - For managing entity extraction tables.

textblob - For computing underlying sentiment metrics.

👤 Developed By
Developer: Rabia Azam

Version: 1.1.0 (Production Ready)

License: Independent Commercial Use