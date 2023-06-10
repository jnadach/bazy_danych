from ingredient import Ingredient
from db_connection import connection

ingredients = []


def add_ingredient(name, calories, protein, fat, carbs, fiber, ingredient_type) -> None:
    ingredients.append(Ingredient(name, calories, protein, fat, carbs, fiber, ingredient_type))
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO Igrredients (Names, Calories, Proteins, Fats, Carbs, Fibers, Igrredient_Types)
            VALUES (?,?,?,?,?,?,?) 
            """,
            (name, calories, protein, fat, carbs, fiber, ingredient_type))

def find_all():
    """
    Find all ingredients in list.
    :return: List of Ingredients
    """
    return ingredients.copy()


def find_by_name_like(name: str):
    """
    Find all ingredients by name like
    :param name: name 'like'
    :return: list of ingredients
    """
    copy = find_all()
    result = []

    for ingredient in copy:
        if name.casefold() in ingredient.name.casefold():
            result.append(ingredient)

    return result
