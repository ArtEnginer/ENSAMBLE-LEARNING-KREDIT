# Deployment Guide for Kredit Macet Prediction App

## Prerequisites
- Python 3.9+
- pip or conda package manager
- Git (optional)

## Local Development Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
streamlit run streamlit_app.py
```

### 3. Access the Application
Open your browser and navigate to: http://localhost:8501

## Docker Deployment

### 1. Build Docker Image
```bash
docker build -t kredit-macet-app .
```

### 2. Run Docker Container
```bash
docker run -p 8501:8501 kredit-macet-app
```

## Cloud Deployment Options

### Streamlit Cloud
1. Push code to GitHub repository
2. Connect to Streamlit Cloud
3. Deploy directly from repository

### Heroku
1. Create Procfile: `web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0`
2. Deploy using Heroku CLI or GitHub integration

### AWS/GCP/Azure
Use container services with the provided Dockerfile

## Model Information
- **Model Type**: Random Forest
- **Training Date**: 2025-10-02T22:30:07.091522
- **Performance**:
  - F1-Score: 0.8399
  - Accuracy: 0.8400
  - AUC Score: 0.9606

## Configuration
- Model files are automatically loaded from the model_deployment directory
- No additional configuration required for basic usage

## Support
For technical support or questions about the model, please refer to the notebook documentation.

Generated on: 2025-10-02 22:32:20
