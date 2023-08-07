gender = input("Insert your gender (M/F): ").upper()
weight = int(input("Insert your weight (kg): "))
height = int(input("Insert your height (cm): "))
age = int(input("Insert your age: "))
activity = input("Insert your level of physical activity (sedentary/light/moderate/heavy)").lower()
restrictions = input("Have you got any food preferences or restrictions? ")

calories_m = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
calories_f = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
calories = int((calories_m * (gender == "M")) + (calories_f * (gender == "F")))
activity_factor = float((activity == "sedentary")*1.2 + (activity == "light")*1.35 + (activity == "moderate")*1.5 + (activity == "heavy")*1.7)
tot_calories = float(calories*activity_factor)
print("Your daily calorie requirement is", tot_calories, "kcal a day")

breakfast_quantity=(calories*25)/100
lunch_quantity=(calories*33)/100
dinner_quantity=(calories*27)/100
snacks_quantity=(calories*5)/100

daily_food_plan = print(f"Your daily food plan is:\nBreakfast: {breakfast_quantity} kcal\nLunch: {lunch_quantity} kcal\nDinner: {dinner_quantity} kcal\nSnacks: {snacks_quantity} kcal\nPreferences or restrictions: {restrictions}")

print("Thanks for your time. Have a great day!")