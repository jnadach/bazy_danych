import csv
from db_connection import connection


def load_initial_data(filename='ingredients.csv') -> None:
    with open(filename, 'r', encoding='UTF-8', newline='') as ingredients_file:
        reader = csv.reader(ingredients_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        ingredients_file.readline()  # Ignore headers
        for row in reader:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO Igrredients "
                               "(Names, Calories, Proteins, Fats, Carbs, Fibers, Igrredient_Types) "
                               "VALUES (?, ?, ?,?,?,?,?)",
                               (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
