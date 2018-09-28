#class calculate_calories_in_meal:

def add_ingredients(meal):
    total_calorie = 0
    for food in meal:
        total_calorie = total_calorie + food

    return str(total_calorie) + " calories"

apple = 25
grapes = 10
mango = 90

meal = [apple, grapes, mango]

print("calories in meal: ",add_ingredients(meal))