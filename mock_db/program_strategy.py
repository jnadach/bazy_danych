from abc import ABC, abstractmethod
import mock_database
import sys


class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass


class ListIngredients(Strategy):
    def execute(self):
        all_ingredients = mock_database.find_all()
        for i in all_ingredients:
            print(i)


class ListIngredientsByNameLike(Strategy):
    def execute(self):
        ingredient_name = input("Proszę podać nazwę składnika: ")
        result = mock_database.find_by_name_like(ingredient_name)
        for i in result:
            print(i)


class AddNewIngredient(Strategy):
    def execute(self):
        print("Dodawanie nowego składnika")
        name = input("name: ")
        calories = input("calories: ")
        protein = input("protein: ")
        fat = input("fat: ")
        carbs = input("carbs: ")
        fiber = input("fiber: ")
        ingredient_type = input("ingredient_type: ")
        mock_database.add_ingredient(name, calories, protein, fat, carbs, fiber, ingredient_type)


class TerminateProgram(Strategy):
    def execute(self):
        sys.exit()
