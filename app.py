import streamlit as st
import time

st.set_page_config(page_title="Mydeen Raahina Portfolio", layout="wide")

# Elegant Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;700&display=swap');

body, .stApp {
    background-color: #f4f6f9;
    font-family: 'Inter', sans-serif;
    color: #212529;
    padding: 0;
    margin: 0;
}

.heading {
    font-size: 32px;
    font-weight: 700;
    color: #004080;
    margin-top: 30px;
    margin-bottom: 10px;
    animation: fadeInDown 1s ease-in-out;
    text-align: left;
    padding-left: 20px;
}

.typingEffect {
    display: block;
    overflow: hidden;
    white-space: nowrap;
    border-right: 3px solid #004080;
    width: 0;
    animation: typing 3s steps(40) 1s 1 normal both;
    font-size: 18px;
    font-weight: 500;
    color: #004080;
    text-align: left;
    padding-left: 20px;
    margin-bottom: 30px;
}

.section {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 12px;
    border: 1px solid #dee2e6;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    animation: fadeIn 1s ease-in-out;
    margin-bottom: 25px;
}

.stExpander > summary {
    font-size: 20px;
    font-weight: 600;
    color: #004080;
    transition: color 0.3s ease;
}

.stExpander > summary:hover {
    color: #0077cc;
    cursor: pointer;
}

a {
    color: #004080;
    text-decoration: none;
    font-weight: 600;
}

a:hover {
    text-decoration: underline;
    color: #0077cc;
}

.stButton > button {
    background-color: #004080;
    color: white;
    border-radius: 8px;
    font-weight: bold;
    border: none;
    padding: 10px 24px;
    transition: background-color 0.3s ease;
}

.stButton > button:hover {
    background-color: #002b5c;
}

.stTextInput input, .stTextArea textarea {
    background-color: #f1f3f5;
    border-radius: 8px;
    border: 1px solid #ced4da;
    padding: 10px;
    font-size: 16px;
}

.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: #004080;
    outline: none;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

@keyframes fadeInDown {
    from {opacity: 0; transform: translateY(-30px);}
    to {opacity: 1; transform: translateY(0);}
}

@keyframes typing {
    from { width: 0; }
    to { width: 100%; }
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="heading">Hi! I\'m Mydeen Raahina</div>', unsafe_allow_html=True)

# Typing effect intro
st.markdown('<div class="typingEffect">🎯 Data-driven, AI-focused, and design-conscious — I build intelligent apps that solve real-world problems using machine learning, prompt engineering, and beautiful code.</div>', unsafe_allow_html=True)

time.sleep(1.5)

# Know More Section
with st.expander("📖 Know More About Me"):
    st.markdown("""
    <div class="section">
        🎓 Computer Science graduate passionate about building smart AI-powered solutions.<br>
        💼 Skilled in prompt engineering, backend data workflows, and real-time AI integrations.<br>
        🔗 Connect with me on <a href="https://linkedin.com" target="_blank">LinkedIn</a> or check my code on <a href="https://github.com" target="_blank">GitHub</a>.
    </div>
    """, unsafe_allow_html=True)

time.sleep(1.5)

# Experience Section
with st.expander("🧠 Experience"):
    st.markdown("""
    <div class="section">
        <strong>AI/ML Engineer — Plattr Tech Studio</strong><br>
        • Built prompt pipelines for Tax Fixxer to auto-suggest tax-saving strategies using OpenAI & LLaMA.<br>
        • Led scraping and backend data ingestion for Wim Card using Playwright.<br><br>

        <strong>Data Scientist Intern — Plattr Tech Studio</strong><br>
        • OCR + ML classification for Tamil/English ads (Ad Classification Project).<br>
        • Vision-based motion detection AI game inspired by Talking Tom (Visionary Project).
    </div>
    """, unsafe_allow_html=True)

time.sleep(1.5)

# Contact Section
with st.expander("📬 Contact Me"):
    st.markdown('<div class="section">Want to collaborate or say hi? Drop your details below 👇</div>', unsafe_allow_html=True)
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message")

        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("✅ Thanks! I’ll get back to you ASAP.")

time.sleep(1.5)

# Online Section
with st.expander("🌐 Find Me Online"):
    st.markdown("""
    <div class="section">
        🔗 <a href="https://linkedin.com" target="_blank">LinkedIn</a><br>
        🧠 <a href="https://github.com" target="_blank">GitHub</a><br>
        ✍️ <a href="https://medium.com" target="_blank">Medium</a>
    </div>
    """, unsafe_allow_html=True)
