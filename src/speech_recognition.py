
# Source: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/HEAD/speech/snippets/quickstart.py
# Imports the Google Cloud client library


from google.cloud import speech



def run_quickstart() -> speech.RecognizeResponse:
    # Instantiates a client
    client = speech.SpeechClient.from_service_account_file("C:/Users/wilso/OneDrive/Documents/Code/keys/analog-daylight-403506-6c4956196627.json")

    # The name of the audio file to transcribe
    file_name = "C:/Users/wilso/OneDrive/Documents/Code/CalHacks/data/TQBFJOTLD.wav"

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

    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")