def shake_calories(shake):
    total_cal = 0
    for item in shake:
        total_cal = total_cal + item

    return 'Calories in shake is: ' + str(total_cal)

peanut_butter = 315
milk = 150
bananas = 90
kale = 5
beets = 50
mango = 90
apples = 25
water = 0

Peanut_Shake = [peanut_butter, milk, bananas]
Kale_Smoothie = [kale, beets, mango, apples, water]

print("Peanut Butter Shake has: " + shake_calories(Peanut_Shake) + " calories")
print("Peanut Butter Shake has: " + shake_calories(Kale_Smoothie) + " calories")