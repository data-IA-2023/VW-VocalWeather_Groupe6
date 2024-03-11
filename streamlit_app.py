from speech_recognition import speech_to_text
import streamlit as st
from audiorecorder import audiorecorder
import pandas as pd
from nlp import get_info

st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Click to stop recording")

if len(audio) > 0:
    audio.export("audio.wav", format="wav")

#On utilise audio.wav pour convertir l'audio au text
text = speech_to_text()

st.write(get_info(text))

lat = 47.392834
lon = 0.667747

df = pd.DataFrame.from_dict({'latitude':[lat], 'longitude':[lon]})
st.map(df)
