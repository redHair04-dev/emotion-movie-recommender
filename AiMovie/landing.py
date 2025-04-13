import streamlit as st
import streamlit.components.v1 as components

# Custom CSS for modern landing page
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

    /* Hero section */
    .hero {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, var(--surface), var(--background));
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }

    .hero h1 {
        font-size: 3.5em;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, var(--primary), var(--secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero p {
        font-size: 1.2em;
        color: var(--text-secondary);
        margin-bottom: 2rem;
    }

    /* Feature cards */
    .feature-card {
        background: var(--surface);
        border-radius: 20px;
        padding: 30px;
        margin: 20px;
        text-align: center;
        transition: all 0.3s ease;
        animation: fadeIn 1s ease-out;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        border-color: var(--primary);
    }

    .feature-card h3 {
        color: var(--primary);
        margin-bottom: 15px;
        font-size: 1.5em;
    }

    .feature-card p {
        color: var(--text-secondary);
        line-height: 1.6;
    }

    /* Emotion badges */
    .emotion-badge {
        background: linear-gradient(45deg, var(--primary), var(--secondary));
        color: white;
        padding: 8px 20px;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
        margin: 5px;
        transition: all 0.3s ease;
        border: none;
    }

    .emotion-badge:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(99, 102, 241, 0.4);
    }

    /* CTA section */
    .cta-section {
        text-align: center;
        padding: 60px 20px;
        background: var(--surface);
        border-radius: 20px;
        margin: 50px 0;
        animation: fadeIn 1s ease-out;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .cta-button {
        background: linear-gradient(45deg, var(--primary), var(--secondary));
        color: white;
        padding: 15px 30px;
        border-radius: 30px;
        text-decoration: none;
        font-weight: 600;
        display: inline-block;
        margin: 20px 0;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        font-size: 1.2em;
    }

    .cta-button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(99, 102, 241, 0.4);
    }

    /* Section titles */
    .section-title {
        text-align: center;
        margin: 50px 0;
        color: var(--text);
        font-size: 2.5em;
        animation: fadeIn 1s ease-out;
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Stats section */
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 50px 0;
        animation: fadeIn 1s ease-out;
    }

    .stat-card {
        background: var(--surface);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        flex: 1;
        margin: 0 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .stat-number {
        font-size: 2.5em;
        color: var(--primary);
        font-weight: 600;
        margin-bottom: 10px;
    }

    .stat-label {
        color: var(--text-secondary);
        font-size: 1.1em;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    st.markdown("""
        <div class="hero">
            <h1>Welcome to Emotion-Based Movie Recommender</h1>
            <p>Discover movies that perfectly match your current mood through advanced facial expression analysis</p>
        </div>

        <div class="features">
            <h2>How It Works</h2>
            <div class="feature-grid">
                <div class="feature-card">
                    <h3>📸 Upload Your Photo</h3>
                    <p>Take or upload a photo showing your current emotion</p>
                </div>
                <div class="feature-card">
                    <h3>🤖 AI Analysis</h3>
                    <p>Our AI analyzes your emotion from the photo</p>
                </div>
                <div class="feature-card">
                    <h3>🎬 Get Recommendations</h3>
                    <p>Receive personalized movie suggestions based on your mood</p>
                </div>
            </div>
        </div>

        <div class="emotions">
            <h2>Emotions We Detect</h2>
            <div class="emotion-grid">
                <div class="emotion-card">
                    <h4>😊 Happy</h4>
                    <p>Comedy & Family Movies</p>
                </div>
                <div class="emotion-card">
                    <h4>😢 Sad</h4>
                    <p>Drama & Romance</p>
                </div>
                <div class="emotion-card">
                    <h4>😠 Angry</h4>
                    <p>Action & Thriller</p>
                </div>
                <div class="emotion-card">
                    <h4>😨 Fear</h4>
                    <p>Horror & Mystery</p>
                </div>
                <div class="emotion-card">
                    <h4>😲 Surprise</h4>
                    <p>Fantasy & Animation</p>
                </div>
                <div class="emotion-card">
                    <h4>😐 Neutral</h4>
                    <p>Drama & Comedy</p>
                </div>
                <div class="emotion-card">
                    <h4>🤢 Disgust</h4>
                    <p>Dark Comedy & Horror</p>
                </div>
                <div class="emotion-card">
                    <h4>🤗 Excited</h4>
                    <p>Adventure & Action</p>
                </div>
                <div class="emotion-card">
                    <h4>😌 Peaceful</h4>
                    <p>Documentary & Family</p>
                </div>
                <div class="emotion-card">
                    <h4>😔 Melancholic</h4>
                    <p>Art House & Drama</p>
                </div>
                <div class="emotion-card">
                    <h4>😰 Anxious</h4>
                    <p>Suspense & Mystery</p>
                </div>
                <div class="emotion-card">
                    <h4>🌟 Nostalgic</h4>
                    <p>Classics & Romance</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Add custom CSS
    st.markdown("""
        <style>
        /* Hero section */
        .hero {
            text-align: center;
            padding: 4rem 2rem;
            background: linear-gradient(135deg, var(--surface), var(--background));
            border-radius: 20px;
            margin: 2rem 0;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }

        .hero h1 {
            font-size: 3.5em;
            margin-bottom: 1rem;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero p {
            font-size: 1.2em;
            color: var(--text-secondary);
            margin-bottom: 2rem;
        }

        /* Features section */
        .features {
            padding: 4rem 2rem;
            text-align: center;
        }

        .features h2 {
            font-size: 2.5em;
            margin-bottom: 3rem;
            color: var(--text);
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .feature-card {
            background: var(--surface);
            padding: 2rem;
            border-radius: 15px;
            transition: transform 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-5px);
        }

        .feature-card h3 {
            color: var(--text);
            margin-bottom: 1rem;
        }

        .feature-card p {
            color: var(--text-secondary);
        }

        /* Emotions section */
        .emotions {
            padding: 4rem 2rem;
            text-align: center;
        }

        .emotions h2 {
            font-size: 2.5em;
            margin-bottom: 3rem;
            color: var(--text);
        }

        .emotion-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .emotion-card {
            background: var(--surface);
            padding: 2rem;
            border-radius: 15px;
            transition: transform 0.3s ease;
        }

        .emotion-card:hover {
            transform: translateY(-5px);
        }

        .emotion-card h4 {
            color: var(--text);
            margin-bottom: 0.5rem;
        }

        .emotion-card p {
            color: var(--text-secondary);
            font-size: 0.9rem;
        }
        </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 