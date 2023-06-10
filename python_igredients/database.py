from connection import connection
from ingredient import Ingredient


def add_many_ingredients(ingredients):
    with connection.cursor() as cursor:
        cursor.fast_executemany = True
        cursor.executemany("""
        INSERT INTO ingredients (ingredient_name, calories, protein, fat, carbs, fiber, ingredient_type)
         VALUES (?,?,?,?,?,?,?)
        """, ingredients)


def add_ingredient(name, calories, protein, fat, carbs, fiber, ingredient_type) -> None:
    with connection.cursor() as cursor:
        cursor.execute("""
        INSERT INTO ingredients (ingredient_name, calories, protein, fat, carbs, fiber, ingredient_type)
         VALUES (?,?,?,?,?,?,?)
        """, (name, calories, protein, fat, carbs, fiber, ingredient_type))


def find_all():
    """
    Find all ingredients in list.
    :return: List of Ingredients
    """
    ingredients = []
    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM ingredients"):
        ingredients.append(Ingredient(*row))
    return ingredients


def find_by_name_like(name: str):
    """
    Find all ingredients by name like
    :param name: name 'like'
    :return: list of ingredients
    """
    ingredients = []
    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM ingredients WHERE ingredient_name like ?", (f'%{name}%',)):
        ingredients.append(Ingredient(*row))
    return ingredients
