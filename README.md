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


def main():
    file_path = 'recipes.txt'  
    lines = read_recipes_from_file(file_path)
    cook_book = parse_cookbook(lines)
    for dish, ingredients in cook_book.items():
        print(f"{dish}:,'\n'{ingredients}")

if __name__ == '__main__':
    main()