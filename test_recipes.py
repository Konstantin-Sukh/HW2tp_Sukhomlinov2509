import pytest
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe

# ---- тесты класса Ingredient ----
def test_ingredient_creation():
    ing = Ingredient("Мука", 500.0, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"
