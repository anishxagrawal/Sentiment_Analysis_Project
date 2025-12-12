---
title: Sentiment Analysis API
emoji: 🎭
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
---

# 🎭 Sentiment Analysis API

A production-ready REST API for real-time sentiment analysis using DistilBERT transformer model.

## 🚀 Live Demo

**API Endpoint:** https://anishxagrawal-sentiment-analysis-api.hf.space

**Interactive Docs:** https://anishxagrawal-sentiment-analysis-api.hf.space/docs

**Web Interface:** https://huggingface.co/spaces/anishxagrawal/sentiment_analysis_ui

## ✨ Features

- 🤖 **ML-Powered**: Uses DistilBERT transformer model fine-tuned on SST-2
- ⚡ **Fast API**: Built with FastAPI for high performance (~50ms per request)
- 📊 **Request Tracking**: Monitor usage with `/stats` endpoint
- ✅ **Input Validation**: Automatic error handling and validation
- 📚 **Auto Documentation**: Interactive Swagger UI at `/docs`
- 🐳 **Dockerized**: Containerized for easy deployment
- 🔒 **Error Handling**: Comprehensive error messages

## 🛠️ Tech Stack

- **Framework**: FastAPI 0.124.2
- **ML Library**: Hugging Face Transformers 4.57.3
- **Model**: distilbert-base-uncased-finetuned-sst-2-english
- **Runtime**: Python 3.11
- **Deployment**: Hugging Face Spaces (Docker)

## 📡 API Endpoints

### GET `/`
Welcome message with available endpoints.

**Response:**
```json
{
  "message": "Welcome to Sentiment API",
  "endpoints": {
    "docs": "/docs",
    "predict": "/predict"
  }
}
```

### POST `/predict`
Analyze sentiment of input text.

**Request Body:**
```json
{
  "text": "I love this product!"
}
```

**Response:**
```json
{
  "text": "I love this product!",
  "sentiment": "POSITIVE",
  "confidence": 0.9998
}
```

**Validation Rules:**
- Text cannot be empty
- Text must be at least 3 characters
- Leading/trailing whitespace is automatically trimmed

**Error Response:**
```json
{
  "error": "Text cannot be empty"
}
```

### GET `/stats`
View total number of predictions made.

**Response:**
```json
{
  "total_predictions": 42
}
```

### GET `/docs`
Interactive API documentation (Swagger UI)

## 💡 Usage Examples

### cURL
```bash
curl -X POST "https://anishxagrawal-sentiment-analysis-api.hf.space/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "This is amazing!"}'
```

### Python
```python
import requests

url = "https://anishxagrawal-sentiment-analysis-api.hf.space/predict"
payload = {"text": "I absolutely love this!"}

response = requests.post(url, json=payload)
result = response.json()

print(f"Sentiment: {result['sentiment']}")
print(f"Confidence: {result['confidence']:.2%}")
```

### JavaScript
```javascript
fetch('https://anishxagrawal-sentiment-analysis-api.hf.space/predict', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ text: 'This is great!' })
})
.then(res => res.json())
.then(data => console.log(data));
```

## 🏃 Running Locally
```bash
# Clone repository
git clone https://github.com/anishxagrawal/Sentiment_Analysis_Project.git
cd Sentiment_Analysis_Project/api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Visit http://localhost:8000/docs
```

## 🐳 Docker Deployment
```bash
# Build image
docker build -t sentiment-api .

# Run container
docker run -p 7860:7860 sentiment-api

# Visit http://localhost:7860/docs
```

## 📊 Model Information

- **Model**: distilbert-base-uncased-finetuned-sst-2-english
- **Source**: Hugging Face Model Hub
- **Training Data**: Stanford Sentiment Treebank (SST-2)
- **Accuracy**: ~91% on SST-2 test set
- **Classes**: POSITIVE, NEGATIVE
- **Model Size**: 268MB

## 🔧 Configuration

The API runs on port 7860 by default (Hugging Face Spaces standard).

To change the port locally:
```bash
uvicorn main:app --port YOUR_PORT
```

## 🚨 Error Handling

The API handles various error cases:

| Error | Status Code | Response |
|-------|-------------|----------|
| Empty text | 200 | `{"error": "Text cannot be empty"}` |
| Text too short | 200 | `{"error": "Text must be at least 3 characters long"}` |
| Server error | 500 | Internal server error message |

## 📈 Performance

- **Latency**: ~50ms per prediction (CPU)
- **Throughput**: ~20 requests/second
- **Memory**: ~500MB RAM usage
- **Cold Start**: ~30 seconds (first request after idle)

## 🔮 Future Improvements

- [ ] Add batch prediction endpoint
- [ ] Implement response caching
- [ ] Add neutral sentiment category
- [ ] Support multiple languages
- [ ] Rate limiting
- [ ] API key authentication
- [ ] Async processing for batch requests

## 👨‍💻 Author

**Anish Agrawal** - CS Student | AI/ML Enthusiast

- GitHub: [@anishxagrawal](https://github.com/anishxagrawal)
- Hugging Face: [@anishxagrawal](https://huggingface.co/anishxagrawal)

## 📝 License

MIT License - See LICENSE file for details

---

Built with ❤️ using FastAPI and Hugging Face Transformers
