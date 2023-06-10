import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

database_password = os.environ.get('DATABASE_PASSWORD')
database_server = 'morfeusz.wszib.edu.pl'
database_name = 'nadachow'
database_user = 'nadachow'
driver = '{ODBC Driver 18 for SQL Server}'

connection_string = f'Driver={driver};' \
                    f'SERVER={database_server};' \
                    f'DATABASE={database_name};' \
                    f'UID={database_user};' \
                    f'PWD={database_password};' \
                    'Encrypt=no;'

connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

# cursor.execute("CREATE TABLE users (id int identity, name varchar(100), age int)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Andrzej', 29)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Maciej', 25)")

cursor = cursor.execute("SELECT * FROM users")

# Sposoby pobierania rekordow
# results = cursor.fetchall()
# results = cursor.fetchone()
# results = cursor.fetchmany(5)

for row in cursor:
    print(row)

cursor.close()
connection.close()


# INSERT, CREATE, DROP, DELETE itp. otwieraja transakcje
