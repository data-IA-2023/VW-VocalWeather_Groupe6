from speech_recognition import speech_to_text
import streamlit as st
from audiorecorder import audiorecorder
import pandas as pd
from nlp import get_info
from geocoding import geocode_address
from meteo import get_meteo

st.title("Vocal Weather")
st.write("Appuyer sur le bouton pour parler et faire votre démande météo")

#On utilise audio.wav pour convertir l'audio au text

audio = audiorecorder("Parler", "Finir la commande")
text = speech_to_text()

location = get_info(text)['where']
time = get_info(text)['when']


if len(audio) > 0:
    audio.export("audio.wav", format="wav")

coordinates = geocode_address(location)

coordinates_in_df = pd.DataFrame.from_dict({'latitude':[coordinates[0]], 'longitude':[coordinates[1]]}) #st.map prends un dataframe
st.write(get_meteo(coordinates, time))
st.map(coordinates_in_df)

