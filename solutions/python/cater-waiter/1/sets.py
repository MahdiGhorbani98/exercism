"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    unique_ingredients = set(dish_ingredients)
    return (dish_name ,unique_ingredients)


def check_drinks(drink_name, drink_ingredients):

    isMocktail = set(drink_ingredients).isdisjoint(ALCOHOLS)
    
    if isMocktail:
        return f"{drink_name} Mocktail"
    return f"{drink_name} Cocktail"



def categorize_dish(dish_name, dish_ingredients):
    if dish_ingredients.issubset(VEGAN):
        return f"{dish_name}: VEGAN"
    elif dish_ingredients.issubset(VEGETARIAN):
        return f"{dish_name}: VEGETARIAN"
    elif dish_ingredients.issubset(PALEO):
        return f"{dish_name}: PALEO"
    elif dish_ingredients.issubset(KETO):
        return f"{dish_name}: KETO"
    else:
        return f"{dish_name}: OMNIVORE"


def tag_special_ingredients(dish):
    dish_name, dish_ingredients = dish
    
    ingredients_set = set(dish_ingredients)

    special_items = ingredients_set.intersection(SPECIAL_INGREDIENTS)

    return (dish_name, special_items)


# تمرین ۵: تهیه لیست خرید کلی
def compile_ingredients(dishes):
    return set().union(*dishes)


def separate_appetizers(dishes, appetizers):
    dishes_set = set(dishes)
    appetizers_set = set(appetizers)
    
    main_dishes = dishes_set.difference(appetizers_set)
    
    return list(main_dishes)


def singleton_ingredients(dishes, INTERSECTIONS):
    all_ingredients = set().union(*dishes)
    
    singletons = all_ingredients.difference(INTERSECTIONS)
    
    return singletons
