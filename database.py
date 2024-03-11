"""
==========================================
classe :
methode : 
==========================================
"""
# importations des librairie
import os
from dotenv import load_dotenv
import pyodbc

# Trouve le chemein du fichier .env et l'ouvre par dotenv
repertoir_fichier = os.path.dirname(__file__)
print(repertoir_fichier)
env_path = f'{repertoir_fichier}/.env'
load_dotenv(dotenv_path=env_path)

# valiable et lien de connexion à la base de donnée
data_key = subscription=os.getenv('DATABASEMDP')
print(data_key)
connection_string  = f"Driver={{ODBC Driver 18 for SQL Server}};Server=vwgroupe6.database.windows.net,1433;Database=vocal_wether;Uid=groupe6;Pwd={data_key};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'"

# connection
conn = pyodbc.connect( connection_string ) 