import streamlit as st
from ibm_watson_machine_learning.foundation_models import Model

credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": st.secrets["api_keys"]["WATSONX_API_KEY"]
}

project_id = st.secrets["api_keys"]["IBM_PROJECT_ID"]

parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 200,
    "temperature": 0.7
}

model = Model(
    model_id="ibm/granite-13b-instruct-v2",
    params=parameters,
    credentials=credentials,
    project_id=project_id
)

def generate_script(topic):
    topic = topic.strip()
    if not topic:
        raise ValueError("Topic cannot be empty.")
    prompt = f"Write a podcast script introduction on the topic: {topic}"
    response = model.generate_text(prompt)
    return response

