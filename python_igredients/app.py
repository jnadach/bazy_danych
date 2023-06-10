from program_strategy import AddNewIngredient, ListIngredients, ListIngredientsByNameLike, TerminateProgram, \
    LoadInitialData

if __name__ == '__main__':
    strategy_map = {
        "1": AddNewIngredient(),
        "2": ListIngredients(),
        "3": ListIngredientsByNameLike(),
        "4": LoadInitialData(),
        "0": TerminateProgram()
    }
    while True:
        print("1 - Dodaj składnik", "2 - Pokaż wszystkie", "3 - Szukaj po nazwie", "4 - Ładowanie danych",
              "0 - Zakończ",
              "Wybierz co chcesz zrobić: ", sep='\n')
        decision = input("> ")

        if decision not in strategy_map:
            print("Proszę wybrać poprawną wartość")
        else:
            strategy_map[decision].execute()
