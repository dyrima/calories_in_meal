def shake_calories(shake):
    total_cal = 0
    for item in shake:
        total_cal = total_cal + item

    return 'Calories in shake is: ' + str(total_cal)

peanut_butter = 315
milk = 150
bananas = 90

Shake = [peanut_butter, milk, bananas]

print("Peanut Butter Shake has: " + shake_calories(Shake) + " calories")