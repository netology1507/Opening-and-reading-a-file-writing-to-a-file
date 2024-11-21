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

if __name__ == '__main__':
    main()

