# Recipe Management System (Система управления рецептами)

Консольное приложение для создания рецептов, управления ингредиентами, масштабирования порций, формирования списка покупок и поддержки диетических категорий (веган, без глютена и т.д.). Реализовано на Python с использованием ООП.

## Использование

Пример кода для работы с библиотекой:

```python
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe

# Создаём ингредиенты
flour = Ingredient("Мука", 500.0, "г")
eggs = Ingredient("Яйца", 2, "шт")

# Создаём рецепт
recipe = Recipe("Омлет")
recipe.add_ingredient(eggs)
recipe.add_ingredient(Ingredient("Молоко", 50, "мл"))

# Масштабируем на 2 порции
double_recipe = recipe.scale(2)

# Диетический рецепт
vegan_pizza = DietaryRecipe("Пицца", "веган", [Ingredient("Тесто", 200, "г")])
print(vegan_pizza)   # [веган] Пицца

# Список покупок
shopping = ShoppingList()
shopping.add_recipe(recipe, 3)   # 3 порции омлета
shopping.add_recipe(double_recipe, 1)

# Итоговый список
for ing in shopping.get_list():
    print(ing)
```
## Установка и запуск тестов

Чтобы развернуть проект на своем устройстве, выполните команды:
```bash
git clone https://github.com/Konstantin-Sukh/HW2tp_Sukhomlinov2509.git
cd /Users/konstantin_sukh/Downloads/HW2_Konst_Sukh2509
pip install -r requirements.txt
pytest (у меня сначала надо было прописать: pip3 install pytest)
```
Примечания:
- Требуется Python версии 3.8 или выше.
- После установки зависимостей команда pytest автоматически найдёт и выполнит все тесты из файла test_recipes.py.

## Автор

Сухомлинов Константин Сергеевич
Группа ББИ2509, НИУ ВШЭ ВШБ