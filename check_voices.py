from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
import os

# Load .env and get API key
load_dotenv()
api_key = os.getenv("ELEVENLABS_API_KEY")

# Initialize ElevenLabs client
client = ElevenLabs(api_key=api_key)

# Get and print available voices
voices = client.voices.get_all()

for v in voices.voices:
    print(f"{v.name}: {v.voice_id}")
