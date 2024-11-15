def read_recipes_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()


def parse_cookbook(lines):
    cook_book = {}
    i = 0
    while i < len(lines):
        # Получаем название блюда
        dish_name = lines[i].strip()
        i += 1

        # Получаем количество ингредиентов
        ingredient_count = int(lines[i].strip())
        i += 1

        ingredients = []
        for _ in range(ingredient_count):
            ingredient_line = lines[i].strip()
            ingredient_name, quantity, measure = ingredient_line.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
            i += 1

        cook_book[dish_name] = ingredients

    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shopping_list = {}
    for dish in dishes:
        if dish not in cook_book:
            continue
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            if name in shopping_list:
                shopping_list[name]['quantity'] += quantity
            else:
                shopping_list[name] = {'measure': measure, 'quantity': quantity}
    return shopping_list


def main():
    file_path = 'recipes.txt'  # Путь к файлу
    lines = read_recipes_from_file(file_path)
    cook_book = parse_cookbook(lines)
    dish_list = ['Запеченный картофель', 'Омлет']
    person_count = 2
    shopping_list = get_shop_list_by_dishes(cook_book, dish_list, person_count)
    for dish, ingredients in cook_book.items():
        print(f"{dish}:,'\n'{ingredients}")
    for ingredient, details in shopping_list.items():
        print(f"{ingredient}: {details}")
if __name__ == '__main__':
    main()

import os

file_names = ['1.txt', '2.txt']
file_info = []

for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        line_count = len(lines)
        file_info.append((file_name, line_count, lines))

file_info.sort(key=lambda x: x[1])

with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_name, line_count, lines in file_info:
        result_file.write(f"{file_name}\n{line_count}\n")  
        result_file.writelines(lines)  

print("Файлы успешно объединены в result.txt")