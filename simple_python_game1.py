import random
from random import randint

secret_number = random.randint(1, 100)
print("Я загадал число от 1 до 100, попробуй отгадать :}")

user_number = 0
try_count = 0

while user_number != secret_number:
    try_count += 1
    user_number = int(input(f"{try_count}-я попытка:"))
    if user_number < secret_number:
        print("Маловато")
    elif user_number > secret_number:
        print("борщ")

print("правильно это:", secret_number)