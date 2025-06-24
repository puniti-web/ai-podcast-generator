import streamlit as st
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def text_to_speech_ibm(text):
    try:
        api_key = st.secrets["api_keys"]["IBM_WATSON_TTS_API_KEY"]
        url = st.secrets["api_keys"]["IBM_WATSON_TTS_URL"]
    except KeyError:
        raise ValueError("Missing IBM Watson TTS credentials.")

    authenticator = IAMAuthenticator(api_key)
    tts = TextToSpeechV1(authenticator=authenticator)
    tts.set_service_url(url)

    with open("output.wav", "wb") as audio_file:
        response = tts.synthesize(
            text,
            voice="en-US_AllisonV3Voice",  # You can change this to another supported voice
            accept="audio/wav"
        ).get_result()
        audio_file.write(response.content)
