"""
==========================================
classe :
    API speechsdk appeller depuis Azure
methode : 
    recognize_from_microphone ()
==========================================
"""
# importations des librairie
import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

# Trouve le chemein du fichier .env et l'ouvre par dotenv
repertoir_fichier = os.path.dirname(__file__)
# print(repertoir_fichier)
env_path = f'{repertoir_fichier}/.env'
load_dotenv(dotenv_path=env_path)


# appelle l'API speechsdk depuis Azure
def recognize_from_microphone(path_audio = None):
    """
    ne supporte que le format WAV
    >>> recognize_from_microphone(f'{repertoir_fichier}/static/stt_test_1.wav')
    Vous avez un nouveau message.
    >>> recognize_from_microphone(f'{repertoir_fichier}/static/stt_test_2.wav')
    10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0.
    """
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.getenv('SPEECH_KEY'), region=os.getenv('SPEECH_REGION'))
    speech_config.speech_recognition_language="fr-FR"

    if path_audio != None :
        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=False, filename=path_audio)
    else :
        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

# test de la fonction recognize_from_microphone()
# recognize_from_microphone()
# recognize_from_microphone(f'{repertoir_fichier}/static/stt_test_1.wav')
# recognize_from_microphone(f'{repertoir_fichier}/static/stt_test_2.wav')