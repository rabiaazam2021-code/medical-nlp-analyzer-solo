from textblob import TextBlob

def predict_sentiment(text):
    try:
        # TextBlob text ka sentiment automatic nikalta hai
        analysis = TextBlob(str(text))
        score = analysis.sentiment.polarity
        
        # Score ke mutabiq Positive, Negative, ya Neutral return karna
        if score > 0.1:
            return "Positive"
        elif score < -0.1:
            return "Negative"
        else:
            return "Neutral"
            
    except Exception as e:
        return f"Error: {str(e)}"