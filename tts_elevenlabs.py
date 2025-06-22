from elevenlabs import generate, save, Voice
from elevenlabs.core.api_error import ApiError

def text_to_speech_elevenlabs(text):
    import os
    try:
        api_key = os.getenv("ELEVENLABS_API_KEY")
        if not api_key:
            raise ValueError("ELEVENLABS_API_KEY not found in environment.")

        audio = generate(
            text=text,
            voice=Voice(voice_id="Rachel"),  # Make sure "Rachel" exists
            api_key=api_key
        )
        save(audio, "output.wav")

    except ApiError as e:
        st.error(f"API Error from ElevenLabs: {e}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
