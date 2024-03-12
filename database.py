"""
Connects to a SQL database using pyodbc
"""
import pyodbc
import os
from dotenv import load_dotenv


repertoir_fichier = os.path.dirname(__file__)
env_path = f'{repertoir_fichier}/.env'
load_dotenv(dotenv_path=env_path)

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={os.environ.get('SERVER')};DATABASE={os.environ.get('DATABASE')};UID={os.environ.get('USERNAME')};PWD={os.environ.get('PASSWORD')}'

conn = pyodbc.connect(connectionString)

SQL_QUERY = """

"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
