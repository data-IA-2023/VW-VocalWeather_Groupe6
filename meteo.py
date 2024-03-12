
import os
from dotenv import load_dotenv
import datetime as dt
import meteomatics.api as api

# Trouve le chemein du fichier .env et l'ouvre par dotenv
repertoir_fichier = os.path.dirname(__file__)
env_path = f'{repertoir_fichier}/.env'
load_dotenv(dotenv_path=env_path)

# valiable et lien de connexion à la base de donnée
username = subscription=os.getenv('username_meteo')
password = subscription=os.getenv('password_meteo')

def get_meteo(coordinates, startdate):

    # requet pour l'API de la meteo
    coordinates = [coordinates]
    parameters = ['t_2m:C', 'precip_1h:mm', 'wind_speed_10m:ms']
    model = 'mix'
    enddate = startdate + dt.timedelta(days=1)
    interval = dt.timedelta(hours=1)

    df = api.query_time_series(coordinates, startdate, enddate, interval, parameters, username, password, model=model)


    return df