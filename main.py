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


