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
# importations des librairie
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

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

# =========================================
# run : uvicorn main:app
# =========================================

# création de l'appli
app = FastAPI()

# création des listes de fichier dans les dociers "templates" et "static"
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

meteo = get_meteo

# appelle de la page home
@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "meteo_r":meteo})
    
# recognize_from_microphone()