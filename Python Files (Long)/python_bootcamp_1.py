# Sample test question 1

# last_name = input("Enter your last name: ")
# birth_year = int(input("Enter your birth year: "))
# print("Input:")
# print(f"Last Name: {last_name}")
# print(f"Birth Year: {birth_year}")
# alias = last_name + str(birth_year)[2:]
# print("Output:")
# print(f"{alias}")

# Sample test question 2

# time_stamp = input("Enter time in HHMMSSDDD format: ")
# print(f"{time_stamp[0:2]}:{time_stamp[2:4]}:{time_stamp[4:6]}-{time_stamp[6:]}")

# Sample test question 3

# number = input("Enter a positive integer: ")
# print(number[:2] + "*" * len(number[2:-4])+ number[-4:])

# Sample test question 4

# import math
# decimal = int(input("Enter the number of decimal of pi to display: "))
# print(f'{math.pi:.{decimal}f}')

# Sample test question 5

# name = input("Enter full name: ")
# first_space_index = name.find(" ")
# last_name = name[:first_space_index]
# first_name = name[first_space_index + 1:]
# print(f"{first_name} {last_name}")

# Practice question

# sentence = input("Enter a sentence: ")
# print(sentence.title())

# Practice start, stop, step print the 1st, 3rd and 5th characters of a word

# x = "banana"
# print(x[0:6:2])

# Add 5 spaces between 2 words with *

# word1 = "Hi"
# word2 = "Ass"
# statement = word1 + " " * 5 + word2
# print(f"{statement:>35}")

# Format text

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# email = first_name + "." + last_name + "@example.com"
# print(email.lower())

# Print final 4 characters

# x = input("Enter any statement: ")
# print(x[-4:])

# x = input("Enter any statement: ")
# print(x[:2])
# print(x[-4:])
# print(len(x[2:-4])*"A")

# grade = ""
# for i in range(5):
#     mark = int(input("Enter mark: "))
#     if mark < 50:
#         grade = "NN"
#     elif mark < 60:
#         grade = "PA"
#     elif mark < 70:
#         grade = "CR"
#     elif mark < 80:
#         grade = "DI"
#     else:
#         grade = "HD"
#     print(f"Grade is {grade}")

# number = 5
# guess = int(input("Guess the number that I am thinking of: "))
# while True: 
#     if guess == number:
#         print("Correct!")
#         break
#     else:
#         guess = int(input("Guess again..."))

# while True:
#     mark = int(input("Enter mark: "))
#     if mark < 50:
#         print("Grade is NN")
#     elif mark < 60:
#         print("Grade is PA")
#     elif mark < 70:
#         print("Grade is CR")
#     elif mark < 80:
#         print("Grade is DI")
#     elif mark <= 100:
#         print("Grade is HD")
#     else:
#         break

# while True:
#     num_x = int(input('How many times should I print the letter X? ')) 
#     to_print = ''
#     if num_x <= 0:
#         break
#     to_print = 'X' * num_x
#     print(to_print)

# Initialize a list of 10 zeros
# list = [0] * 10
# for i in range(len(list)):
#     list[i] = int(input("Enter a number to add to a list:"))
# largest_odd = None
# for num in list:
#     if (num % 2) == 1 and (largest_odd is None or num > largest_odd):
#         largest_odd = num
# if largest_odd is not None:
#     print(f"The largest odd number is: {largest_odd}")
# else:
#     print("There are no odd numbers in the list.")

# for i in range (2, 21, 2):
#     if i % 2 == 0:
#         print(i)

# x = int(input("> "))
# while x != 0:
#     print(x)
#     x = x - 1
# print("Blast off!")

# num = int(input("Enter a positive integer: "))
# sum = 0
# for i in range(1, num + 1):
#     if i % 2 == 1:
#         sum += i
# print(f"The sum of odd numbers from 1 to {num} is: {sum}")

# sum = 0
# for i in range(2, 1000):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     # The loop needs to go from i to the number right before it. If the loop does not, i will not be a prime
#     # If the loop did not break, not even once through all iterations, than else statement will be executed
#     else:
#         sum += i
# print(f"The sum of all prime numbers from 2 to below 1000 is: {sum}")

#clock
# import time
# for i in range(12):
#     for j in range(60):
#         print(f"{i:02}:{j:02}")
#         time.sleep(1)

# Find position of character without using find()
# count = 0
# for i in "appearance":
#     if i == "c":
#         print(count)
#         break
#     count+=1

# while True:
#     num = input("> ")
#     if not num.lstrip("-").isdigit():
#         print("Please enter a valid integer.")
#         continue 
#     num = int(num)
#     print(num)
#     if num < 0: 
#         break

# for i in range(5):
#     pass

# for i in range(5):
#     num = int(input("> "))
#     if num % 2 == 0:
#         print(num)
#         break

# for i in range(1,6):
#     if i == 3:
#         continue
#     print(i)

# for i in range (1,21):
#     if i % 4 == 0:
#         continue
#     print(i)

# for j in range(1,6):
#         print("*" * j)

# for i in range(1, 6):        # Outer loop: number of rows
#     for j in range(i):       # Inner loop: number of stars in each row
#         print("*", end="")   # End without new line. 1st iteration print 1 star 2nd - 2 stars, etc.s
#     print()                  # Move to the next line

# num = 1
# while True:
#     if num % 4 == 0 and num % 6 == 0:
#         print(num)
#         break
#     num += 1

# for i in range(1,8):
#     for j in range(1,5):
#         if i * j > 12:
#             break
#         print(i, j)
#     if i * j > 12:
#         break