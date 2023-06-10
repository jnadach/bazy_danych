from abc import ABC, abstractmethod
import database
import sys

import loader


class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass


class ListIngredients(Strategy):
    def execute(self):
        all_ingredients = database.find_all()
        for i in all_ingredients:
            print(i)


class ListIngredientsByNameLike(Strategy):
    def execute(self):
        ingredient_name = input("Proszę podać nazwę składnika: ")
        result = database.find_by_name_like(ingredient_name)
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
        database.add_ingredient(name, calories, protein, fat, carbs, fiber, ingredient_type)


class LoadInitialData(Strategy):
    def execute(self):
        loader.load_initial_data()


class TerminateProgram(Strategy):
    def execute(self):
        sys.exit()
