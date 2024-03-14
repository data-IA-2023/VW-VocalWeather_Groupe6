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
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# import pydub
# pydub.AudioSegment.ffmpeg = "C:\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe"
# pydub.AudioSegment.converter = "C:\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe"
# pydub.AudioSegment.ffprobe ="C:\\ffmpeg\\ffmpeg\\bin\\ffprobe.exe"

# =========================================
# main run : streamlit run c:/Users/sandy/Documents/devIA/brief/vw_vocal_weather/VW-VocalWeather_Groupe6/main.py
# =========================================

# traitement du bouton de captation de l'audio
def set_audio():
    st.session_state.Parler = True

if 'Parler' not in st.session_state:
    st.session_state.Parler = False

# entête de la page 
st.set_page_config(
    page_title="Vocal_Weather",
    page_icon="static/icon.png",
)

# Customization for body
st.markdown('''<style>body 
            {font-family: "Arial", sans-serif;color: rgb(137,137,137);background-color: rgb(38,196,236);font-size: 20px;text-align: center;} 
            </style>''', unsafe_allow_html=True)
st.markdown('''<style>.st-emotion-cache-1ml213r
            {font-family: "Arial", sans-serif;color: rgb(137,137,137);background-color: rgb(38,196,236);font-size: 20px;} 
            </style>''', unsafe_allow_html=True)


# =========================================
# side_bar
# =========================================

# Customization for sidebar
st.markdown('''<style>.st-emotion-cache-ifmt0g
            { background-color: rgb(137,137,137);color: rgb(255,255,255);font-size: 25px;} 
            </style>''', unsafe_allow_html=True)

st.markdown('''<style>.st-emotion-cache-1kyxreq
            {align-items: center;display: contents;} 
            </style>''', unsafe_allow_html=True)

st.markdown('''<style>.st-emotion-cache-1v0mbdj
            {align-items: center;} 
            </style>''', unsafe_allow_html=True)

st.markdown('''<style>.st-emotion-cache-a31l0r 
            {background-color: rgb(38,196,236);} 
            </style>''', unsafe_allow_html=True)

# side bar
st.sidebar.image("static/logo_vw.png", width=100)
st.sidebar.button('Parler', on_click=set_audio)

# =========================================
# main_contenent
# =========================================

# Customization for main
st.markdown('''<style>.st-emotion-cache-1y4p8pa
            {background-color: rgb(255,255,255);color: rgb(137,137,137);height: 400%;font-size: 20px;} 
            </style>''', unsafe_allow_html=True)

st.markdown('''<style>.st-emotion-cache-1n76uvr
            { display: contents; } 
            </style>''', unsafe_allow_html=True)

st.markdown('''<style>h1 
            {font-family: "Lucida Handwriting", Cursive;color: #26c4ec;font-size: 50px;} 
            </style>''', unsafe_allow_html=True)

# variable de l'api météo
datetime_value = None
coordinates = None

# main page
st.title("Vocal Weather")
st.write("Appuyer sur le bouton pour parler et faire votre démande météo")

# si session_state.stage==1 : l'utilisateur à cliger sur "Parler"
if st.session_state.Parler :
    try  :
        text = speech_to_text()
        # text = "Quel temps fera-t-il à Paris demain ?"

        st.sidebar.write(f"Tu vien de dire : '{text}'")

        info = get_info(text)
        # print("info :", info)
        location = info['where']
        time = info['when']
        # print("location :", location, "time :", time)
        time_heur = datetime.time(hour=0, minute=0, second=0, microsecond=0)
        datetime_value = datetime.datetime.combine(time, time_heur)
        # print("times :", datetime_value)
        # print("location :", location, "time :", datetime_value)

        st.sidebar.write(f"Tu chreche donc a avoir la météo à {location} pour le {time} ?")
        st.sidebar.write("Si ce n'est pas correcte, merci de recommencer.")
        
        coordinates = geocode_address(location)
        # print("coordinates :", coordinates)

    except :
        st.sidebar.error("Tu n'as pas été assez compris par la reconnaissence vocal, merci de recommencer...")
        
if coordinates != None and datetime_value != None :
    try :
        # global gb_coordinates
        # gb_coordinates = coordinates
        # print("test 1 :", coordinates, datetime_value)

        st.write(f"à {location} le {time}, la météo sera :")

        # st.write(f"météo à {coordinates} pour le {datetime_value}")
        df_meteo = get_meteo(coordonnee = coordinates, startdate = datetime_value)
        print("df_meteo :", df_meteo)
        coordinates_in_df = pd.DataFrame.from_dict({'latitude':[coordinates[0]], 'longitude':[coordinates[1]]}) #st.map prends un dataframe
        
        # print("type 1 :",type(df_meteo))
        # print( df_meteo.info() )

        df_meteo = df_meteo.reset_index()
        # print("type 2 :",type(df_meteo))
        # print( df_meteo.info() )

        plt.style.use('ggplot')
        # figure
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111)
        ax.set_title("température, présipitation et vitesse du vent", color="#555555")
        # plot the differents quantities
        ax.plot(df_meteo["validdate"], df_meteo["t_2m:C"], marker="o", label="température", linestyle="--", linewidth=.5)
        ax.plot(df_meteo["validdate"], df_meteo["precip_1h:mm"], marker="o", label="présipitation", linestyle="--", linewidth=.5)
        ax.plot(df_meteo["validdate"], df_meteo["wind_speed_10m:ms"], marker="o", label="vitesse du vent", linestyle="--", linewidth=.5)
        # format and style
        ax.legend()
        fig.savefig("xy_pop.png", dpi=300)

        st.pyplot(fig)
        st.map(coordinates_in_df)
    except :
        st.sidebar.error("Le lieu ou la date n'ont pas été comprise, merci de recommencer...") 

st.markdown('''<style>.st-emotion-cache-1v0mbdj e115fcil1
            { display: contents; } 
            </style>''', unsafe_allow_html=True)

# =========================================
# ancienne vertion
# =========================================

# #On utilise audio.wav pour convertir l'audio au text
# audio = audiorecorder("Parler", "Finir la commande")
# if len(audio) > 0:
#     audio.export("audio.wav", format="wav")

# text = speech_to_text()
# print("text :", text)
# #info = {'where':'tours','when': datetime.datetime(2024,3,12)}

# info = get_info(text)
# print("info :", info)
# location = info['where']
# time = info['when']
# print("location :", location, "time :", time)
# time_heur = datetime.time(hour=0, minute=0, second=0, microsecond=0)
# datetime_value = datetime.datetime.combine(time, time_heur)
# print("times :", datetime_value)
# print("location :", location, "time :", datetime_value)

# coordinates = geocode_address(location)
# print("coordinates :", coordinates)

# df_meteo = get_meteo(coordonnee = coordinates, startdate = datetime_value)
# print("df_meteo :", df_meteo)
# coordinates_in_df = pd.DataFrame.from_dict({'latitude':[coordinates[0]], 'longitude':[coordinates[1]]}) #st.map prends un dataframe
# st.write(df_meteo)
# st.map(coordinates_in_df)