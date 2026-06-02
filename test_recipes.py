import pytest
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe

# ---- тесты класса Ingredient ----
def test_ingredient_creation():
    ing = Ingredient("Мука", 500.0, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"

def test_ingredient_str():
    ing = Ingredient("Мука", 500.0, "г")
    assert str(ing) == "Мука: 500.0 г"

def test_ingredient_eq():
    i1 = Ingredient("Мука", 600, "г")
    i2 = Ingredient("Мука", 1500, "г")
    i3 = Ingredient("Ветчина", 600, "г")
    i4 = Ingredient("Мука", 600, "кг")
    assert i1 == i2
    assert i1 != i3
    assert i1 != i4

def test_ingredient_quantity_positive():
    with pytest.raises(ValueError, match="Количество должно быть положительным"):
        Ingredient("Соль", -5, "г")
    ing = Ingredient("Соль", 10, "г")
    with pytest.raises(ValueError, match="Количество должно быть положительным"):
        ing.quantity = -1


# ---- тесты класса Recipe ----
def test_recipe_creation():
    r = Recipe("Пицца")
    assert r.title == "Пицца"
    assert r.ingredients == []

def test_add_ingredient():
    r = Recipe("ТП")
    i1 = Ingredient("рецепты", 3, "шт")
    i2 = Ingredient("тесты", 1000, "кг")
    r.add_ingredient(i1)
    r.add_ingredient(i2)
    assert len(r) == 2

    i3 = Ingredient("рецепты", 1, "шт")
    r.add_ingredient(i3)
    assert len(r) == 2

    for ing in r.ingredients:
        if ing.name == "Яйцо":
            assert ing.quantity == 4

def test_scale():
    r = Recipe("Блины")
    r.add_ingredient(Ingredient("Молоко", 300, "мл"))
    r.add_ingredient(Ingredient("Мука", 150, "г"))
    r2 = r.scale(2)
    assert r2 is not r
    assert len(r2) == 2
    for ing in r2.ingredients:
        if ing.name == "Мука":
            assert ing.quantity == 300
        if ing.name == "Молоко":
            assert ing.quantity == 600
    with pytest.raises(ValueError):
        r.scale(0)

def test_recipe_len():
    r = Recipe("Салат")
    r.add_ingredient(Ingredient("Капуста", 4, "шт"))
    r.add_ingredient(Ingredient("Чеснок", 10, "шт"))
    r.add_ingredient(Ingredient("Чеснок", 11, "шт"))
    r.add_ingredient(Ingredient("Лук", 15, "кг"))
    assert len(r) == 3


# ---- тесты класса ShoppingList ----