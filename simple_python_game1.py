import random
from random import randint

secret_number = random.randint(1, 100)
print("Я загадал число от 1 до 100, попробуй отгадать :}")

try_count = 0

while True:

    user_number = input("введите число: ")

    if user_number == '':
        print("Вы ничего не ввели")
        continue

    is_number = True
    for i in user_number:
        if i not in "0123456789":
            is_number = False
            break


    if is_number == False:
        print("Нужно целое число!")
        continue

    guess = int(user_number)
    try_count += 1



    if guess < secret_number:
        print("Маловато")
    elif guess > secret_number:
        print("борщ")
    else:
        print(f"Поздравляем вы отгадали число {secret_number} за {try_count} попыток")

