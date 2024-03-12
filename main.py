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
from speech_recognition import speech_to_text
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
import streamlit as st
from audiorecorder import audiorecorder
import pandas as pd
import datetime
# import pydub
# pydub.AudioSegment.ffmpeg = "C:/Users/sandy/Documents/devIA/brief/vw_vocal_weather/VW-VocalWeather_Groupe6/env/Lib/site-packages/ffmpeg-6.1.1"

# =========================================
# main run : streamlit run c:/Users/sandy/Documents/devIA/brief/vw_vocal_weather/VW-VocalWeather_Groupe6/main.py
# =========================================

# =========================================
# side_bar
# =========================================


# styl = f"""
# <style>
# 	.reportview-container .main .block-container{{
# 		{max_width_str}
# 		padding-top: {padding_top}rem;
# 		padding-right: {padding_right}rem;
# 		padding-left: {padding_left}rem;
# 		padding-bottom: {padding_bottom}rem;
# 	}}
# 	}}
# </style>
# """

# =========================================
# main_contenent
# =========================================

st.title("Vocal Weather")
st.write("Appuyer sur le bouton pour parler et faire votre démande météo")

#On utilise audio.wav pour convertir l'audio au text

audio = audiorecorder("Parler", "Finir la commande")
if len(audio) > 0:
    audio.export("audio.wav", format="wav")

text = speech_to_text()
print("text :", text)
#info = {'where':'tours','when': datetime.datetime(2024,3,12)}

info = get_info(text)
print("info :", info)
location = info['where']
time = info['when']
print("location :", location, "time :", time)
time_str = time.strftime("%Y%m%d%H%M%S")
time_int = int(time_str)
print("times :", time_int)

coordinates = geocode_address(location)
print("coordinates :", coordinates)

df_meteo = get_meteo(coordonnee = coordinates, startdate = time_int)
print("df_meteo :", df_meteo)
coordinates_in_df = pd.DataFrame.from_dict({'latitude':[coordinates[0]], 'longitude':[coordinates[1]]}) #st.map prends un dataframe
st.write(df_meteo)
st.map(coordinates_in_df)