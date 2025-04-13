# Emotion-Based Movie Recommender

An AI-powered application that recommends movies based on your current emotional state.

## Features
- Real-time emotion detection from photos
- Camera capture support
- Personalized movie recommendations
- Modern and responsive UI

## Local Development
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run AiMovie/Home.py
   ```

## Deployment Options

### 1. Heroku Deployment
1. Create a Heroku account
2. Install Heroku CLI
3. Login to Heroku:
   ```bash
   heroku login
   ```
4. Create a new Heroku app:
   ```bash
   heroku create your-app-name
   ```
5. Deploy to Heroku:
   ```bash
   git push heroku main
   ```

### 2. Streamlit Cloud Deployment
1. Create a Streamlit Cloud account
2. Connect your GitHub repository
3. Select the main file (AiMovie/Home.py)
4. Deploy

### 3. AWS Deployment
1. Create an EC2 instance
2. Install required dependencies
3. Configure security groups
4. Run the application using:
   ```bash
   streamlit run AiMovie/Home.py
   ```

## Environment Variables
Create a `.env` file with:
```
TMDB_API_KEY=your_api_key
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

## Requirements
- Python 3.8+
- Streamlit
- DeepFace
- Pillow
- NumPy
- Requests

## License
MIT License 