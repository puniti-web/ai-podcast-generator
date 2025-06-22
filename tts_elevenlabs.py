import os
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings

def text_to_speech_elevenlabs(text):
    client = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY")
    )

    audio = client.generate(
        text=text,
        voice="Rachel",  # or any available voice
        model="eleven_multilingual_v2",
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.75
        )
    )

    with open("output.wav", "wb") as f:
        for chunk in audio:
            f.write(chunk)
