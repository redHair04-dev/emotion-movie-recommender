import streamlit as st
import requests
import json
import os
from PIL import Image
import numpy as np
from deepface import DeepFace
import time

# Custom CSS for modern UI
st.markdown("""
    <style>
    /* Main theme colors */
    :root {
        --primary: #6366f1;
        --secondary: #8b5cf6;
        --accent: #ec4899;
        --background: #0f172a;
        --surface: #1e293b;
        --text: #f8fafc;
        --text-secondary: #94a3b8;
    }

    /* Global styles */
    .stApp {
        background: var(--background);
        color: var(--text);
    }

    /* Custom container styles */
    .custom-container {
        background: var(--surface);
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }

    /* Header styles */
    .header {
        text-align: center;
        margin-bottom: 2rem;
    }

    .header h1 {
        font-size: 2.5rem;
        background: linear-gradient(45deg, var(--primary), var(--secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }

    .header p {
        color: var(--text-secondary);
        font-size: 1.1rem;
    }

    /* Upload section styles */
    .upload-section {
        text-align: center;
        padding: 2rem;
        border: 2px dashed var(--primary);
        border-radius: 16px;
        margin: 2rem 0;
        transition: all 0.3s ease;
    }

    .upload-section:hover {
        border-color: var(--secondary);
        background: rgba(99, 102, 241, 0.05);
    }

    /* Movie card styles */
    .movie-card {
        background: var(--surface);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        height: 100%;
    }

    .movie-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }

    .movie-title {
        font-size: 1.25rem;
        color: var(--text);
        margin-bottom: 0.5rem;
    }

    .movie-info {
        color: var(--text-secondary);
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }

    .movie-overview {
        color: var(--text-secondary);
        font-size: 0.9rem;
        margin-bottom: 1rem;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }

    /* Button styles */
    .stButton > button {
        background: linear-gradient(45deg, var(--primary), var(--secondary));
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
        font-size: 0.9rem;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }

    /* Loading animation */
    .loading {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 200px;
    }

    .loading::after {
        content: "";
        width: 40px;
        height: 40px;
        border: 4px solid var(--primary);
        border-top-color: transparent;
        border-radius: 50%;
        animation: loading 1s linear infinite;
    }

    @keyframes loading {
        to {
            transform: rotate(360deg);
        }
    }

    /* Emotion display styles */
    .emotion-display {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(45deg, var(--primary), var(--secondary));
        border-radius: 12px;
        margin: 1rem 0;
    }

    .emotion-text {
        font-size: 1.5rem;
        font-weight: 600;
        color: white;
    }

    /* Sidebar styles */
    .css-1d391kg {
        background: var(--surface);
        padding: 1rem;
    }

    /* File uploader styles */
    .stFileUploader > div {
        border: 2px dashed var(--primary);
        border-radius: 12px;
        padding: 2rem;
    }

    .stFileUploader > div:hover {
        border-color: var(--secondary);
    }

    /* Upload card styles */
    .upload-card {
        background: var(--surface);
        border-radius: 16px;
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
        border: 2px dashed var(--primary);
        transition: all 0.3s ease;
    }

    .upload-card:hover {
        border-color: var(--secondary);
        background: rgba(99, 102, 241, 0.05);
    }

    .upload-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
    }

    .upload-content h3 {
        color: var(--text);
        font-size: 1.5rem;
        margin: 0;
    }

    .upload-content p {
        color: var(--text-secondary);
        font-size: 1rem;
        margin: 0;
    }

    /* Image container styles */
    .image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 1rem 0;
    }

    .uploaded-image {
        max-width: 250px;
        max-height: 250px;
        object-fit: contain;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }

    /* Upload note styles */
    .upload-note {
        color: var(--text-secondary);
        font-size: 0.9rem;
        margin-top: 0.5rem;
        font-style: italic;
    }

    /* Emotion scores styles */
    .emotion-scores {
        background: var(--surface);
        border-radius: 12px;
        padding: 1rem;
        margin: 1rem 0;
    }

    .emotion-scores h4 {
        color: var(--text);
        margin-bottom: 0.5rem;
    }

    .emotion-scores ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .emotion-scores li {
        color: var(--text-secondary);
        padding: 0.25rem 0;
    }

    /* Camera instructions styles */
    .camera-instructions {
        text-align: center;
        margin: 1rem 0;
    }

    .camera-instructions p {
        color: var(--text);
        margin: 0.5rem 0;
    }

    .camera-instructions .note {
        color: var(--text-secondary);
        font-size: 0.9rem;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

# TMDB API Configuration
TMDB_API_KEY = "6f9ce6c776e4d4fce4eab4665a010d4f"  # Your TMDB API key
TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

# Emotion to Genre Mapping
EMOTION_TO_GENRE = {
    "happy": [35, 10751],  # Comedy, Family
    "sad": [18, 10749],    # Drama, Romance
    "angry": [28, 53],     # Action, Thriller
    "fear": [27, 9648],    # Horror, Mystery
    "surprise": [14, 16],  # Fantasy, Animation
    "neutral": [18, 35],   # Drama, Comedy
    "disgust": [27, 53],   # Horror, Thriller
    "excited": [28, 12],   # Action, Adventure
    "peaceful": [18, 10749], # Drama, Romance
    "melancholic": [18, 10749], # Drama, Romance
    "anxious": [53, 27],   # Thriller, Horror
    "nostalgic": [18, 35]  # Drama, Comedy
}

def analyze_emotion(image):
    try:
        # Convert image to numpy array
        img_array = np.array(image)
        
        # Analyze emotion using DeepFace without enforcing face detection
        result = DeepFace.analyze(img_array, actions=['emotion'], enforce_detection=False)
        
        # Get the dominant emotion
        emotions = result[0]['emotion']
        dominant_emotion = max(emotions.items(), key=lambda x: x[1])[0]
        
        # Show confidence scores
        st.markdown("""
            <div class="emotion-scores">
                <h4>Emotion Analysis Results:</h4>
                <ul>
        """, unsafe_allow_html=True)
        
        for emotion, score in emotions.items():
            st.markdown(f"""
                <li>{emotion.capitalize()}: {score:.2f}%</li>
            """, unsafe_allow_html=True)
        
        st.markdown("</ul></div>", unsafe_allow_html=True)
        
        return dominant_emotion
    except Exception as e:
        st.error(f"Error analyzing emotion: {str(e)}")
        return None

def get_movies_by_genre(genre_ids, max_retries=3):
    if not TMDB_API_KEY or TMDB_API_KEY == 'YOUR_TMDB_API_KEY':
        st.error("Please set your TMDB API key in the environment variables or in the code.")
        return []

    for retry in range(max_retries):
        try:
            # Convert genre_ids to string if it's a list
            if isinstance(genre_ids, list):
                genre_ids = ','.join(map(str, genre_ids))
            
            # Make API request
            url = f"{TMDB_BASE_URL}/discover/movie"
            params = {
                'api_key': TMDB_API_KEY,
                'with_genres': genre_ids,
                'sort_by': 'popularity.desc',
                'page': 1
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            movies = data.get('results', [])
            
            if not movies:
                st.warning("No movies found for the selected genre. Trying alternative genres...")
                # Try with a single genre if multiple genres didn't work
                if isinstance(genre_ids, str) and ',' in genre_ids:
                    return get_movies_by_genre(genre_ids.split(',')[0])
                return []
            
            return movies[:10]  # Return top 10 movies
            
        except requests.exceptions.RequestException as e:
            if retry < max_retries - 1:
                time.sleep(1)  # Wait before retrying
                continue
            st.error(f"Error fetching movies: {str(e)}")
            return []

def display_movie_info(movie):
    col1, col2 = st.columns([1, 3])
    
    with col1:
        if movie.get("poster_path"):
            st.image(
                f"{TMDB_IMAGE_BASE_URL}{movie['poster_path']}",
                use_container_width=True,
                width=200
            )
        else:
            st.image(
                "https://via.placeholder.com/200x300?text=No+Poster",
                use_container_width=True,
                width=200
            )
    
    with col2:
        st.markdown(f"""
            <div class="movie-card">
                <h2 class="movie-title">{movie['title']}</h2>
                <p class="movie-info">
                    ⭐ {movie.get('vote_average', 'N/A')}/10 | 
                    📅 {movie.get('release_date', 'N/A')}
                </p>
                <p class="movie-overview">{movie.get('overview', 'No overview available.')}</p>
                <a href="https://www.themoviedb.org/movie/{movie['id']}" target="_blank">
                    <button class="stButton">View Details</button>
                </a>
            </div>
        """, unsafe_allow_html=True)

def main():
    st.markdown("""
        <div class="header">
            <h1>🎬 Emotion-Based Movie Recommender</h1>
            <p>Upload your photo and let AI find the perfect movie for your mood!</p>
        </div>
    """, unsafe_allow_html=True)

    # File uploader with custom styling
    st.markdown("""
        <div class="upload-card">
            <div class="upload-content">
                <h3>📸 Upload Your Photo</h3>
                <p>Let's analyze your emotions and find the perfect movie!</p>
                <p class="upload-note">Please upload a clear photo of your face</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Add tabs for different upload methods
    tab1, tab2 = st.tabs(["📁 Upload Photo", "📸 Take Photo"])
    
    with tab1:
        uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            process_image(image)
    
    with tab2:
        st.markdown("""
            <div class="camera-instructions">
                <p>Click the button below to open your camera</p>
                <p class="note">Make sure your face is clearly visible and well-lit</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Add camera input
        camera_image = st.camera_input("", label_visibility="collapsed")
        if camera_image is not None:
            image = Image.open(camera_image)
            process_image(image)

def process_image(image):
    # Display the uploaded image
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div class="image-container">
                <img src="data:image/png;base64,{0}" class="uploaded-image">
            </div>
        """.format(image_to_base64(image)), unsafe_allow_html=True)

    # Add loading animation
    with st.spinner("Analyzing your emotion..."):
        # Analyze emotion
        emotion = analyze_emotion(image)
        
        if emotion is None:
            return  # Stop execution if no face is detected

        # Display emotion result with animation
        st.markdown(f"""
            <div class="emotion-display">
                <p class="emotion-text">Detected Emotion: {emotion.capitalize()}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Get recommended movies
        genre_ids = EMOTION_TO_GENRE.get(emotion, [18])  # Default to Drama if emotion not found
        movies = get_movies_by_genre(genre_ids)
        
        if movies:
            st.markdown("""
                <div class="header">
                    <h2>🎥 Recommended Movies</h2>
                    <p>Based on your current mood</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Display movies in a grid
            for movie in movies:
                display_movie_info(movie)
        else:
            st.error("No movies found. Please try again later.")

# Add helper function to convert image to base64
def image_to_base64(image):
    import base64
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

if __name__ == "__main__":
    main() 