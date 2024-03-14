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
            OUTPUT INSERTED.ID
            VALUES (?, ?, ?)
    """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY, datetime.now(), output, 'OK')
    conn.commit()
    cursor.close()
    conn.close()

def senderrorspeech(error):
    conn = pyodbc.connect(connectionString)
    SQL_QUERY = f"""
            INSERT INTO dbo.monitoring_vw (timestamp, result_stt, statut_stt) 
            OUTPUT INSERTED.ID
            VALUES (?, ?, ?)
    """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY, datetime.now(), error, 'ERROR')
    cursor.execute(SQL_QUERY)
    conn.commit()

def sendresultnlp(date, loc):
    conn = pyodbc.connect(connectionString)
    SQL_QUERY = f"""
            INSERT INTO dbo.monitoring_vw (timestamp, date_nlp, localisation_nlp, statut_nlp) 
            OUTPUT INSERTED.ID
            VALUES (?, ?, ?, ?)
    """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY, datetime.now(), date, loc, 'OK')
    conn.commit()
    cursor.close()
    conn.close()

def senderrornlp(error):
    conn = pyodbc.connect(connectionString)
    SQL_QUERY = f"""
            INSERT INTO dbo.monitoring_vw (timestamp, date_nlp, localisation_nlp) 
            OUTPUT INSERTED.ID
            VALUES (?, ?, ?, ?)
    """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY, datetime.now(), error, error, 'ERROR')
    conn.commit()
    cursor.close()
    conn.close()

def sendresultgeo(output):
    conn = pyodbc.connect(connectionString)
    SQL_QUERY = f"""
            INSERT INTO dbo.monitoring_vw (timestamp, localisation_geo, statut_geo) 
            OUTPUT INSERTED.ID
            VALUES (?, ?, ?)
    """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY, datetime.now(), output, 'OK')
    conn.commit()
    cursor.close()
    conn.close()

def senderrorgeo(error):
    conn = pyodbc.connect(connectionString)
    SQL_QUERY = f"""
            INSERT INTO dbo.monitoring_vw (timestamp, localisation_geo, statut_geo) 
            OUTPUT INSERTED.ID
            VALUES (?, ?, ?)
    """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY, datetime.now(), error, 'ERROR')
    conn.commit()
    cursor.close()
    conn.close()


def sendresultmeteo(output):
    conn = pyodbc.connect(connectionString)
    SQL_QUERY = f"""
            INSERT INTO dbo.monitoring_vw (timestamp, result_meteo, statut_meteo) 
            OUTPUT INSERTED.ID
            VALUES (?, ?, ?)
    """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY, datetime.now(), output, 'OK')
    conn.commit()
    cursor.close()
    conn.close()

def senderrormeteo(error):
    conn = pyodbc.connect(connectionString)
    SQL_QUERY = f"""
            INSERT INTO dbo.monitoring_vw (timestamp, result_meteo, statut_meteo) 
            OUTPUT INSERTED.ID
            VALUES (?, ?, ?)
    """
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY, datetime.now(), error, 'ERROR')
    conn.commit()
    cursor.close()
    conn.close()

