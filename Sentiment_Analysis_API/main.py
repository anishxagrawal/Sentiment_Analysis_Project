#trigger comment
# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# TODO: Create FastAPI app instance
app = FastAPI()

# TODO: Load sentiment analysis pipeline
sentiment_classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
request_count = 0

# Hint: pipeline("sentiment-analysis")

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(input: TextInput):
    # TODO: Get prediction from classifier
    # TODO: Return result as JSON

    global request_count
    request_count += 1

    text = input.text.strip()

    if(len(text) == 0):
        return {
            "error": "Text cannot be empty"
        } 
    
    if(len(text) < 3):
        return {
            "error": "Enter a larger text"
        }
  
    prediction = sentiment_classifier(text)

    response = {
    "text": text,
    "sentiment": prediction[0]["label"],
    "confidence": prediction[0]["score"]
    }

    return response

# TODO: Add a welcome endpoint at "/"
@app.get("/")
def home():
    return {"message": "Welcome to Sentiment API"}

@app.get("/stats")
def get_stats():
    return {
        "total_predictions": request_count
    }