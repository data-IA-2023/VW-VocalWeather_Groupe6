from speech_recognition import speech_to_text
import streamlit as st
from audiorecorder import audiorecorder

st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Click to stop recording")

if len(audio) > 0:
    audio.export("audio.wav", format="wav")

#On utilise audio.wav pour convertir l'audio au text
st.write(speech_to_text())
