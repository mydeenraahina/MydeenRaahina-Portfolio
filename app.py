import streamlit as st

st.set_page_config(layout="wide")

# Initialize session state
if "expand" not in st.session_state:
    st.session_state.expand = "home"

# Navigation bar with horizontal buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Home"):
        st.session_state.expand = "home"
with col2:
    if st.button("💼 Experience"):
        st.session_state.expand = "experience"
with col3:
    if st.button("🧠 Skills"):
        st.session_state.expand = "skills"
with col4:
    if st.button("📨 Contact"):
        st.session_state.expand = "contact"

# Content sections
with st.expander("🏠 Home", expanded=st.session_state.expand == "home"):
    st.write("Hi! I'm Mydeen Raahina, an aspiring data analyst...")

with st.expander("💼 Experience", expanded=st.session_state.expand == "experience"):
    st.write("Worked as a Data Analyst Intern...")

with st.expander("🧠 Skills", expanded=st.session_state.expand == "skills"):
    st.write("Skills: Python, SQL, Streamlit...")

with st.expander("📨 Contact", expanded=st.session_state.expand == "contact"):
    st.write("You can reach me at mydeen@example.com")
    
