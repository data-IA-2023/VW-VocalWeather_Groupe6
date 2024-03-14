import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
from database import sendresultspeech, senderrorspeech


repertoir_fichier = os.path.dirname(__file__)
env_path = f'{repertoir_fichier}/.env'
load_dotenv(dotenv_path=env_path)

def speech_to_text():
    try: # clé et région dans le .env
        speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
        speech_config.speech_recognition_language="fr-FR"

        audio_config = speechsdk.audio.AudioConfig(filename='audio.wav')
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
        
        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return speech_recognition_result.text
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            return "Nous avons pas réussi à detecter votre voix: {}".format(speech_recognition_result.no_match_details)
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            return "Programme annulée: {}".format(cancellation_details.reason)
        sendresultspeech(speech_recognition_result.text)
    except Exception as error:
        senderrorspeech(error)