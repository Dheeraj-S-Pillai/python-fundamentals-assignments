# Python Assignment 3 While Loop, For Loop and Functions


# 1. Number Guessing Game

import random

secret_number = random.randint(1, 10)
attempts = 3
count = 0

while count < attempts:
    guess = int(input("Guess the number (between 1 and 10): "))

    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue

    count += 1

    if guess > secret_number:
        print("Too high. Try again.")
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break
else:
    print("Better luck next time!")


# 2. Multiplication Table Generator

number = int(input("Enter the number for the multiplication table: "))

for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)


# 3. FUNCTION - BMI Calculator

def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print("BMI is:", round(bmi, 2))
