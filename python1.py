import random
"""
try:
    int(input("test."))
except ValueError:
    print("you got value ValueError")
"""

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

numbers = [num1, num2, num3, num4]

choice = random.choice(numbers)
print(choice)
