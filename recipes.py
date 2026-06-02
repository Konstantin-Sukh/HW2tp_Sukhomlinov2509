
class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self._quantity = None
        self.quantity = quantity
        self.unit = unit
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        
        self._quantity = value

    def __str__(self):
        return f"{self.name}: {self.quantity:.1f} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', '{self.quantity:.1f}', '{self.unit}')"

    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        
        return self.name == other.name and self.unit == other.unit


class Recipe:
    def __init__(self, title: str, ingredients=None):
        self.title = title
        self.ingredients = ingredients if ingredients is not None else []
    
    def add_ingredient(self, ingredient: Ingredient):
        for i, ing in enumerate(self.ingredients):
            if ing == ingredient:
                self.ingredients[i].quantity = ing.quantity + ingredient.quantity
                return
            
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0
    
    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент масштабирования должен быть положительным числом")
        
        new_ingredients = []
        for ing in self.ingredients:
            new_ingredients.append(Ingredient(ing.name, ing.quantity * ratio, int.unit))

        return Recipe(self.title, new_ingredients)
    
    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        recipe_text = [f"Рецепт: {self.title}"]
        for ing in self.ingredients:
            recipe_text.append(f"  {ing}")
        return "\n".join(recipe_text)


class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled_recipe = recipe.scale(portions)
        for ing in scaled_recipe.ingredients:
            self._items.append((ing, recipe.title))

    def remove_recipe(self, title: str):
        self._items = [item for item in self._items if item[1] != title]

    def get_list(self):
        res_lst = {}
        for ing, recipe_title in self._items:
            key = (ing.name, ing.unit)
            if key in res_lst:
                res_lst[key] += ing.quantity
            else:
                res_lst[key] = ing.quantity
        result = [Ingredient(name, qty, unit) for (name, unit), qty in res_lst.items()]
        result.sort(key=lambda ing: ing.name)
        return result

    def __add__(self, other):
        if not isinstance(other, ShoppingList):
            return False
        new_lst = ShoppingList()
        new_lst._items = self._items + other._items
        return new_lst
    
class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
        
    def scale(self, ratio: float):
        scaled = super().scale(ratio)
        return DietaryRecipe(scaled.title, self.diet_type, scaled.ingredients)
    
    def __str__(self):
        return f"[{self.diet_type}] {self.title}"
    
