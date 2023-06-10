import csv
import database


def load_initial_data(filename='ingredients.csv') -> None:
    with open(filename, 'r', encoding='UTF-8', newline='') as ingredients_file:
        reader = csv.reader(ingredients_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        ingredients_file.readline()  # Ignore headers
        ingredients = []
        for row in reader:
            ingredients.append(row)
        database.add_many_ingredients(ingredients)
