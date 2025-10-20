# Project: Daily Calorie Tracker

# Name: Tarun Sharma

# Admission number: 2501010034

# course: Btech CSE

# Task 1: Setup & Introduction
print("Welcome to the Daily Calorie Tracker!")
print("This simple program helps you record meals and calories, then checks if you are within your daily limit.")
print()

# Task 2: Input Data Collection
meals = []
calories = []

num_meals = int(input("How many meals did you have today? "))

for i in range(num_meals):
    print()
    meal_name = input(f"Enter name of meal {i+1}: ")
    calorie = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(calorie)

print()

# Task 3: Calorie Calculations
total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("Enter your daily calorie limit: "))
print()

# Task 4: Exceed Limit Warning System
if total_calories > daily_limit:
    print("Warning: You have exceeded your daily calorie limit!")
else:
    print("Good job! You are within your daily calorie limit.")

print()

# Task 5: Neatly Formatted Output
print("----------- Daily Calorie Summary -----------")
print("Meal Name\tCalories")


for i in range(len(meals)):
    print(f"{meals[i]}\t\t{calories[i]}")
print("---------------------------------------------")

print(f"Total\t\t{total_calories}")
print(f"Average\t\t{average_calories:.2f}")
