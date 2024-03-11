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
            select s.name as schema_name, 
    s.schema_id,
    u.name as schema_owner
from sys.schemas s
    inner join sys.sysusers u
        on u.uid = s.principal_id
order by s.name
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
