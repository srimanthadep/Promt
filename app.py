import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Prompt Manager",
    page_icon="💡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown(
    """
    <style>
        .main {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .title-container {
            text-align: center;
            margin-bottom: 2rem;
            padding: 1.5rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .title-text {
            font-size: 2.5rem;
            font-weight: 700;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .title-subtitle {
            font-size: 1.1rem;
            margin-top: 0.5rem;
            opacity: 0.9;
        }
        .input-section {
            background-color: #f8f9fa;
            padding: 2rem;
            border-radius: 12px;
            border: 1px solid #e9ecef;
            margin-bottom: 2rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }
        .prompt-card {
            background-color: white;
            border: 1px solid #dee2e6;
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            position: relative;
            overflow: hidden;
        }
        .prompt-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
        }
        .prompt-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .prompt-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #f1f3f4;
        }
        .prompt-number {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
        }
        .prompt-timestamp {
            color: #6c757d;
            font-size: 0.85rem;
            font-weight: 500;
        }
        .prompt-content {
            color: #343a40;
            line-height: 1.6;
            font-size: 1rem;
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 6px;
            border-left: 3px solid #667eea;
            margin-top: 1rem;
        }
        .stats-container {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }
        .stats-number {
            font-size: 2rem;
            font-weight: 700;
            margin: 0;
        }
        .stats-label {
            font-size: 0.9rem;
            margin-top: 0.25rem;
            opacity: 0.9;
        }
        .empty-state {
            text-align: center;
            padding: 3rem 2rem;
            color: #6c757d;
            background-color: #f8f9fa;
            border-radius: 12px;
            border: 2px dashed #dee2e6;
            margin-top: 2rem;
        }
        .empty-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
            opacity: 0.5;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1.5rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .stTextArea > div > div > textarea {
            border-radius: 8px;
            border: 2px solid #e9ecef;
            transition: border-color 0.3s ease;
        }
        .stTextArea > div > div > textarea:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
        }
    </style>
    """, unsafe_allow_html=True
)

# Initialize session state
if "prompts" not in st.session_state:
    st.session_state.prompts = []

# Title
st.markdown(
    """
    <div class="title-container">
        <h1 class="title-text">💡 Prompt Manager</h1>
        <p class="title-subtitle">Store, organize, and manage your prompts with style</p>
    </div>
    """, unsafe_allow_html=True
)

# Input section
st.markdown('<div class="input-section">', unsafe_allow_html=True)
col1, col2 = st.columns([4, 1])

with col1:
    new_prompt = st.text_area(
        "Enter your prompt:",
        height=120,
        placeholder="Type your prompt here… (e.g., ‘Write a creative story about…’)",
        help="Enter a detailed prompt that you want to save for future use."
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("💾 Save Prompt", type="primary"):
        if new_prompt.strip():
            prompt_entry = {
                "content": new_prompt.strip(),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "id": len(st.session_state.prompts) + 1
            }
            st.session_state.prompts.append(prompt_entry)
            st.success(f"✅ Prompt #{prompt_entry['id']} saved successfully!")
            st.rerun()
        else:
            st.warning("⚠️ Please enter a prompt before saving.")

if st.session_state.prompts:
    if st.button("🗑️ Clear All", type="secondary"):
        st.session_state.prompts = []
        st.success("🧹 All prompts cleared!")
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Stats
if st.session_state.prompts:
    total_prompts = len(st.session_state.prompts)
    st.markdown(
        f"""
        <div class="stats-container">
            <p class="stats-number">{total_prompts}</p>
            <p class="stats-label">Saved Prompt{'s' if total_prompts != 1 else ''}</p>
        </div>
        """, unsafe_allow_html=True
    )

# Display saved prompts
st.markdown("## 📋 Your Saved Prompts")

if st.session_state.prompts:
    for prompt in reversed(st.session_state.prompts):
        st.markdown(
            f"""
            <div class="prompt-card">
                <div class="prompt-header">
                    <span class="prompt-number">#{prompt['id']}</span>
                    <span class="prompt-timestamp">📅 {prompt['timestamp']}</span>
                </div>
                <div class="prompt-content">{prompt['content']}</div>
            </div>
            """, unsafe_allow_html=True
        )
        with st.expander(f"Actions for Prompt #{prompt['id']}", expanded=False):
            c1, c2, c3 = st.columns(3)
            with c1:
                if st.button(f"📋 Copy", key=f"copy_{prompt['id']}"):
                    st.code(prompt['content'], language=None)
                    st.info("💡 Content displayed above - you can manually copy it!")
            with c2:
                if st.button(f"✏️ Edit", key=f"edit_{prompt['id']}"):
                    st.info("✏️ Edit functionality would go here in a full implementation!")
            with c3:
                if st.button(f"🗑️ Delete", key=f"delete_{prompt['id']}", type="secondary"):
                    st.session_state.prompts = [p for p in st.session_state.prompts if p['id'] != prompt['id']]
                    st.success(f"🗑️ Prompt #{prompt['id']} deleted!")
                    st.rerun()
else:
    st.markdown(
        """
        <div class="empty-state">
            <div class="empty-icon">📝</div>
            <h3>No prompts saved yet</h3>
            <p>Start by entering your first prompt above and click “Save Prompt” to get started!</p>
        </div>
        """, unsafe_allow_html=True
    )

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #6c757d; margin-top: 2rem;">
        <p>💡 <strong>Tip:</strong> All prompts are stored in your current session. They will be cleared when you refresh the page.</p>
    </div>
    """, unsafe_allow_html=True
)
