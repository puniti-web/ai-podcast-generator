import streamlit as st
from watsonx_script import generate_script
from tts_ibm import text_to_speech_ibm
import time

# Page Config
st.set_page_config(page_title="AI Podcast Generator", layout="wide")

# Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #f5f5dc, #fbeec1);
        color: #002244;
    }
    h1 {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        color: #4b3f2f;
        margin-bottom: 5px;
    }
    .description {
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 40px;
        color: #5c4932;
    }
    .stTextInput>div>div>input {
        padding: 0.75rem;
        border-radius: 10px;
        font-size: 1rem;
        border: 1px solid #d8bfae;
        background-color: #fffdf5;
    }
    .stButton>button {
        background-color: #8b6f47;
        color: white;
        font-size: 1rem;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #a57c55;
        transform: scale(1.03);
    }
    .script-box {
        margin-top: 30px;
        padding: 25px;
        background-color: #fff8e7;
        border-left: 5px solid #8b6f47;
        border-radius: 10px;
        font-size: 1rem;
        line-height: 1.6;
        color: #4b3f2f;
    }
    .footer {
        margin-top: 50px;
        text-align: center;
        font-size: 14px;
        color: #7a6754;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>AI Podcast Generator</h1>", unsafe_allow_html=True)
st.markdown("<div class='description'>Generate podcast scripts and voices using IBM Watsonx</div>", unsafe_allow_html=True)

# Form UI
with st.container():
    with st.form("podcast_form"):
        topic = st.text_input("Enter your podcast topic", placeholder="e.g. The Future of AI")
        generate_voice = st.checkbox("Add voiceover using IBM Watson Text-to-Speech")
        submitted = st.form_submit_button("Generate Podcast")

        if submitted:
            if topic.strip() == "":
                st.warning("Please enter a topic.")
            else:
                with st.spinner("Generating podcast script using IBM Watsonx..."):
                    time.sleep(1.2)
                    script = generate_script(topic)

                st.markdown("### Your Podcast Script")
                st.markdown(f"<div class='script-box'>{script}</div>", unsafe_allow_html=True)

                if generate_voice:
                    with st.spinner("Generating voice using IBM Text-to-Speech..."):
                        text_to_speech_ibm(script)
                    st.success("Voice generated successfully!")
                    st.audio("output.wav", format="audio/wav")

# Footer
st.markdown("<div class='footer'>Built with IBM Watsonx | Designed by <b>Puniti Jodhwani</b></div>", unsafe_allow_html=True)
