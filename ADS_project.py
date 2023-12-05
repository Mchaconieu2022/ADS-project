import pandas as pd
import random
import openpyxl

# Caloric Intake Table
caloric_intake_table = pd.read_excel("caloric_intake.xlsx")

# PCF Ratio Table
pcf_ratio_table = pd.read_excel("pcf_ratio.xlsx")

# Meals Table
meals_table = pd.read_excel("nutrition.xlsx")


def calculate_daily_calories(age, sex, activity_level):
    if age >= 15 and age <= 18:
        if sex == "M":
            if activity_level.lower() == "sedentary":
                caloric_intake = caloric_intake_table.loc[0, 'Sedentary']
            elif activity_level.lower() == "moderately active":
                caloric_intake = caloric_intake_table.loc[0, 'Moderately Active']
            else:
                caloric_intake = caloric_intake_table.loc[0, 'Active']
        else:
            if activity_level.lower() == "sedentary":
                caloric_intake = caloric_intake_table.loc[1, 'Sedentary']
            elif activity_level.lower() == "moderately active":
                caloric_intake = caloric_intake_table.loc[1, 'Moderately Active']
            else:
                caloric_intake = caloric_intake_table.loc[1, 'Active']

    elif age >= 19 and age <= 30:
        if sex == "M":
            if activity_level.lower() == "sedentary":
                caloric_intake = caloric_intake_table.loc[2, 'Sedentary']
            elif activity_level.lower() == "moderately active":
                caloric_intake = caloric_intake_table.loc[2, 'Moderately Active']
            else:
                caloric_intake = caloric_intake_table.loc[2, 'Active']
        else:
            if activity_level.lower() == "sedentary":
                caloric_intake = caloric_intake_table.loc[3, 'Sedentary']
            elif activity_level.lower() == "moderately active":
                caloric_intake = caloric_intake_table.loc[3, 'Moderately Active']
            else:
                caloric_intake = caloric_intake_table.loc[3, 'Active']

    elif age >= 31 and age <= 50:
        if sex == "M":
            if activity_level.lower() == "sedentary":
                caloric_intake = caloric_intake_table.loc[4, 'Sedentary']
            elif activity_level.lower() == "moderately active":
                caloric_intake = caloric_intake_table.loc[4, 'Moderately Active']
            else:
                caloric_intake = caloric_intake_table.loc[4, 'Active']
        else:
            if activity_level.lower() == "sedentary":
                caloric_intake = caloric_intake_table.loc[5, 'Sedentary']
            elif activity_level.lower() == "moderately active":
                caloric_intake = caloric_intake_table.loc[5, 'Moderately Active']
            else:
                caloric_intake = caloric_intake_table.loc[5, 'Active']

    else:
        if sex == "M":
            if activity_level.lower() == "sedentary":
                caloric_intake = caloric_intake_table.loc[6, 'Sedentary']
            elif activity_level.lower() == "moderately active":
                caloric_intake = caloric_intake_table.loc[6, 'Moderately Active']
            else:
                caloric_intake = caloric_intake_table.loc[6, 'Active']
        else:
            if activity_level.lower() == "sedentary":
                caloric_intake = caloric_intake_table.loc[7, 'Sedentary']
            elif activity_level.lower() == "moderately active":
                caloric_intake = caloric_intake_table.loc[7, 'Moderately Active']
            else:
                caloric_intake = caloric_intake_table.loc[7, 'Active']
    return caloric_intake


def calculate_macronutrient_ratios(age, activity_level):
    if age >= 15 and age <= 18:
        if activity_level.lower() == "sedentary":
            protein = pcf_ratio_table.loc[0, 'SEDENTARY (Protein)']
            carbs = pcf_ratio_table.loc[0, 'SEDENTARY (Carbs)']
            fats = pcf_ratio_table.loc[0, 'SEDENTARY (Fats)']
        elif activity_level.lower() == "moderately active":
            protein = pcf_ratio_table.loc[0, 'MODERATELY ACTIVE (Protein)']
            carbs = pcf_ratio_table.loc[0, 'MODERATELY ACTIVE (Carbs)']
            fats = pcf_ratio_table.loc[0, 'MODERATELY ACTIVE (Fats)']
        else:
            protein = pcf_ratio_table.loc[0, 'ACTIVE (Carbs)']
            carbs = pcf_ratio_table.loc[0, 'ACTIVE (Carbs)']
            fats = pcf_ratio_table.loc[0, 'ACTIVE (Carbs)']

    elif age >= 19 and age <= 30:
        if activity_level.lower() == "sedentary":
            protein = pcf_ratio_table.loc[1, 'SEDENTARY (Protein)']
            carbs = pcf_ratio_table.loc[1, 'SEDENTARY (Carbs)']
            fats = pcf_ratio_table.loc[1, 'SEDENTARY (Fats)']
        elif activity_level.lower() == "moderately active":
            protein = pcf_ratio_table.loc[1, 'MODERATELY ACTIVE (Protein)']
            carbs = pcf_ratio_table.loc[1, 'MODERATELY ACTIVE (Carbs)']
            fats = pcf_ratio_table.loc[1, 'MODERATELY ACTIVE (Fats)']
        else:
            protein = pcf_ratio_table.loc[1, 'ACTIVE (Carbs)']
            carbs = pcf_ratio_table.loc[1, 'ACTIVE (Carbs)']
            fats = pcf_ratio_table.loc[1, 'ACTIVE (Carbs)']

    elif age >= 31 and age <= 50:
        if activity_level.lower() == "sedentary":
            protein = pcf_ratio_table.loc[2, 'SEDENTARY (Protein)']
            carbs = pcf_ratio_table.loc[2, 'SEDENTARY (Carbs)']
            fats = pcf_ratio_table.loc[2, 'SEDENTARY (Fats)']
        elif activity_level.lower() == "moderately active":
            protein = pcf_ratio_table.loc[2, 'MODERATELY ACTIVE (Protein)']
            carbs = pcf_ratio_table.loc[2, 'MODERATELY ACTIVE (Carbs)']
            fats = pcf_ratio_table.loc[2, 'MODERATELY ACTIVE (Fats)']
        else:
            protein = pcf_ratio_table.loc[2, 'ACTIVE (Carbs)']
            carbs = pcf_ratio_table.loc[2, 'ACTIVE (Carbs)']
            fats = pcf_ratio_table.loc[2, 'ACTIVE (Carbs)']

    else:
        if activity_level.lower() == "sedentary":
            protein = pcf_ratio_table.loc[3, 'SEDENTARY (Protein)']
            carbs = pcf_ratio_table.loc[3, 'SEDENTARY (Carbs)']
            fats = pcf_ratio_table.loc[3, 'SEDENTARY (Fats)']
        elif activity_level.lower() == "moderately active":
            protein = pcf_ratio_table.loc[3, 'MODERATELY ACTIVE (Protein)']
            carbs = pcf_ratio_table.loc[3, 'MODERATELY ACTIVE (Carbs)']
            fats = pcf_ratio_table.loc[3, 'MODERATELY ACTIVE (Fats)']
        else:
            protein = pcf_ratio_table.loc[3, 'ACTIVE (Carbs)']
            carbs = pcf_ratio_table.loc[3, 'ACTIVE (Carbs)']
            fats = pcf_ratio_table.loc[3, 'ACTIVE (Carbs)']

    micronutrients = [protein, carbs, fats]
    return micronutrients


def generate_meal_baskets(age, sex, activity_level):
    # Calculate daily caloric intake
    daily_calories = calculate_daily_calories(age, sex, activity_level)

    # Calculate macronutrient ratios
    pcf_ratios = calculate_macronutrient_ratios(age, activity_level)

    # Initialize meal baskets
    meal_basket_1 = []

    caloric_counter = 0

    # Iterate through meals table and add meals to meal baskets
    for index, row in meals_table.iterrows():
        # Calculate macronutrient content per meal
        meal_protein = row["Protein(g)"]
        meal_carbs = row["Carbs(g)"]
        meal_fat = row["Fat(g)"]

        # Calculate percentage of daily caloric intake for each macronutrient
        if abs(meal_protein / (meal_protein + meal_carbs + meal_fat) - pcf_ratios[0]) < 0.1 and abs(meal_carbs / (meal_protein + meal_carbs + meal_fat) - pcf_ratios[1]) < 0.1 and abs(meal_fat / (meal_protein + meal_carbs + meal_fat) - pcf_ratios[2]) < 0.1:
            if random.random() < 0.5:
                meal_basket_1.append(row)
                caloric_counter = caloric_counter + meal_protein * 4 + meal_carbs * 4 + meal_fat * 9
                if caloric_counter >= daily_calories:
                    return meal_basket_1


# Get user input
age = int(input("Enter your age: "))
sex = input("Enter your sex (M/F): ")
activity_level = input("Enter your activity level (Sedentary, Moderately Active, Active): ")

# Generate meal baskets
meal_basket_1 = generate_meal_baskets(age, sex, activity_level)

# Print meal baskets
print("Meal Basket 1: ", meal_basket_1)