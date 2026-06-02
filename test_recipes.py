import pytest
from recipes import Ingredient, Recipe, ShoppingList

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
def test_shopping_list_add_recipe():
    r = Recipe("Омлет")
    r.add_ingredient(Ingredient("Яйцо", 3, "шт"))
    r.add_ingredient(Ingredient("Молоко", 100, "мл"))
    sl = ShoppingList()
    sl.add_recipe(r, 2)
    assert len(sl._items) == 2
    with pytest.raises(ValueError, match="Количество порций должно быть положительным"):
        sl.add_recipe(r, -1)

def test_shopping_list_remove_recipe():
    r1 = Recipe("Суп")
    r1.add_ingredient(Ingredient("Свекла", 2, "шт"))
    r2 = Recipe("Другой суп")
    r2.add_ingredient(Ingredient("Огурец", 3, "шт"))
    sl = ShoppingList()
    sl.add_recipe(r1, 1)
    sl.add_recipe(r2, 1)
    sl.remove_recipe("Суп")
    assert all(item[1] != "Суп" for item in sl._items)
    sl.remove_recipe("Нет в списке")

def test_shopping_list_get_list():
    r1 = Recipe("Каша")
    r1.add_ingredient(Ingredient("Молоко", 200, "мл"))
    r1.add_ingredient(Ingredient("Овсянка", 100, "г"))
    r2 = Recipe("Молочный напиток")
    r2.add_ingredient(Ingredient("Молоко", 500, "мл"))
    sl = ShoppingList()
    sl.add_recipe(r1, 1)
    sl.add_recipe(r2, 1)
    final = sl.get_list()
    assert len(final) == 2
    milk_drink = [ing for ing in final if ing.name == "Молоко"][0]
    assert milk_drink.quantity == 700
    assert final[0].name <= final[1].name

def test_shopping_list_add():
    sl1 = ShoppingList()
    sl2 = ShoppingList()
    r = Recipe("Печенье")
    r.add_ingredient(Ingredient("Мука", 150, "г"))
    sl1.add_recipe(r, 1)
    sl2.add_recipe(r, 1)
    sl3 = sl1 + sl2
    assert sl3 is not sl1 and sl3 is not sl2
    assert len(sl3._items) == 2
    assert len(sl1._items) == 1
    assert len(sl2._items) == 1
