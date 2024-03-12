from speech_recognition import speech_to_text
import streamlit as st
from audiorecorder import audiorecorder
import pandas as pd
from nlp import get_info
from geocoding import geocode_address

st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Click to stop recording")

if len(audio) > 0:
    audio.export("audio.wav", format="wav")

#On utilise audio.wav pour convertir l'audio au text
text = speech_to_text()
ville = get_info(text)['where']
time = get_info(text)['when']

st.write(ville, time)

lat, lon = geocode_address(ville)

coordinates_in_df = pd.DataFrame.from_dict({'latitude':[lat], 'longitude':[lon]}) #st.map prends un dataframe
st.map(coordinates_in_df)
