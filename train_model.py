import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

print("Training process shuru ho raha hai...")

# Manual Medical Data (Testing ke liye)
data = {
    'review': [
        "This medicine is amazing, I feel so much better!",
        "Terrible side effects, I hated this drug.",
        "It worked okay but the recovery was slow.",
        "Excellent results, highly recommend to patients.",
        "Worst experience ever, made me feel very sick.",
        "The doctor prescribed this and it worked like a charm.",
        "I saw no improvement after taking this for a month.",
        "Great medication, very effective for pain relief."
    ],
    'sentiment': ['Positive', 'Negative', 'Negative', 'Positive', 'Negative', 'Positive', 'Negative', 'Positive']
}

df = pd.DataFrame(data)

# Features aur Labels
X = df['review']
y = df['sentiment']

# Vectorization (Text ko numbers mein badalna)
tfidf = TfidfVectorizer(stop_words='english')
X_tfidf = tfidf.fit_transform(X)

# Model Training
model = MultinomialNB()
model.fit(X_tfidf, y)

# Save Model and Vectorizer
if not os.path.exists('models'):
    os.makedirs('models')

# Hum model aur tfidf dono ko save karenge
with open('models/sentiment_model.pkl', 'wb') as f:
    pickle.dump((model, tfidf), f)

print("Mubarak ho! 'models/sentiment_model.pkl' file ban gayi hai.")