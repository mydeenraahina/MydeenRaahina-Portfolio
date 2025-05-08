import streamlit as st
import time

st.set_page_config(page_title="Mydeen Raahina Portfolio", layout="wide")

# CSS for animations and mild color accents
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@500&display=swap');

body, .stApp {
    background-color: #f8f9fa;
    font-family: 'Inter', sans-serif;
    color: #212529;
}

.heading {
    font-size: 42px;
    font-weight: bold;
    color: #0056b3; /* Softer blue */
    padding: 10px 0;
    margin-bottom: 10px;
    border-bottom: 2px solid #0056b3; /* Softer blue */
    animation: fadeIn 1s ease-in-out;
}

.typingEffect {
    display: inline-block;
    overflow: hidden;
    white-space: nowrap;
    border-right: 2px solid #0056b3; /* Softer blue */
    width: 0;
    animation: typing 3s steps(30) 1s 1 normal both;
    font-size: 20px;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    color: #0056b3; /* Softer blue */
    margin-top: 20px;
}

.section {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 10px;
    border: 1px solid #dee2e6;
    margin-bottom: 20px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    display: none;
    animation: fadeIn 1s ease-in-out;
}

.stExpander > summary {
    font-size: 18px;
    font-weight: 600;
    color: #0056b3; /* Softer blue */
}

.stExpander > summary:hover {
    color: #17a2b8;
    cursor: pointer;
}

form {
    background-color: #e9ecef;
    padding: 15px;
    border-radius: 10px;
}

a {
    color: #0056b3; /* Softer blue */
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

.stButton > button {
    background-color: #0056b3; /* Softer blue */
    color: white;
    border-radius: 5px;
    font-weight: bold;
    border: none;
    padding: 10px 20px;
    transition: background-color 0.3s ease;
}

.stButton > button:hover {
    background-color: #003366; /* Darker blue */
}

.stTextInput input, .stTextArea textarea {
    background-color: #f1f3f5;
    border-radius: 8px;
    border: 1px solid #dee2e6;
    padding: 10px;
}

.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: #0056b3; /* Softer blue */
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(-20px);}
    to {opacity: 1; transform: translateY(0);}
}

@keyframes typing {
    from { width: 0; }
    to { width: 100%; }
}

@keyframes slideIn {
    from { opacity: 0; transform: translateY(-20px);}
    to { opacity: 1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)

# Header with typing effect
st.markdown('<div class="heading">Hi! I\'m Mydeen Raahina</div>', unsafe_allow_html=True)

# Intro with typing effect
st.markdown('<div class="typingEffect">🎯 Data-driven, AI-focused, and design-conscious — I build intelligent apps that solve real-world problems using machine learning, prompt engineering, and beautiful code.</div>', unsafe_allow_html=True)

# Wait for 2 seconds to reveal the next section
time.sleep(2)

# Know More About Me Section
with st.expander("📖 Know More About Me"):
    st.markdown('<div class="typingEffect">🎓 Computer Science graduate passionate about building smart AI-powered solutions.<br> 💼 Skilled in prompt engineering, backend data workflows, and real-time AI integrations.<br> 🔗 Connect with me on <a href="https://linkedin.com" target="_blank">LinkedIn</a> or check my code on <a href="https://github.com" target="_blank">GitHub</a>.</div>', unsafe_allow_html=True)

# Wait for 2 seconds to reveal the next section
time.sleep(2)

# Experience Section
with st.expander("🧠 Experience"):
    st.markdown('<div class="typingEffect">AI/ML Engineer — Plattr Tech Studio<br> • Built prompt pipelines for Tax Fixxer to auto-suggest tax-saving strategies using OpenAI & LLaMA.<br> • Led scraping and backend data ingestion for Wim Card using Playwright.<br><br>Data Scientist Intern — Plattr Tech Studio<br> • OCR + ML classification for Tamil/English ads (Ad Classification Project).<br> • Vision-based motion detection AI game inspired by Talking Tom (Visionary Project).</div>', unsafe_allow_html=True)

# Wait for 2 seconds to reveal the next section
time.sleep(2)

# Contact Me Section
with st.expander("📬 Contact Me"):
    st.markdown('<div class="typingEffect">Want to collaborate or say hi? Drop your details below 👇</div>', unsafe_allow_html=True)

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message")

        submitted = st.form_submit_button("Send")

        if submitted:
            st.success("✅ Thanks! I’ll get back to you ASAP.")

# Wait for 2 seconds to reveal the next section
time.sleep(2)

# Find Me Online Section
with st.expander("🌐 Find Me Online"):
    st.markdown('<div class="typingEffect">🔗 <a href="https://linkedin.com" target="_blank">LinkedIn</a><br> 🧠 <a href="https://github.com" target="_blank">GitHub</a><br> ✍️ <a href="https://medium.com" target="_blank">Medium</a></div>', unsafe_allow_html=True)
