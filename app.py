import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Mydeen Raahina | Portfolio", page_icon="📊", layout="wide")

# --- Initial State ---
if "section" not in st.session_state:
    st.session_state.section = "home"

# --- CSS Styling ---
st.markdown("""
    <style>
    .topnav {
        display: flex;
        justify-content: center;
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .topnav button {
        background-color: #ffffff;
        border: 1px solid #ccc;
        padding: 0.6rem 1.2rem;
        margin: 0 0.5rem;
        border-radius: 10px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .topnav button:hover {
        background-color: #dbe8f3;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# --- Navigation Bar ---
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([1, 1, 1, 1])
with nav_col1:
    if st.button("🏠 Home"):
        st.session_state.section = "home"
with nav_col2:
    if st.button("💼 Experience"):
        st.session_state.section = "experience"
with nav_col3:
    if st.button("🧠 Skills & Projects"):
        st.session_state.section = "skills"
with nav_col4:
    if st.button("📨 Contact Me"):
        st.session_state.section = "contact"

# --- Home Section ---
if st.session_state.section == "home":
    st.markdown("<h1 style='text-align: center;'>👋 Hi, I'm <span style='color:#3085C3;'>Mydeen Raahina</span></h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: gray;'>Aspiring Data Analyst | AI Enthusiast | Python Developer</h3>", unsafe_allow_html=True)
    st.image("https://cdn.pixabay.com/photo/2020/06/30/20/23/girl-5352514_1280.jpg", use_column_width=True)
    st.markdown("### 🚀 Welcome to my portfolio!")
    st.write("I specialize in turning data into actionable insights using tools like Python, Pandas, SQL, and Streamlit. I'm also passionate about building AI-powered apps like meme generators and emoji predictors!")

# --- Experience Section ---
elif st.session_state.section == "experience":
    st.markdown("## 💼 Experience")
    st.markdown("### Data Analyst Intern @ ABC Corp (2024)")
    st.write("""
    - Cleaned and analyzed real-time sales data using Pandas and SQL  
    - Built interactive dashboards in Tableau and Power BI  
    - Collaborated with cross-functional teams to derive data-driven decisions
    """)
    st.markdown("### AI Project Intern @ XYZ Innovations")
    st.write("""
    - Built a meme generator using VGG16 + LSTM  
    - Integrated GloVe embeddings for better NLP understanding  
    - Applied multi-modal learning (image + text)
    """)

# --- Skills & Projects Section ---
elif st.session_state.section == "skills":
    st.markdown("## 🧠 Skills & Projects")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ⚙️ Skills")
        st.write("""
        - **Languages**: Python, SQL  
        - **Libraries**: Pandas, NumPy, Matplotlib, Scikit-learn  
        - **Tools**: Streamlit, Tableau, Power BI  
        - **Concepts**: EDA, Regression, Classification, NLP  
        """)

    with col2:
        st.markdown("### 📂 Projects")
        st.write("""
        - 🖼️ **AI Meme Caption Generator** — Generates funny captions from image + label  
        - 🤖 **Emoji Predictor** — Predicts emojis from text using NLP  
        - 📊 **Sales Dashboard** — Built with Power BI for a retail store  
        """)

# --- Contact Section ---
elif st.session_state.section == "contact":
    st.markdown("## 📨 Contact Me")
    st.write("Let's connect! I'm open to internships, collaborations, and learning opportunities.")

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message", placeholder="What's on your mind?")
        if st.form_submit_button("Send Message"):
            st.success("✅ Thank you! I'll get back to you soon.")

    st.markdown("---")
    st.markdown("📧 Email: mydeen@example.com")
    st.markdown("🌐 [LinkedIn](https://www.linkedin.com/in/mydeenraahina)")

# --- Footer ---
st.markdown("<hr style='margin-top: 40px;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Made with ❤️ by Mydeen Raahina using Streamlit</p>", unsafe_allow_html=True)
