"""
==========================================
classe :
    meteo
methode : 
    get_meteo: dataframe => résultat de la requet de l'api 
==========================================
"""

# importations des librairie
import os
from dotenv import load_dotenv
import datetime as dt
import meteomatics.api as api

# Trouve le chemein du fichier .env et l'ouvre par dotenv
repertoir_fichier = os.path.dirname(__file__)
print(repertoir_fichier)
env_path = f'{repertoir_fichier}/.env'
load_dotenv(dotenv_path=env_path)

# valiable et lien de connexion à la base de donnée
username = subscription=os.getenv('username_meteo')
password = subscription=os.getenv('password_meteo')

def get_meteo (coordinates = [(47.11, 11.47)], parameters = ['t_2m:C', 'precip_1h:mm', 'wind_speed_10m:ms'], 
               startdate = dt.datetime.utcnow().replace(minute=0, second=0, microsecond=0), 
               enddate_value = 1, interval_value = 1 ):
    # variable
    global username
    global password

    # requet pour l'API de la meteo
    model = 'mix'
    enddate = startdate + dt.timedelta(days=enddate_value)
    interval = dt.timedelta(hours=interval_value)

    df = api.query_time_series(coordinates, startdate, enddate, interval, parameters, username, password, model=model)
    print(df)
    
    return df