def read_recipes_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def parse_cookbook(file):
    cook_book = {}
    with open(file, 'r', encoding='utf-8') as rf:
        while True:
            dish_name = rf.readline().strip()
            if not dish_name:  # Если строка пустая, выходим из цикла
                break
            ingredient_count = int(rf.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_line = rf.readline().strip()
                ingredient_name, quantity, measure = ingredient_line.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
    return cook_book

def main():
    file_path = 'recipes.txt'  
    cook_book = parse_cookbook(file_path)
    for dish, ingredients in cook_book.items():
        print(f"{dish}:\n{ingredients}")

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
    file_path = 'recipes.txt'
    lines = read_recipes_from_file(file_path)
    cook_book = parse_cookbook(file_path)
    dish_list = ['Запеченный картофель', 'Омлет']
    person_count = 2
    shopping_list = get_shop_list_by_dishes(cook_book, dish_list, person_count)
    for dish, ingredients in cook_book.items():
        print(f"{dish}:\n{ingredients}")
    for ingredient, details in shopping_list.items():
        print(f"{ingredient}: {details}")    
     
if __name__ == '__main__':
    main()


import os

def merge_files_sorted_by_line_count(input_file_names, output_file_name):
    file_info = []

    for file_name in input_file_names:
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            line_count = len(lines)
            file_info.append((file_name, line_count, lines))

    # Сортируем файлы по количеству строк
    file_info.sort(key=lambda x: x[1])

    with open(output_file_name, 'w', encoding='utf-8') as result_file:
        for file_name, line_count, lines in file_info:
            result_file.write(f"{file_name}\n{line_count}\n")  # Записываем имя файла и количество строк
            result_file.writelines(lines)  # Записываем содержимое файла
    
    print(f"Файлы успешно объединены в {output_file_name}")

def main():
    # Список файлов для объединения
    input_file_names = ['1.txt', '2.txt']
    output_file_name = 'result.txt'
    
    merge_files_sorted_by_line_count(input_file_names, output_file_name)

if __name__ == '__main__':
    main()


