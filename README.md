# **🧠 Personality Type Predictor API**

## 🚀 **Overview**
This API predicts a user's MBTI personality type based on text input. The solution uses a **RandomForestClassifier** with an accuracy of **0.68** and is built with **FastAPI**. The application is containerized with Docker and runs on port **8000**.

---

## ⚙️ **API Endpoints**

### 1. **Health Check**
- **Endpoint:** `GET /`
- **Description:** Check if the API is running.
- **Response:**
  ```json
  {
    "message": "API is running",
    "status": 200
  }
  ```

### 2. **Prediction**
- **Endpoint:** `POST /predict`
- **Description:** Predicts the MBTI personality type based on the input text.
- **Request Body:**
  ```json
  {
    "text": "I love deep conversations and thinking about abstract ideas."
  }
  ```

- **Response:**
  ```json
  {
    "mbti_type": "INFJ",
    "confidence": 0.87
  }
  ```

---

## 🛠️ **Installation and Usage**

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/SananSuleymanov/mbti.git
cd mbti
```

### 2️⃣ **Build the Docker Image**
```bash
docker build -t mbti-fastapi-app .
```

### 3️⃣ **Run the Docker Container**
```bash
docker run -d -p 8000:8000 mbti-fastapi-app
```

### 4️⃣ **Access the API**
- Open a browser or use a tool like **Postman** to test the endpoints.
- The API documentation is available at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧠 **Model Training**
The model was trained using a **RandomForestClassifier** on the **MBTI dataset**.
- **Training Notebook:** `model-training.ipynb`
- **Model Accuracy:** `0.68`

---

## 📦 **Project Structure**
```
.
├── model-training.ipynb        # notebook for training the model
├── main.py                  # FastAPI application code
├── Dockerfile               # Docker configuration file
├── requirements.txt         # Python dependencies
├── mbti_classifier.joblib   # Trained RandomForest model
├── tfidf_vectorizer.joblib  # TF-IDF vectorizer
├── label_encoder.joblib     # Label encoder for personality types
└── README.md                # Project documentation
```

---

## 🧪 **Testing the API**

### **Health Check**
```bash
curl -X GET http://localhost:8000/
```
Expected Output:
```json
{
  "message": "API is running",
  "status": 200
}
```

### **Prediction**
```bash
curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{"text": "I love exploring abstract ideas and discussing possibilities."}'
```
Expected Output:
```json
{
  "mbti_type": "INFJ",
  "confidence": 0.87
}
```

---

## 🌐 **API Documentation**
The interactive API documentation is available via:
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🛠️ **CI/CD Integration**
The project uses **GitHub Actions** for CI/CD:
- **Run tests** to validate API functionality.
- **Build Docker image** automatically upon successful test runs.

---
