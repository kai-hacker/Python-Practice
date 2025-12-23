# Week 4 inclass exercises & challenge

# Q9
# age = 14
# if 13 <= age <= 19:
#     print(age)

# Q1
# num = float(input("Give me a number: "))
# if num > 0:
#     print("The number is positve: ")
# elif num == 0:
#     print("The number is 0")
# else: 
#     print("The number is negative")

# Q2
# num = int(input("Give me an integer: "))
# if num % 2 == 0:
#     print("This number is an even number")
# else:
#     print("This number is an odd number")

# Q3
# age = int(input("Give me your age: "))
# if age < 13:
#     print("You are a child")
# elif age < 20:
#     print("You are a teen")
# else: 
#     print("You are an adult")

# Q4
# year = int(input("Enter a year: "))
# if year % 4 == 0:
#     print(f"{year} is a leap year")

# Q5
# Syntax if - else to print using 1 line
# print("x is positive") if x > 0 else print("x is zero or negative")
# amount = float(input("Enter the purchased amount: "))
# print("You get a discount") if amount > 50000 else print("No discount!")

# Q6
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# print(max(num1, num2), "is larger")

# Q7: Grade Evaluator
# grade = int(input("Enter your grade (0 - 100): "))
# if grade >= 90:
#     print("Excellent")
# elif grade >= 80:
#     print("Good")
# elif grade >= 50:
#     print("Average")
# else:
#     print("Fail")

# Q8
# hour = int(input("Enter hour (0 - 23): "))
# if 5 <= hour <= 11:
#     print("Morning")
# elif hour < 18:
#     print("Afternoon")
# elif hour < 22:
#     print("Evening")
# else: 
#     print("Night")

# Q10
# stored = "python123"      
# pw = input("Enter pw: ")
# while pw != stored:
#     print("Access denied")
#     pw = input("Enter pw: ")
# print("Access granted")

# Week 4 inclass exercises & challenge

# Q10 Strong password checker
# pw = input("Enter your password: ")
# # Use 'in' in python: any(i in string for i in [... , ...])
# # in Python, 0 is falsy, 1 is truthy
# if len(pw) >= 8 and any(special_char in pw for special_char in ['@' , '#']) : 
#     print("Strong pw")
# else: 
#     print("Weak pw")

# Q1 absolute value
# num = int(input("Enter a number: "))
# print("Absolute Value:", abs(num))

# Q2: Compare 3 numbers
# Solution 1: Compare the first two → keep the larger. Compare the result with the third. Better for not many variables
# Solution 2: Put them in a list. 
# Solution 3: Compare with max
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))
# largest = None
# if num1 >= num2:
#     largest = num1
# else: 
#     largest = num2
# if num3 >= largest: 
#     largest = num3
# print("Largest:", largest)

# Q3: 
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# if a % b == 0:
#     print(f"{a} is divisible by {b}")
# else: 
#     print("Not divisible")

# Q4:
# if x in [..., ...]
# month = int(input("Enter month (1-12): "))
# if month in [1, 3, 5, 7, 8, 10, 12]: 
#     print("31 days") 
# elif month in [4, 6, 9, 11]: 
#     print("30 days")
# else: 
#     print("28 or 29 days") 

# Q6:
# sides = int(input("Number of the sides of the shape: "))
# if sides == 3:
#     print("Triangle")
# elif sides == 4:
#     print("Square")
# elif sides == 5:
#     print("Pentagon")
# else:
#     print("Unknown shape")

# Q8
# hour = int(input("Enter hour (0 - 23): "))
# if 5 <= hour <= 11:
#     print("Good Morning")
# elif hour < 18:
#     print("Good Afternoon")
# elif hour < 22:
#     print("Good Evening")
# else: 
#     print("Good Night")

# Q9
# color = input("Give me a color (red, green, yellow): ").strip()
# if color == "red":
#     print("Stop")
# elif color == "green":
#     print("Go")
# elif color == "yellow":
#     print("Ready")
# else:
#     print("Invalid color")

# WEEK 5 INCLASS EXERCISES AND CHALLENGE
# Q1:
# for i in range(1, 11):
#     print(i, end = " ")

# Q3:
# n = int(input("Gives a number 'n': "))
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("Sum:", sum)

# Q4:
# word = input("Word: ")
# num = int(input("Number: "))
# for i in range(num):
#     print(word, end = " ")

# Q8:
# for i in range(1, 6):
#     print(f"{i} → {i**2}")

# Q10
# sum = 0
# num = int(input("Enter number (not 0): "))
# while num != 0:
#     sum += num
#     num = int(input("Enter number (not 0): "))
# print("Sum:", sum)


# W3resource Python basic part 2    

# Q1: Write a Python function that takes a sequence of numbers and determines 
# whether all the numbers are different from each other.
# 
# Strategy 1: Compare size before and after removing duplicates
# Pros:
# Very concise and readable
# Easy to reason about
# Works well for small inputs
# Cons:
# You must process the entire sequence, even if a duplicate appears early
# Requires creating a new data structure containing all unique values
# Slightly more memory usage
# 
# values = []
# num = float(input("Enter a number: "))
# while num != -1: 
#     values.append(num) 
#     num = float(input("Enter a number: "))
# print(values)
# def check_all_uniques(values):
#     # Create a list of uniques
#     uniques = []
#     # Each value of i will be the value of an element in the 'values' list
#     # The check, by default, is true
#     for i in values:
#         if i not in uniques:
#             uniques.append(i)
#     return True if len(values) == len(uniques) else False
# check = check_all_uniques(values)
# if check:
#     print("All values are unique")
# else:
#     print("Got duplicates")    
# 
# Strategy 2: Check while looping. Go through the sequence one element at a time
# Keep track of values you’ve already encountered
# The moment you see a value twice, you already know the answer
# 
# Strategy 3: Create an empty list. As soon as there is a duplicate, stops and conclude
# that not all the numbers are different
# Avoid using "list" as a variable name
# Pros: 
# It can terminate early, saving time
# It avoids unnecessary work when duplicates exist
# It scales better for large inputs
# It reflects how many real-world algorithms are optimized (fail fast)
# Empty list to take in all the inputs
# values = []
# num = float(input("Enter a number: "))
# while num != -1: 
#     values.append(num) 
#     num = float(input("Enter a number: "))
# print(values)
# 
# def check_all_uniques(values):
#     # Create a list of uniques
#     uniques = []
#     # Each value of i will be the value of an element in the 'values' list
#     # The check, by default, is true
#     for i in values:
#         if i not in uniques:
#             uniques.append(i)
#         else:
#             # For a function with loop, could use "return False" to end the function once finished
#             # Instead of "break"
#             return False
#     return True
# 
# check = check_all_uniques(values)
# if check:
#     print("All values are unique")
# else:
#     print("Got duplicates")
# Check for False in python: if not check, if check == False, if check if False (advanced & not recommended)

# Q2: Write a Python program that creates all possible strings 
# using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.
# Permutations
# Below is keeping the order & not switchin elements positions
# Not done

# def all_possible_aeioI():
#     # put all the letters in a list
#     letters = ['a', 'e', 'i', 'o', 'I']
#     # Empty list of the words to be created
#     words = []
#     # Create a loop, for each iteration a unique letter will start
#     for i in range(len(letters)):
#         # re-create the copy at the start of every iteration ['a', 'e', 'i', 'o', 'I']
#         copy = letters.copy()
#         # After the 1st loop, change the 1st letter
#         if i != 0:
#             # temp = copy[0]
#             # copy[0] = copy[i]
#             # copy[i] = temp
#             # Use python switch syntax for quicker switch
#             copy[0], copy[i] = copy[i], copy[0]
#             # separator.join(iterable_of_strings))
#         # The 1st word at the start of the iteration
#         # The inside loop iterates through the 4 remaining elements
#         # The number of iterations is 1 less than the length of the list
#         for j in range(len(copy) - 1):
#             word = ''.join(copy)
#             words.append(word)
#             copy.append(copy[1])
#             copy.pop(1)
#     print(len(words))
#     print(words)

# all_possible_aeioI()





