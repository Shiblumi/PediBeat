# Imports the Google Cloud client library

from google.cloud import speech
import sys
sys.path.append('data/')


class SpeechRecognition:
    def __init__(self, file_path: str, api_key: str):
        self.file_path = file_path
        self.api_key = api_key
        
        
    def set_file_path(self, file_path: str):
        self.file_path = file_path
        
        
    def set_api_key(self, api_key: str):
        self.api_key = api_key
        
    # Source: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/HEAD/speech/snippets/quickstart.py
    def run(self) -> speech.RecognizeResponse:
        # Instantiates a client
        client = speech.SpeechClient.from_service_account_file(self.api_key)

        # The name of the audio file to transcribe
        file_name = self.file_path

        with open(file_name, "rb") as audio_file:
            wav_data = audio_file.read()

        audio = speech.RecognitionAudio(content=wav_data)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=48000,
            enable_automatic_punctuation=True,
            language_code="en-US",
        )

        # Detects speech in the audio file
        response = client.recognize(config=config, audio=audio)

        return response.results[0].alternatives[0].transcript