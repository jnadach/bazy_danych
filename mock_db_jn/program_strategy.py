from abc import ABC, abstractmethod
from db_connection import connection
import pyodbc
import loader
import sys


class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass


class InitialLoadToDatabase(Strategy):
    def execute(self):
        loader.load_initial_data()


class ListIngredients(Strategy):
    def execute(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Igrredients")
            for i in cursor:
                print(i)


class ListIngredientsByNameLike(Strategy):
    def execute(self):
        ingredient_name = input("Proszę podać nazwę składnika: ")
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Igrredients WHERE Names LIKE ?", (f'%{ingredient_name}%'))
            for i in cursor:
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
        with connection.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO Igrredients "
                               "(Names, Calories, Proteins, Fats, Carbs, Fibers, Igrredient_Types) "
                               "VALUES (?, ?, ?,?,?,?,?)",
                               (name, calories, protein, fat, carbs, fiber, ingredient_type))
            except pyodbc.IntegrityError:
                print("Składnik już istnieje.")



class TerminateProgram(Strategy):
    def execute(self):
        sys.exit()
