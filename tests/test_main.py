import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running", "status": 200}

def test_predict_valid_input():
    response = client.post("/predict", json={"text": "I love abstract ideas."})
    assert response.status_code == 200
    assert "mbti_type" in response.json()
    assert "confidence" in response.json()

def test_predict_empty_input():
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 200
    assert "mbti_type" in response.json()
    assert "confidence" in response.json()