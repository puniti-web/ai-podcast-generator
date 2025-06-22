from elevenlabs.client import ElevenLabs
from elevenlabs.play import save
from dotenv import load_dotenv
import os

def text_to_speech_elevenlabs(text):
    load_dotenv()
    api_key = os.getenv("ELEVENLABS_API_KEY")

    client = ElevenLabs(api_key=api_key)

    audio = client.text_to_speech.convert(
        voice_id="9BWtsMINqrJLrRacOk9x",  # Aria
        model_id="eleven_monolingual_v1",
        text=text
    )

    save(audio, "output.wav")
