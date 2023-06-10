import csv
from db_connection import connection


def add_many_ingredients(ingredients):
    with connection.cursor() as cursor:
        cursor.fast_executemany = True
        cursor.executemany("""
        INSERT INTO Igrredients (Names, Calories, Proteins, Fats, Carbs, Fibers, Igrredient_Types)
         VALUES (?,?,?,?,?,?,?)
        """, ingredients)


def load_initial_data(filename='ingredients.csv') -> None:
    with open(filename, 'r', encoding='UTF-8', newline='') as ingredients_file:
        reader = csv.reader(ingredients_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        ingredients_file.readline()  # Ignore headers
        igredients = []
        for row in reader:
            igredients.append(row)
        add_many_ingredients(igredients)
