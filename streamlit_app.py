from speech_recognition import speech_to_text
import streamlit as st
from audiorecorder import audiorecorder
import pandas as pd
from nlp import get_info
from geocoding import geocode_address
from meteo import get_meteo
import datetime

st.title("Vocal Weather")
st.write("Appuyer sur le bouton pour parler et faire votre démande météo")

#On utilise audio.wav pour convertir l'audio au text

audio = audiorecorder("Parler", "Finir la commande")
if len(audio) > 0:
    audio.export("audio.wav", format="wav")

text = speech_to_text()

#info = {'where':'tours','when': datetime.datetime(2024,3,12)}

info = get_info(text)
location = info['where']
time = info['when']

coordinates = geocode_address(location)

coordinates_in_df = pd.DataFrame.from_dict({'latitude':[coordinates[0]], 'longitude':[coordinates[1]]}) #st.map prends un dataframe
st.write(get_meteo(coordinates, time))
st.map(coordinates_in_df)

