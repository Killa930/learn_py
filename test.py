# print("Hello, World!")

# input()

# number = 5
# print(number)

# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))

# num1 += 5

# print("Result:", num1 + num2)
# print("Result:", num1 - num2)
# print("Result:", num1 / num2)
# print("Result:", num1 ** num2)
# print("Result:", num1 // num2)

# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))

# num1 *= 5

# print("Result:", num1 + num2)
# print("Result:", num1 - num2)
# print("Result:", num1 / num2)
# print("Result:", num1 ** num2)
# print("Result:", num1 // num2)

# word = "Hi" #String

# print(word * 5)

# word = True #Boolean


# IF;ELIF;ELSE

# if 5 == 5 :
#     print("Yes it is true")

# sk = 0
# while sk < 10:
#     user_data = int(input("Enter a number: "))
    
#     if user_data > 5:
#         print("The number is bigger than 5")
#     elif user_data == 5:
#         print("The number is equal to 5")
#     else:
#         print("the number is smaller than 5")
#     sk += 1


# isHappy = str(input("Are you happy? (yes/no): "))

# if isHappy == "yes":
#     print("I am happy")
# else:
#     print("I am not happy")

# user_data = int(input("Enter a number: "))

# isHappy = True

# if isHappy and user_data == 6:
#     print("I am happy and the number is 6")
# elif user_data == 5:
#     print("The number is 5")
# elif user_data == 7:
#     print("The number is 7")
# else:
#     print("User unhappy")

# TERNARY OPERATOR

# data = input()

# number = 5 if data == "Five" else 0 # В одну строку пишем

# # if data == "Five":
# #     number = 5
# # else:
# #     number = 0

# print(number)


# LOOPS(FOR, WHILE)

# for i in range(1, 6, 2):
#     print(i)


# count = 0
# word = "Hello Bitch"
# for i in word:
#     if i == "h":
#         count += 1

# print(count)

# for i in range(11):
#     if i == 5:
#         break
#     if i % 2 == 0:
#         continue
#     print(i)

# found = None

# for i in "hello":
#     if i == "l":
#         found = True
#         break
# else:
#     found = False

# print(found)



# i = 5
# while i < 15:
#     print(i)
#     i += 2



# i = 5

# isHasCar = True

# while isHasCar:
#     print(i)
#     i += 1


# isHasCar = True

# while isHasCar:
#     if input("Enter data:") == "Exit":
#         isHasCar = False

#LISTS

# nums = [5, 4, 3, 5, 7, 8, 7, True, "Hello", 5.5,[1, 2, 3]]

# nums[0] = 50
# nums[5] = 11

# print(nums[0])
# print(nums[5])
# print(nums[-1][0])


# numbers = [5, 2, 3]
# # numbers[3] =  100

# numbers.append(100)
# numbers.insert(1, 200)

# b = [1, 2, 3]
# numbers.extend(b)
# # numbers.reverse()
# numbers.sort()
# numbers.pop(-2)
# numbers.remove(2)

# # numbers.clear()

# # print(numbers.count(3))
# print(len(numbers))

# nums = [5, 2, 7, "ello", False]

# for el in nums:
#     el *= 2
#     print(el)

# n = int(input("Enter length of list: "))

# user_list = []

# # i = 0

# # while i < n:
# #     string = "Enter element #" + str(i + 1) + ": "
# #     user_list.append(input(string))
# #     i += 1

# for i in range(n):
#     string = "Enter element #" + str(i + 1) + ": "
#     user_list.append(input(string))
#     i += 1

# print(user_list, i)

# Indexing (slicing & strides)

# word = 'Football,basketball,volleyball'

# # # print(word.count('r'))
# # # print(word.capitalize())
# # # print(word.find('pro'))

# hobby = word.split(',')

# for i in range(len(hobby)):
#     hobby[i] = hobby[i].capitalize()

# print(hobby)




# numbers = [
#     951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
#     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
#     743, 527
# ]

# for number in numbers:
#     if number == 237:
#         break
#     if number % 2 == 1:
#         continue
#     print(number)


# word = "Football"

# print(word[1:-1:2])

# lis = [6, 7, "Stroka", True, 6.5]


# print(lis[2:5:2])

#TUPLES

# data = (4, 5, 7, 2, 3,)

# # print(data[1:4])

# # for i in range(len(data)):
# #     print(data[i])

# for el in data:
#     print(el)

# nums = [5, 7, 8]

# new_data = tuple(nums)
# word = "Hello world"
# print(tuple(word))

