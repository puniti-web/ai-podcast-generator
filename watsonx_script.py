import streamlit as st
from ibm_watson_machine_learning.foundation_models import Model

# Load credentials securely from Streamlit secrets
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": st.secrets["IBM_API_KEY"]
}

project_id = st.secrets["IBM_PROJECT_ID"]

parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 200,
    "min_new_tokens": 20,
    "temperature": 0.7
}

model = Model(
    model_id="ibm/granite-13b-instruct-v2",
    params=parameters,
    credentials=credentials,
    project_id=project_id
)

def generate_script(topic):
    prompt = f"Write a podcast script introduction on the topic: {topic}"
    response = model.generate_text(prompt)
    return response
