from program_strategy import InitialLoadToDatabase, AddNewIngredient, ListIngredients, ListIngredientsByNameLike, TerminateProgram

if __name__ == '__main__':
    strategy_map = {
        "0": InitialLoadToDatabase(),
        "1": AddNewIngredient(),
        "2": ListIngredients(),
        "3": ListIngredientsByNameLike(),
        "4": TerminateProgram()
    }
    while True:
        print("0 - Załaduj całość do bazy danych", "1 - Dodaj składnik", "2 - Pokaż wszystkie", "3 - Szukaj po nazwie", "4 - Zakończ",
              "Wybierz co chcesz zrobić: ", sep='\n')
        decision = input("> ")

        if decision not in strategy_map:
            print("Proszę wybrać poprawną wartość")
        else:
            strategy_map[decision].execute()
