import os
import pickle

# Path set karein
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "sentiment_model.pkl")

# Model aur Vectorizer load karein
with open(MODEL_PATH, "rb") as f:
    model, tfidf = pickle.load(f)

def predict_sentiment(review):
    # Text ko numbers mein badal kar prediction karein
    review_tfidf = tfidf.transform([review])
    prediction = model.predict(review_tfidf)[0]
    return prediction

def extract_entities(text):
    return []