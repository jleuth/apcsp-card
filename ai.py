import os
mpv_dir = os.path.expanduser('~/Desktop/libmpv')  # Adjust if your unzip path differs
os.environ['PATH'] = mpv_dir + ':' + os.environ.get('PATH', '')  # Prepends so 'mpv' resolves to yours

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import stream
from openai import OpenAI
import os
import threading

load_dotenv()


SYSTEM_PROMPT = """

"""


class Eleven: # this was sorta ripped from elevenlabs docs
    def __init__(self):
        self.apiKey = os.getenv("ELEVENLABS_API_KEY")
        self.elevenLabs = ElevenLabs(api_key=self.apiKey)

    def generateSpeech(self, text, voiceId, modelId="eleven_v3", outputFormat="mp3_44100_128"):
        print('tried to speak')
        audio = self.elevenLabs.text_to_speech.stream(
            text=text,
            voice_id=voiceId,
            model_id=modelId,
            output_format=outputFormat,
        )
        stream(audio)

class OpenRouter:
    def __init__(self):
        self.apiKey = os.getenv("OPENROUTER_API_KEY")
        self.openRouter = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=self.apiKey)

    def generateVoiceLine(self, prompt):
        print('tried to generate voice line')

        try:
            completion = self.openRouter.chat.completions.create(
                model="meta-llama/llama-4-scout:free",
                messages=[{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": prompt}]
            )
            return completion.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating voice line: {e}")
