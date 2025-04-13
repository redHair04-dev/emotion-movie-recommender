import streamlit as st
st.set_page_config(
    page_title="Emotion-Based Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

import app
import landing

# Custom CSS for modern navigation
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

    /* CTA Button */
    .stButton > button {
        display: inline-block;
        padding: 1rem 2rem;
        background: linear-gradient(45deg, var(--primary), var(--secondary));
        color: white;
        text-decoration: none;
        border-radius: 50px;
        font-weight: bold;
        transition: transform 0.3s ease;
        border: none;
        cursor: pointer;
        width: auto;
        margin: 0 auto;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
    }

    /* Back Button */
    .back-button {
        position: fixed;
        top: 20px;
        left: 20px;
        z-index: 1000;
    }

    .back-button > button {
        background: var(--surface);
        color: var(--text);
        border: 1px solid var(--primary);
        padding: 0.5rem 1rem;
        border-radius: 25px;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .back-button > button:hover {
        background: var(--primary);
        color: white;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        margin-top: 4rem;
        color: var(--text-secondary);
        font-size: 0.9em;
    }

    /* Loading spinner */
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
    </style>
""", unsafe_allow_html=True)

def main():
    # Get the current page from URL parameters
    page = st.query_params.get("page", "landing")

    # Back button for app page
    if page == "app":
        st.markdown('<div class="back-button">', unsafe_allow_html=True)
        if st.button("← Back to Home", key="back_button"):
            st.query_params["page"] = "landing"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # Render the appropriate page
    if page == "app":
        app.main()
    else:
        # Hero section
        st.markdown("""
            <div class="hero">
                <h1>Emotion-Based Movie Recommender</h1>
                <p>Discover movies that match your mood through facial expression analysis</p>
            </div>
        """, unsafe_allow_html=True)

        # CTA Button
        if st.button("Start Your Movie Journey", key="cta_button"):
            st.query_params["page"] = "app"
            st.rerun()

        # Landing page content
        landing.main()

    # Footer
    st.markdown("""
        <div class="footer">
            <p>© 2024 Emotion-Based Movie Recommender | Made with ❤️ using Streamlit</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 