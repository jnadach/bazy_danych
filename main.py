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

connection.execute("CREATE TABLE users (id int identity, name varchar(100), age int)")
connection.execute("INSERT INTO users (name, age) VALUES ('Andrzej', 29)")
connection.execute("INSERT INTO users (name, age) VALUES ('Maciej', 25)")

cursor = connection.cursor()

cursor.execute("SELECT * FROM users")

for row, name, age in cursor:
    print(row)
    print(name)
    print(age)
    print(20*"-")

cursor.close()
connection.close()

