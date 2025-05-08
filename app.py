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
        border-right: 2px solid #333;
        width: 0;
        animation: typing 3s steps(30) 1s 1 normal both;
        font-size: 20px;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        color: #2c3e50;
        margin-top: 30px;
    }

    .normalText {
        font-size: 18px;
        color: #444;
        margin-top: 30px;
        line-height: 1.6;
        font-family: 'Arial', sans-serif;
    }

    /* Styling for the compact expander with hover effect */
    .stExpander {
        background-color: #2c3e50;
        color: white;
        font-weight: bold;
        font-size: 16px;
        border-radius: 8px;
        padding: 0.5em 1em;  /* Reduced padding for compact size */
        margin-top: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease;  /* Smooth transition for hover effect */
    }

    /* Hover effect */
    .stExpander:hover {
        background-color: #34495e;  /* Darker shade on hover */
    }

    .stExpander div {
        font-size: 16px;
        font-weight: bold;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Typing effect for name
st.markdown('<div class="typingEffect">Hi! I\'m Mydeen Raahina 👋</div>', unsafe_allow_html=True)

# Delay to allow the typing animation to complete
time.sleep(4)

# Two-line intro
st.markdown(
    """
    <div class="normalText">
        A passionate tech enthusiast crafting smart solutions with AI/ML 🤖, Prompt Engineering ✍️, and Data Engineering 🛠️.<br>
        Skilled in Python Backend & Full Stack Development 💻, and Data Analytics 📊 — turning ideas into impact! 🚀
    </div>
    """,
    unsafe_allow_html=True
)

# Button-like expander for more information
with st.expander("Know More About Me", expanded=False):
    st.markdown(
        """
        <div class="normalText">
            🌟 I'm currently pursuing Computer Science, exploring Data Science and AI.<br>
            🧠 Love building AI-powered apps and solving real-world problems with tech.<br>
            📫 You can connect with me on <a href='https://www.linkedin.com' target='_blank'>LinkedIn</a> or check out my projects on <a href='https://github.com' target='_blank'>GitHub</a>!
        </div>
        """,
        unsafe_allow_html=True
    )
