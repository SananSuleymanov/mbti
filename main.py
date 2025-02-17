from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import re


# Load model, vectorizer, and label encoder for inference
model = joblib.load('mbti_classifier.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')
label_encoder = joblib.load('label_encoder.joblib')

# Initialize FastAPI app
app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "API is running", "status": 200}

@app.post("/predict")
def read_root(input: TextInput):
    try: 
        cl_text = clean_text(input.text)
        features = vectorizer.transform([cl_text])

        probabilities = model.predict_proba(features)[0]
        prediction = model.predict(features)[0]

        mbti_type = label_encoder.inverse_transform([prediction])[0]
        confidence = max(probabilities)
        return {"mbti_type": mbti_type, "confidence": round(confidence, 2)}
    except Exception as e:
            return {"error": str(e)}


def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text) # removes URL 
    text = re.sub(r'[^a-z ]', '', text)  #removes nonalphabetic characters
    return text