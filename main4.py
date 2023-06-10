# PRZYKŁAD 'executescript' --> sql injection



import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

database_password = os.environ.get('DATABASE_PASSWORD')
database_server = 'morfeusz.wszib.edu.pl'
database_name = 'nadachow'
database_user = 'nadachow'
driver = '{ODBC Driver 18 for SQL Server}'

# DOcumentation https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Windows
connection_string = f'Driver={driver};' \
                    f'SERVER={database_server};' \
                    f'DATABASE={database_name};' \
                    f'UID={database_user};' \
                    f'PWD={database_password};' \
                    'Encrypt=no;'

connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

update_sql = []


new_name = input('Proszę podać imię: ')


sql = f"UPDATE users SET email='update@sql.injection' WHERE name ={new_name}"

split_arr = sql.split(';')

for update in split_arr:
    cursor.execute(update)

cursor.commit()

cursor.close()
connection.close()



