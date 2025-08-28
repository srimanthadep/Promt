import streamlit as st
from datetime import datetime

# Page configuration

st.set_page_config(
page_title=“Prompt Manager”,
page_icon=“💡”,
layout=“centered”,
initial_sidebar_state=“collapsed”
)

# Custom CSS for simple monochromatic styling

st.markdown(
“””
<style>
.main {
padding-top: 2rem;
padding-bottom: 2rem;
}
.title-container {
text-align: center;
margin-bottom: 3rem;
padding: 2rem;
background-color: #f8f9fa;
border-radius: 8px;
border: 1px solid #e9ecef;
}
.title-text {
font-size: 2.2rem;
font-weight: 600;
margin: 0;
color: #212529;
}
.title-subtitle {
font-size: 1rem;
margin-top: 0.5rem;
color: #6c757d;
}
.input-section {
background-color: #ffffff;
padding: 2rem;
border-radius: 8px;
border: 1px solid #dee2e6;
margin-bottom: 2rem;
}
.stats-container {
background-color: #f8f9fa;
color: #495057;
padding: 1.5rem;
border-radius: 8px;
text-align: center;
margin-bottom: 2rem;
border: 1px solid #e9ecef;
}
.stats-number {
font-size: 2rem;
font-weight: 600;
margin: 0;
color: #212529;
}
.stats-label {
font-size: 0.9rem;
margin-top: 0.25rem;
color: #6c757d;
}
.success-message {
background-color: #f8f9fa;
border: 1px solid #dee2e6;
border-radius: 8px;
padding: 1rem;
margin: 1rem 0;
text-align: center;
color: #495057;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stButton > button {
background-color: #495057;
color: white;
border: none;
border-radius: 6px;
padding: 0.5rem 1.5rem;
font-weight: 500;
transition: all 0.2s ease;
}
.stButton > button:hover {
background-color: #343a40;
}
.stButton > button[data-baseweb=“button”][kind=“secondary”] {
background-color: #6c757d;
color: white;
}
.stButton > button[data-baseweb=“button”][kind=“secondary”]:hover {
background-color: #5a6268;
}
.stTextArea > div > div > textarea {
border-radius: 6px;
border: 1px solid #ced4da;
transition: border-color 0.2s ease;
}
.stTextArea > div > div > textarea:focus {
border-color: #495057;
box-shadow: 0 0 0 0.1rem rgba(73, 80, 87, 0.2);
}
.footer-tip {
text-align: center;
color: #6c757d;
margin-top: 2rem;
padding: 1rem;
background-color: #f8f9fa;
border-radius: 6px;
border: 1px solid #e9ecef;
}
</style>
“””, unsafe_allow_html=True
)

# Initialize session state

if “prompts” not in st.session_state:
st.session_state.prompts = []

# Title

st.markdown(
“””
<div class="title-container">
<h1 class="title-text">Prompt Manager</h1>
<p class="title-subtitle">Simple prompt storage and management</p>
</div>
“””, unsafe_allow_html=True
)

# Input section

st.markdown(’<div class="input-section">’, unsafe_allow_html=True)

new_prompt = st.text_area(
“Enter your prompt:”,
height=150,
placeholder=“Type your prompt here…”,
help=“Enter a prompt that you want to save.”
)

col1, col2 = st.columns([3, 1])

with col1:
if st.button(“Save Prompt”, type=“primary”):
if new_prompt.strip():
prompt_entry = {
“content”: new_prompt.strip(),
“timestamp”: datetime.now().strftime(”%Y-%m-%d %H:%M:%S”),
“id”: len(st.session_state.prompts) + 1
}
st.session_state.prompts.append(prompt_entry)
st.success(“Prompt saved successfully!”)
st.rerun()
else:
st.warning(“Please enter a prompt before saving.”)

with col2:
if st.session_state.prompts:
if st.button(“Clear All”, type=“secondary”):
st.session_state.prompts = []
st.success(“All prompts cleared!”)
st.rerun()

st.markdown(’</div>’, unsafe_allow_html=True)

# Stats only

if st.session_state.prompts:
total_prompts = len(st.session_state.prompts)
st.markdown(
f”””
<div class="stats-container">
<p class="stats-number">{total_prompts}</p>
<p class="stats-label">Prompt{‘s’ if total_prompts != 1 else ‘’} Saved</p>
</div>
“””, unsafe_allow_html=True
)

# Footer tip

st.markdown(”—”)
st.markdown(
“””
<div class="footer-tip">
<p><strong>Note:</strong> Prompts are stored in your current session and will be cleared when you refresh the page.</p>
</div>
“””, unsafe_allow_html=True
)