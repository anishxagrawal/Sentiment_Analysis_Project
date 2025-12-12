---
title: Sentiment Analysis UI
emoji: 🎨
colorFrom: pink
colorTo: purple
sdk: streamlit
sdk_version: 1.32.0
app_file: app.py
pinned: false
---

# 🎨 Sentiment Analysis Web Interface

A beautiful, user-friendly web interface for analyzing text sentiment in real-time, powered by AI.

## 🚀 Live Demo

**Web App:** https://huggingface.co/spaces/anishxagrawal/sentiment_analysis_ui

**Backend API:** https://huggingface.co/spaces/anishxagrawal/sentiment_analysis_api

## ✨ Features

- 🎨 **Beautiful UI**: Clean, modern interface with dark theme
- 🚀 **Real-time Analysis**: Instant sentiment predictions
- 💡 **Quick Examples**: Pre-filled examples for testing
- 📊 **Live Statistics**: View total predictions in real-time
- 🎯 **User-Friendly**: No technical knowledge required
- 📱 **Responsive**: Works on desktop and mobile
- 🌈 **Visual Feedback**: Color-coded results (green for positive, red for negative)
- ⚡ **Fast**: Results in under 1 second

## 🛠️ Tech Stack

- **Frontend Framework**: Streamlit
- **Backend API**: FastAPI (separate service)
- **ML Model**: DistilBERT via API
- **Deployment**: Hugging Face Spaces

## 🎯 How to Use

1. **Visit the app**: https://huggingface.co/spaces/anishxagrawal/sentiment_analysis_ui
2. **Enter text**: Type or paste any text in the input box
3. **Or use examples**: Click one of the quick example buttons
4. **Analyze**: Click the "Analyze Sentiment" button
5. **View results**: See sentiment (positive/negative) and confidence score

## 💡 Example Texts

Try these in the app:

**Positive:**
- "I absolutely love this product! It's amazing and exceeded my expectations!"
- "Best purchase ever! Highly recommend to everyone!"
- "The service was excellent and staff were very helpful!"

**Negative:**
- "This is terrible and very disappointing. Would not recommend."
- "Worst experience ever. Complete waste of money."
- "Poor quality and terrible customer service."

**Mixed:**
- "The product is okay, nothing special but not bad either."
- "Good features but the price is too high."
- "Works as expected but shipping was slow."

## 🏃 Running Locally
```bash
# Clone repository
git clone https://github.com/anishxagrawal/Sentiment_Analysis_Project.git
cd Sentiment_Analysis_Project/ui

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

# Visit http://localhost:8501
```

## 📁 Project Structure
```
ui/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── config.toml       # Streamlit theme configuration
└── README.md             # This file
```

## 🎨 UI Components

### Main Interface
- **Text Input Area**: Large text box for entering content
- **Quick Examples**: Three buttons for instant testing
- **Analyze Button**: Triggers sentiment analysis
- **Results Display**: Color-coded sentiment with confidence

### Sidebar
- **About Section**: App description and model info
- **API Statistics**: Live prediction counter
- **Developer Info**: Author and links
- **API Documentation**: Direct link to API docs

## 🔧 Configuration

The app connects to the FastAPI backend at:
```
https://anishxagrawal-sentiment-analysis-api.hf.space
```

To change the API endpoint, modify the `API_URL` variable in `app.py`:
```python
API_URL = "your-api-url-here"
```

## 🎨 Theme Customization

The app uses a custom dark theme. To modify colors, edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#FF4B4B"        # Accent color
backgroundColor = "#0E1117"      # Main background
secondaryBackgroundColor = "#262730"  # Sidebar background
textColor = "#FAFAFA"           # Text color
```

## 📊 Features Breakdown

| Feature | Description |
|---------|-------------|
| **Input Validation** | Prevents empty submissions |
| **Error Handling** | User-friendly error messages |
| **Loading States** | Spinner during API calls |
| **Example Texts** | Quick-start buttons |
| **Live Stats** | Real-time prediction counter |
| **API Link** | Direct link to documentation |
| **Responsive Design** | Works on all screen sizes |

## 🚨 Error Handling

The app handles various scenarios gracefully:

- **Empty Input**: Warning to enter text
- **API Timeout**: Friendly message about startup time
- **Connection Error**: Clear error message
- **API Validation**: Displays validation errors from backend

## ⚡ Performance

- **Response Time**: < 1 second for predictions
- **First Load**: ~30 seconds (API cold start)
- **Subsequent Requests**: Instant
- **Concurrent Users**: Supports multiple simultaneous users

## 🔮 Future Enhancements

- [ ] History of previous analyses
- [ ] Export results to CSV
- [ ] Bulk text analysis (upload files)
- [ ] Sentiment trends visualization
- [ ] Emotion detection (joy, anger, sadness)
- [ ] Multiple language support
- [ ] Share results functionality
- [ ] Dark/Light theme toggle

## 🐛 Troubleshooting

**App is slow on first use:**
- The API has a ~30 second cold start time
- Subsequent requests are instant

**"Could not connect to API" error:**
- Check if API is running at the backend URL
- Verify your internet connection

**Text not appearing after clicking examples:**
- Refresh the page
- Try typing manually

## 👨‍💻 Author

**Anish Agrawal** - CS Student | Building AI/ML Portfolio

- GitHub: [@anishxagrawal](https://github.com/anishxagrawal)
- Hugging Face: [@anishxagrawal](https://huggingface.co/anishxagrawal)

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Backend powered by [FastAPI](https://fastapi.tiangolo.com/)
- ML model from [Hugging Face](https://huggingface.co/)

## 📝 License

MIT License - See LICENSE file for details

---

**Try it now:** https://huggingface.co/spaces/anishxagrawal/sentiment_analysis_ui

Built with ❤️ using Streamlit and FastAPI
