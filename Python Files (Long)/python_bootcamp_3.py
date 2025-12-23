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

# WEEK 5 POST CLASS EXERCISES AND CHALLENGE
# Q1: Ask for n and calculate the sum of all odd numbers from 1 to n
# sum = 0
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     if i % 2 == 1:
#         sum += i
# print("Sum of all odd numbers from 1 to n:",sum)

# Q2: Ask for a number x and print its multiplication table from 1 to 10.
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{i} * {n} = {i*n}")

# Q3: Use a while loop to find the smallest number greater than 0 that is divisible by both 3 and 5.
# n = 1
# while True:
#     if n % 3 == 0 and n % 5 == 0:
#         print(n)
#         break
#     n+=1

# Q4: 
# n = int(input("Enter a number: "))
# while n != 0:
#     print(n)
#     n -= 1
# print("Go")

# Q6: 
# n = int(input("Enter a number: "))
# product = 1
# for i in range(1, n+1):
#     product *= i
# print(product)

# Q7: Ask for a positive integer and print its digits in reverse order using a while loop.
# Solution 1: Use range, but reverse step -1. Starts from len() - 1, ends with -1
# Change the number to a string to loop through the number
# n = int(input("Enter a number (at least 4 digits): "))
# for i in range(len(str(n))-1, -1, -1):
#     print(str(n)[i], end ="")
# 
# Solution 2: Using modulo (%) and integer division (//)
# The opposite of getting the remainder (%) is integer division (//).
# num = int(input("Enter a number (at least 4 digits): "))
# while num > 0:
#     digit = num % 10
#     print(digit, end = "")
#     num //= 10

# Q8: Ask for a word and count how many vowels (a, e, i, o, u) it has.s
# Make a list of vowels, and use 'in'
# vowels = ['a', 'e', 'i', 'o', 'u']
# count = 0
# word = input("Give a word (at least 6 characters): ")
# for char in word:
#     if char in vowels:
#         count += 1
# print("Vowels in word:", count) 

# Q9: Ask for a positive integer n. Repeat these rules until n becomes 1:
#  If n is even, divide by 2. If n is odd, multiply by 3 and add 1. Count how many steps it takes
# n = int(input("Enter a number: "))
# count = 0
# while n != 1:
#     if n % 2 == 0:
#         # Interger division. Normal division in python results in an float
#         n //= 2
#     else:
#         n = n * 3 + 1
#     count += 1
# print(f"Took {count} steps")

# WEEK 6 INCLASS EXERCISES AND CHALLENGE
# Q2
# for i in range(1, 10+1):
#     if i == 3:
#         continue
#     print(i, end = " ")

# Q3
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1, n + 1):
#     sum += i
#     if sum >= 50:
#         break
#     print(i, end = " ")

# Q5: Use nested loops to print a multiplication table from 1 to 3.
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i}x{j}={i*j}", end = " ")
#     print("")

# Q6:
# name = input("Enter name: ")
# while name.lower() != "exit":
#     if name != "":
#         print(name)
#     name = input("Enter name: ")

# Q7:
# for i in range(5):
#     n = int(input("Enter an integer: "))
#     if n % 2 == 0:
#         break

# Q8
# Outer loop: row. Inner loop: row
# for i in range(5):
#     for j in range(5):
#         print("*", end = '')
#         if j == i:
#             break
#     print("")

# Q9
# for i in range(1, 6):
#     if i == 3:
#         continue
#     for j in range(1, 9):
#         print(f"{i}x{j}={i*j}", end = " ")
#     print("")

# WEEK 6 POST CLASS EXERCISES AND CHALLENGE

# Q3
# for i in range(1, 101):
#     # is_integer() is a method to check float
#     if (i**0.5).is_integer():
#         print(i)
#         break

# Q7:
# for i in range(1, 4):
#     for j in range(1, 4):
#         if (i+j) % 2 == 0:
#             continue
#         print(i, j)

# WEEK 7 INCLASS EXERCISES AND CHALLENGE
# Q1
# def greet_name(name):
#     print(f"Welcome {name}!")
# name = input("Enter name: ")
# greet_name(name)

# Q4
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# num = int(input("Give me an integer: "))
# print("Even") if is_even(num) else print("Odd")

# Q5
# def formatted_name(first, last):
#     # Python name can be concatenated like this
#     name = last + ", " + first
#     return name
# first = input("Enter first name: ")
# last = input("Enter last name: ")
# print(formatted_name(first, last))

# Q8
# def count_chars(text):
#     count = len(text)
#     return count
# text = input("> ")
# print(count_chars(text))

# Q11
# def is_prime(n):
#     # Number has to be bigger than 1. 1 is a prime number
#     if n <= 1:
#         return False
#     # Number has to be divided by numbers smaller than itself
#     for i in range(2, n):
#         if n % i == 0:
#             return True
#     return False
# num = int(input("Give me an integer: "))
# print(is_prime(num))

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

# Q: Count the digits in a number
# num = 88888888555
# digit_count = {}
# for d in str(num):
#     digit_count[d] = digit_count.get(d, 0) + 1
# print(digit_count)





