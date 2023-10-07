#Задача 1

with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file.read().split('\n\n'):
        meal_name, *ingredients = line.split('\n')
        cook_list = []
        for ingredient in ingredients[1:]:
            ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, ingredient.split(' | '))
            cook_list.append(
                {'ingredient_name': ingredient_name,
                 'quantity': quantity,
                 'measure': measure
                 }
            )
        cook_book[meal_name] = cook_list
    del cook_book["Фахитос"]
# print(cook_book)

#Задача 2

    def get_shop_list_by_dishes(dishes, person_count = 1):
        # print(dishes)
        ingredient_dict_all = {}
        for dish in dishes:
            # print(dish)
            for el in cook_book[dish]:
                # print(el)
                ingredient_dict = {}
                ingredient_name = el['ingredient_name']
                work_dict = {}
                quantity = int(el['quantity']) * person_count
                work_dict['measure'] = el['measure']
                work_dict['quantity'] = quantity
                ingredient_dict[ingredient_name] = work_dict
                for key in ingredient_dict:
                    if key in  ingredient_dict_all:
                     ingredient_dict[key]['quantity'] += ingredient_dict_all[key]['quantity']
                ingredient_dict_all.update(ingredient_dict)
        print(ingredient_dict_all)
    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)