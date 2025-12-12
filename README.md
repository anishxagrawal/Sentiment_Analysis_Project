# 🎭 Sentiment Analysis Project

A complete end-to-end ML application featuring a FastAPI backend and Streamlit frontend for real-time sentiment analysis using DistilBERT.

## 🚀 Live Demo

- **🖥️ Web Interface:** https://huggingface.co/spaces/anishxagrawal/sentiment_analysis_ui
- **⚙️ API Backend:** https://huggingface.co/spaces/anishxagrawal/sentiment_analysis_api
- **📚 API Documentation:** https://anishxagrawal-sentiment-analysis-api.hf.space/docs

## 📁 Project Structure
```
Sentiment_Analysis_Project/
├── api/                    # FastAPI backend service
│   ├── main.py            # API endpoints and ML model
│   ├── Dockerfile         # Container configuration
│   ├── requirements.txt   # Python dependencies
│   └── README.md          # API documentation
│
├── ui/                     # Streamlit web interface
│   ├── app.py             # Streamlit application
│   ├── requirements.txt   # UI dependencies
│   ├── .streamlit/        # Streamlit configuration
│   └── README.md          # UI documentation
│
└── README.md              # This file
```

## ✨ Features

### API Backend
- 🤖 **ML-Powered**: DistilBERT transformer model for sentiment analysis
- ⚡ **FastAPI**: High-performance REST API
- 📊 **Request Tracking**: Monitor usage statistics
- ✅ **Input Validation**: Automatic error handling
- 📚 **Auto Documentation**: Interactive Swagger UI

### Web Interface
- 🎨 **Beautiful UI**: Clean, modern Streamlit interface
- 🚀 **Real-time Analysis**: Instant sentiment predictions
- 💡 **Example Texts**: Quick-start with pre-filled examples
- 📈 **Live Stats**: View total predictions in real-time
- 🎯 **User-Friendly**: No technical knowledge required

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **ML Model** | DistilBERT (Hugging Face Transformers) |
| **Backend** | FastAPI, Python 3.11 |
| **Frontend** | Streamlit |
| **Deployment** | Hugging Face Spaces (Docker + Streamlit SDK) |
| **Version Control** | Git, GitHub |

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message and endpoint info |
| POST | `/predict` | Analyze sentiment of input text |
| GET | `/stats` | View total predictions made |
| GET | `/docs` | Interactive API documentation |

## 💡 Usage Examples

### Using the Web Interface
1. Visit https://huggingface.co/spaces/anishxagrawal/sentiment_analysis_ui
2. Enter text or click an example button
3. Click "Analyze Sentiment"
4. View results with confidence scores

### Using the API

**Request:**
```bash
curl -X POST "https://anishxagrawal-sentiment-analysis-api.hf.space/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this product!"}'
```

**Response:**
```json
{
  "text": "I love this product!",
  "sentiment": "POSITIVE",
  "confidence": 0.9998
}
```

**Python Example:**
```python
import requests

response = requests.post(
    "https://anishxagrawal-sentiment-analysis-api.hf.space/predict",
    json={"text": "I love this product!"}
)

result = response.json()
print(f"Sentiment: {result['sentiment']}")
print(f"Confidence: {result['confidence']:.2%}")
```

## 🏃 Running Locally

### API Backend
```bash
cd api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn main:app --reload

# Visit http://localhost:8000/docs
```

### Streamlit UI
```bash
cd ui

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

# Visit http://localhost:8501
```

## 🚀 Deployment

Both components are deployed on **Hugging Face Spaces**:

- **API**: Docker SDK for flexible FastAPI deployment
- **UI**: Streamlit SDK for easy frontend hosting

### Deploy Your Own

1. Fork this repository
2. Create new Spaces on Hugging Face
3. Connect your GitHub repository
4. Push changes - auto-deploys!

See individual README files in `/api` and `/ui` for detailed deployment instructions.

## 📊 Model Performance

- **Model**: distilbert-base-uncased-finetuned-sst-2-english
- **Accuracy**: ~91% on SST-2 dataset
- **Speed**: ~50ms per prediction
- **Size**: 268MB (optimized for CPU)

## 🔮 Future Enhancements

- [ ] Add batch prediction endpoint
- [ ] Implement caching for common phrases
- [ ] Support multiple languages
- [ ] Add neutral sentiment category
- [ ] Emotion detection (joy, anger, sadness, etc.)
- [ ] Export predictions to CSV
- [ ] User authentication
- [ ] Rate limiting for API

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Anish Agrawal**
- GitHub: [@anishxagrawal](https://github.com/anishxagrawal)
- Hugging Face: [@anishxagrawal](https://huggingface.co/anishxagrawal)

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for the DistilBERT model and hosting
- [FastAPI](https://fastapi.tiangolo.com/) for the amazing web framework
- [Streamlit](https://streamlit.io/) for the beautiful UI framework

---

**⭐ If you found this project helpful, please consider giving it a star!**

Built as part of AI/ML internship preparation portfolio.
