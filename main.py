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
# ==========================================
# classe :
#     database
# methode : 
#     monitoring: insert les résultats a la BDD
# =========================================
from database import monitoring


# importations des librairie
import streamlit as st
from audiorecorder import audiorecorder
import pandas as pd
import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


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
time = None
coordinates = None

# main page
st.title("Vocal Weather")
st.write("Appuyer sur le bouton pour parler et faire votre démande météo")

# si session_state.stage==1 : l'utilisateur à cliquer sur "Parler"
if st.session_state.Parler :
    try  :
        #-----AZURE STT-----
        try:
            text = speech_to_text()
            statut_stt = "OK"
        except Exception as error:
            text = "unknown"
            statut_stt = error

        st.sidebar.write(f"Tu vien de dire : '{text}'")
        
        #-----CAMEMBERT NLP--------
        try:
            info = get_info(text)
            location = info['where']
            time = info['when']
            statut_nlp = "OK"
        except Exception as error:
            location = "unknown"
            time = datetime.date.today()
            statut_nlp = error

        st.sidebar.write(f"Tu chreche donc a avoir la météo à {location} pour le {time} ?")
        st.sidebar.write("Si ce n'est pas correcte, merci de recommencer.")
        
        #-----GOOGLE GEOCODING------
        try:
            coordinates = geocode_address(location)
            loc_coord = f"({coordinates[0]}, {coordinates[1]})"
            statut_geo = "OK"
        except Exception as error:
            loc_coord = "unknown"
            statut_geo = error

    except :
        st.sidebar.error("Tu n'as pas été assez compris par la reconnaissence vocal, merci de recommencer...")
        
#if coordinates != None and time != None :
try :
    st.write(f"à {location} le {time}, la météo sera :")
    
    #-----METEO METEOMATICS API-------
    try:
        df_meteo = get_meteo(coordonnee = coordinates, startdate = time)
        status_meteo = "OK"
    except Exception as error:
        status_meteo = error

    coordinates_in_df = pd.DataFrame.from_dict({'latitude':[coordinates[0]], 'longitude':[coordinates[1]]}) #st.map prends un dataframe
    
    df_meteo = df_meteo.reset_index()
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

#function pour envoyer tous les resultats à la base de données
monitoring(text, statut_stt, time, location, statut_nlp, loc_coord, statut_geo, status_meteo)

st.markdown('''<style>.st-emotion-cache-1v0mbdj e115fcil1
            { display: contents; } 
            </style>''', unsafe_allow_html=True)
