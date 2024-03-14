"""
==========================================
 classe :
     database
 methode : 
    monitoring: insert les résultats a la BDD
=========================================
"""
# importations des librairie
import pyodbc
import os
from dotenv import load_dotenv
from datetime import datetime

# Trouve le chemein du fichier .env et l'ouvre par dotenv
repertoir_fichier = os.path.dirname(__file__)
env_path = f'{repertoir_fichier}/.env'
load_dotenv(dotenv_path=env_path)

# valiable et lien de connexion à la base de donnée
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={os.environ.get('SERVER')};DATABASE={os.environ.get('DATABASE')};UID={os.environ.get('USERNAME')};PWD={os.environ.get('PASSWORD')}'
def monitoring(text, statut_stt, time, location, statut_nlp, loc_coord, statut_geo, status_meteo):
    # connection
    conn = pyodbc.connect( connectionString )

    SQL_QUERY = f"""
            INSERT INTO dbo.monitoring_vw (timestamp, result_stt, statut_stt, date_nlp, localisation_nlp, statut_nlp, localisation_geo, statut_geo, statut_meteo)
            OUTPUT INSERTED.ID
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY, datetime.now(), text, statut_stt, time, location, statut_nlp, loc_coord, statut_geo, status_meteo)
    conn.commit()
    cursor.close()
    conn.close()
