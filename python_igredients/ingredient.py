class Ingredient:

    def __init__(self, id, name, calories, protein, fat, carbs, fiber, ingredient_type):
        self.id = id
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.fiber = fiber
        self.ingredient_type = ingredient_type

    def __str__(self):
        return "{0:<50} {1:<6} {2:<5}".format(self.name, self.calories, self.ingredient_type)
