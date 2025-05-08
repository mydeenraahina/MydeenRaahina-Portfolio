import streamlit as st

st.set_page_config(layout="wide")

# Only one expander should be expanded at a time.
# You can manually set which section to expand by changing the value of `default_expand`.

default_expand = "home"  # Options: "home", "experience", "skills", "contact"

with st.expander("🏠 Home", expanded=(default_expand == "home")):
    st.write("Hi! I'm Mydeen Raahina, an aspiring data analyst...")

with st.expander("💼 Experience", expanded=(default_expand == "experience")):
    st.write("Worked as a Data Analyst Intern...")

with st.expander("🧠 Skills", expanded=(default_expand == "skills")):
    st.write("Skills: Python, SQL, Streamlit...")

with st.expander("📨 Contact", expanded=(default_expand == "contact")):
    st.write("You can reach me at mydeen@example.com")
