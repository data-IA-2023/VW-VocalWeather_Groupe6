"""
==========================================
classe :
    sql
methode : 
==========================================
"""
# importations des librairie
import pyodbc
import os
from dotenv import load_dotenv

# Trouve le chemein du fichier .env et l'ouvre par dotenv
repertoir_fichier = os.path.dirname(__file__)
env_path = f'{repertoir_fichier}/.env'
load_dotenv(dotenv_path=env_path)

# valiable et lien de connexion à la base de donnée
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={os.environ.get('SERVER')};DATABASE={os.environ.get('DATABASE')};UID={os.environ.get('USERNAME')};PWD={os.environ.get('PASSWORD')}'

# connection
conn = pyodbc.connect( connectionString )

# requet sql
SQL_QUERY = """
            select * from dbo.monitoring_vw
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
print(records)