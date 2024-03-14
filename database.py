"""
Connects to a SQL database using pyodbc
"""
import pyodbc
import os
from dotenv import load_dotenv
from datetime import datetime


repertoir_fichier = os.path.dirname(__file__)
env_path = f'{repertoir_fichier}/.env'
load_dotenv(dotenv_path=env_path)

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={os.environ.get('SERVER')};DATABASE={os.environ.get('DATABASE')};UID={os.environ.get('USERNAME')};PWD={os.environ.get('PASSWORD')}'

def sendresultspeech(output):
    conn = pyodbc.connect(connectionString)
    SQL_QUERY = f"""
            INSERT INTO dbo.monitoring_vw (timestamp, result_stt, statut_stt)
            VALUES ({datetime.now()} {output} {'OK'})
    """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)

def senderrorspeech(error):
    conn = pyodbc.connect(connectionString)
    SQL_QUERY = f"""
            INSERT INTO dbo.monitoring_vw (timestamp, result_stt, statut_stt) 
            VALUES ({datetime.now()} {error} {'ERROR'})
    """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)

def sendresultnlp(date, loc):
    conn = pyodbc.connect(connectionString)
    SQL_QUERY = f"""
            INSERT INTO dbo.monitoring_vw (timestamp, date_nlp, localisation_nlp) 
            VALUES ({datetime.now()} {date} {loc})
    """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)


def senderrornlp(error):
    conn = pyodbc.connect(connectionString)
    SQL_QUERY = f"""
            INSERT INTO dbo.monitoring_vw (timestamp, date_nlp, localisation_nlp) 
            VALUES ({datetime.now()} {error} {'ERROR'})
    """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)

def sendresultgeo(output):
    conn = pyodbc.connect(connectionString)
    SQL_QUERY = f"""
            INSERT INTO dbo.monitoring_vw (timestamp, localisation_geo, statut_geo) 
            VALUES ({datetime.now()} {output} {'OK'})
    """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)

def senderrorgeo(error):
    conn = pyodbc.connect(connectionString)
    SQL_QUERY = f"""
            INSERT INTO dbo.monitoring_vw (timestamp, localisation_geo, statut_geo) 
            VALUES ({datetime.now()} {error} {'ERROR'})
    """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)


def sendresultmeteo(output):
    conn = pyodbc.connect(connectionString)
    SQL_QUERY = f"""
            INSERT INTO dbo.monitoring_vw (timestamp, result_meteo, statut_meteo) 
            VALUES ({datetime.now()} {output} {'OK'})
    """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)

def senderrormeteo(error):
    conn = pyodbc.connect(connectionString)
    SQL_QUERY = f"""
            INSERT INTO dbo.monitoring_vw (timestamp, result_meteo, statut_meteo) 
            VALUES ({datetime.now()} {error} {'ERROR'})
    """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)

