import streamlit as st
import time

# Set page config
st.set_page_config(page_title="About Me", layout="wide")

# Add custom styles
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

    .stApp {
        background-color: #f7f7f7;
        font-family: 'Arial', sans-serif;
    }

    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }

    .typingEffect {
        display: inline-block;
        overflow: hidden;
        white-space: nowrap;
        border-right: 3px solid #333;
        width: 0;
        animation: typing 3s steps(30) 1s 1 normal both;
        font-size: 26px;  /* Reduced font size */
        font-family: 'Poppins', sans-serif;  /* More attractive font */
        font-weight: 600;
        color: #2c3e50;
        margin-top: 30px;
    }

    .normalText {
        font-size: 16px;  /* Reduced paragraph font size */
        color: #444;
        margin-top: 30px;
        line-height: 1.6;
        font-family: 'Arial', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Typing effect for name
st.markdown('<div class="typingEffect">Hi! I\'m MydeenRaahina 👋</div>', unsafe_allow_html=True)

# Delay to allow the typing animation to complete
time.sleep(4)

# Enthusiastic two-line intro with reduced font size
st.markdown(
    """
    <div class="normalText">
        A passionate tech enthusiast crafting smart solutions with AI/ML 🤖, Prompt Engineering ✍️, and Data Engineering 🛠️.<br>
        Skilled in Python Backend & Full Stack Development 💻, and Data Analytics 📊 — turning ideas into impact! 🚀
    </div>
    """,
    unsafe_allow_html=True
)
