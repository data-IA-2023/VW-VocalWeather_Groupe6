"""
==========================================
classe :
    main
methode : 
    
==========================================
classe de l'appli fastAPI
appelle des api,
appelle de l'interface utilisateur
"""
# ==========================================
# classe :
#     API speechsdk appeller depuis Azure
# methode : 
#     recognize_from_microphone ()
# ==========================================
from speech_recognition import recognize_from_microphone
# ==========================================
# classe :
#     NLP
# methode : 
#     get_info(text)=> return info{'where':'', 'when':''}
#     date_jours_nom ( DATE ) => date (yyyy, mm, jj) à partir du nom d'un jours
# ==========================================
from nlp import get_info
# ==========================================
# classe :
#     geocoding
# methode : 
#     geocode_address(address): latitude, longitude => résultat de la requet de l'api 
# ==========================================
from geocoding import geocode_address
# ==========================================
# classe :
#     meteo
# methode : 
#     get_meteo: dataframe => résultat de la requet de l'api
# =========================================
from meteo import get_meteo

# importations des librairie
from speech_recognition import speech_to_text
import streamlit as st
from audiorecorder import audiorecorder
import pandas as pd
from nlp import get_info
from geocoding import geocode_address

# =========================================
# main
# =========================================

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