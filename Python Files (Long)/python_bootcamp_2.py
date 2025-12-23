# From lesson 7 & assignment 2
# Q1
# def function(a,b):
#     return a + b

# Q2
# def count_char(x):
#     count = 0
#     for char in x:
#         count += 1
#     return count
# text = input("Enter some text: ")
# print(count_char(text))

# Q3
# num = int(input("Enter an integer: "))
# if (num % 3 == 0 and num % 5 == 0):
#     print(f"{num} is divisible by both")
# elif (num % 5 == 0):
#     print(f"{num} is divisible by 5")
# elif (num % 3 == 0):
#     print(f"{num} is divisible by 3")
# else:
#     print(f"{num} is not divisible")


# Q4
# Q: Write a Python program that reads two positive integers n and m, then print all integers between them whose digits are all odd.

# Solution 1
# def find_numbers (x,y):
#     if (x < 0 or y < 0):
#         return print("x or y is not positive")
#     list = []
#     # Loops through every number between the 2 inputs
#     for i in range (x, y+1):
#         # If the number between x and y is a single digit number
#             if i < 10: 
#                 if i % 2 == 1:
#                     list.append(i)
#         # If the number between x and y is 10 or above
#             else:
#                 # Loop through each digit in the number. 
#                 # 2 digits > 2 j values, etc.
#                 for j in range(len(str(i))):
#                     #  If a digit is found to be even, break the loop
#                      if int(str(i)[j]) % 2 == 0:
#                           break
#                     # If j makes it to the last digit and it's odd, append the number to the list 
#                      if j == len(str(i)) - 1 and int(str(i)[j]) % 2 == 1:
#                           list.append(i)
#     return list
# first_num = int(input("Enter first positive integer: "))
# second_num = int(input("Enter second positive integer: "))
# list = find_numbers(first_num, second_num)
# for i in list: 
#     print(i, end=" ")

# Solution 2
# Split the problem into 2 functions
# When there are 2 things to look for, write the function to look for the easier one
# def has_all_odd_digits(num):
#     # """Check if all digits in the number are odd"""
#     # Check for 1 even digit is easier than checking for all even digits
#     for digit in str(num):
#         if int(digit) % 2 == 0:  # If any digit is even
#             # return false instead of break
#             return False 
#     return True
# def find_all_odd_digit_numbers(n, m):
#     """Find all numbers between n and m whose digits are all odd"""
#     # Do not know in advance which number is smaller. So have to compare
#     start = min(n, m)
#     end = max(n, m)
    
#     result = []
#     for num in range(start, end + 1):
#         if has_all_odd_digits(num):
#             result.append(num)
    
#     return result
# # Main program
# n = int(input("Enter first positive integer: "))
# m = int(input("Enter second positive integer: "))
# numbers = find_all_odd_digit_numbers(n, m)
# if numbers:
#     print("Numbers with all odd digits:", " ".join(map(str, numbers)))
# else:
#     print("No numbers found with all odd digits")

# Q5
# Q3, sample assignment 3
# Given a list of integers. Write a Python program that prints all ordered pairs (i, j) such that:
# i < j, values[i] == values[j]

# list = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
# # i starts from the 1st number to the last number
# for i in range(len(list) - 1):
#     for j in range(i + 1, len(list)):
#         if list[i] == list[j]:
#             print(f"{i, j}")


# Q6
# Q4, sample assignment 3
# Write a function named sum_of_unique_digits that takes a positive integer n and returns the sum of the digits 
# that appear exactly once in n or returns -1 if there’s no such digits in n

# def sum_of_unit_digits(n):
#     sum = 0
#     digits_list = [int(d) for d in str(n)]
#     for i in digits_list:
#         if digits_list.count(i) == 1:
#             sum += i
#     if sum == 0:
#         return -1
#     return sum
# print(sum_of_unit_digits(4334))


# Q7
# Q5, sample assignment 3
# Write a function named investment_growth_streak that takes this list and returns the length of the longest 
# consecutive period during which the daily percentage changes strictly increase from one day to the next.
# OR find the length of the longest increasing sub-sequence in a list.

# solution 1
# def investment_growth_streak (daily_growth):
#     if len(daily_growth) == 0:
#         return 0
#     else: 
#         streak = []
#         for i in range(len(daily_growth)-1):
#             count = 1
#             for j in range(i, len(daily_growth)-1):
#                 if (daily_growth[j+1] <= daily_growth[j]):
#                     break
#                 count += 1
#             streak.append(count)
#         max = streak[0]
#         for k in range(1, len(streak)):
#             if streak[k] > max:
#                 max = streak[k]
#         return max
# daily_growth = []
# print(investment_growth_streak (daily_growth))

# solution 2:
# def investment_growth_streak(daily_changes):
#     if len(daily_changes) = 0:
#         return 0
#     max_streak = 1
#     current_streak = 1    
#     for i in range(len(daily_changes) - 1):
#         if daily_changes[i + 1] > daily_changes[i]:
#             current_streak += 1
#             max_streak = max(max_streak, current_streak)
#         else:
#             current_streak = 1
#     return max_streak

# Q8 
# Write a program that examines three variables— x, y, and z—and prints the largest 
# odd number among them. If none of them are odd, it should print the smallest value of the three. 

# solution 1
# x = 5
# y = 15
# z = 12
# # if none are odd, print min
# if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
#     print(min(x, y, z))
# else:
#     # Declare max = 0 (assumes min value = 0)
#     max = 0
#     # Loop through and see which one can be max
#     list = [x, y ,z]
#     for i in list:
#         if i % 2 == 1 and i > 0:
#             max = i
#     print(max)

# solution 2
# x = 8
# y = 12
# z = 12
# list = [x, y, z]
# odds = []
# for i in list:
#     if i % 2 == 1:
#         odds.append(i)
# if len(odds) == 0:
#     print(min(list))
# else:
#     print(max(odds))

# Q9: find max divisor

# x = int(input('Enter an integer greater than 2: '))
# divisors = []
# for guess in range (2, x):
#     if x % guess == 0:
#         divisors.append(guess)
# if len(divisors) > 0:
#     print(max(divisors))
# else:
#     print('x is a prime number')


# Q10: Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that
# 1 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, it should print a message to that effect.

# import math
# num = int(input("integer: "))
# root = None
# for pwr in range (2,6):
#     if math.pow(num, (1/pwr)).is_integer():
#         root = int(math.pow(num, (1/pwr)))
#         break
# if root == None:
#     print('no pair of root & pwr exist')
# else:
#     print(root, pwr)

# Q11

# a = 0
# b = 1
# while a <= 50:
#     # just print each number is find
#     print(a, end = ' ')
#     # The next number replace the 1st position
#     # a new number goes into the 2nd position (a)
#     c = a
#     a = b
#     # a new number goes into the 2nd position (b)
#     b = a + c

# Q12

# rows = 3
# columns = 4
# big_list = []
# # (row = 0, 1, 2)
# for row in range(rows):
#     list = []
#     # (0 : 0, 1, 2)
#     for col in range(columns):
#         list.append(row * col)
#     big_list.append(list)
# print(big_list)

# Q12: selection sort
# find the smallest in the sorted part, then move to the next
# list = [14,46,43,27,57,41,45,21,70]
# for i in range(len(list) - 1):
#     for j in range(i, len(list)):
#         if list[j] < list[i]:
#             temp = list[i]
#             list[i] = list[j]
#             list[j] = temp
# print(list)
            
# Q13: insertion sort

# list = [14,46,43,27,57,41,45,21,70]
# # starts at the 2nd position
# # Insertion sort split the list into 2 parts: sorted (left) and unsorted (right)
# # So the unsorted starts at the 2nd position and ends at the final element
# # The 1st element of the unsorted will be compared to the final element of the sorted
# # The outer loop goes from the 2nd element to the last element
# for i in range(1, len(list)):
#     # The inner loop, the comparision for sorting starts at the 1st element of unsorted, or at i
#     j = i
#     # we don't know how many iterations, so use while. J cannot be less than 1
#     while list[j - 1] > list[j] and j > 0:
#         # The sorted part is sorted, so no worries that the while loop get interuppted wrongly
#         temp = list[j]
#         list[j] = list[j - 1]
#         list[j - 1] = temp
#         j -= 1
# print(list)

# Q14: Generate every possible ordering of the elements in the list, using each element exactly once per ordering.
# number of permutations = n!
# Step 1: Pick the first element
# Step 2: move the other elements around the other positions in the list using pop() & append()
# Step 3: Pick the 2nd element and move it to the 1st position
# Step 4: move the other elements around the other positions in the list
# Learn to move elements while fixing the 1st element
# The outer loop changes the 1st element
# The inside loop move the elements

# list = [0, 1, 2, 3]
# for i in range(len(list)):
#     # if i = 0, the number at the 1st position of the list stays the same
#     # if i != 0, list[i] and the 1st position of the list switch places
#     if i != 0:
#         temp = list[0]
#         list[0] = list[i]
#         list[i] = temp
#     # When i = 0, the inner loops (len(list)-1) * 2 times
#     for j in range(len(list)-1):
#         print(list)
#         temp = list[1]
#         list.pop(1)
#         list.append(temp)

# Print Full Multiplication Table

# list = [i for i in range(1,11)]
# multiple = int(input('multiplication table of: '))
# list = [i * multiple for i in list]
# print(list)

# Find largest and smallest digit in a number

# num1 = int(input("Enter a whole number with atleast 2 digits: "))
# solution 1
# min = int(str(num1)[0])
# for i in range(1, len(str(num1))):
#     if (int(str(num1)[i]) < min ):
#         min = int(str(num1)[i])
# print("Min: ", min)
# solution 2
# list = [int(i) for i in str(num1)]
# print(list)
# min = list[0]
# for i in range(1, len(list)):
#     if list[i] < min:
#         min = list[i]
# print("Min: ", min)

# Generate a Python list of all the even numbers between ...

# def even_nums(x,y):
#     list = []
#     for i in range(x, y+1):
#         if i % 2 == 0:
#             list.append(i)
#     return list
# print(even_nums(4,30))

# Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
# All list elements are string

# List = ['abc', 'xyz', 'aba', '1221', 'oWWwo', '22222582']
# Count = []
# for i in List:
#     if i[0] == i[len(i) - 1]:
#         Count.append(i)   
# print(len(Count))

# Q15: Write a Python program to get a list, sorted in increasing order by 
# the last element in each tuple from a given list of non-empty tuples.

# tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# find the smallest in the sorted part, then move to the next
# The outer loop starts from the 1st tuple to the second last
# for i in range(len(tuple_list) - 1):
# #     # The inner loop starts from i to the last tuple
#     for j in range(i, len(tuple_list)): 
# #         # get last element of the 1st tuple
#         last_ele_i = tuple_list[i][-1]
#         # get last element of the 2nd tuple
#         last_ele_j = tuple_list[j][-1]
#         if last_ele_j < last_ele_i:
#             temp = tuple_list[i]
#             tuple_list[i] = tuple_list[j]
#             tuple_list[j] = temp
# print(tuple_list)

# Q16: Calculate Difference Between Lists. Find the elements that appear in one list but NOT in the other.
# list1 = [1, 2, 3, 4, 5]
# list2 = [1, 2, 3, 4, 5]
# # In python, create a copy to not affect the original list
# # combine lists with '+'
# combine = list1.copy() + list2.copy()
# distinct = []
# for i in combine:
#     if combine.count(i) == 1:
#         distinct.append(i)
# print(distinct)

# Concatenate Dictionaries

# Q17:Write a Python script to concatenate the following dictionaries to create a new one.

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# # # Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# # new_dict1 = {**dic1, **dic2, **dic3}
# # new_dict2 = {}
# # new_dict2.update(dic1)
# # new_dict2.update(dic2)
# # new_dict2.update(dic3)
# new_dict3 = {}
# d in a list of dictionary somehow works, each d is a key-value pair
# for d in (dic1, dic2, dic3):
#     new_dict3.update(d)

# Q18: Multiply All Items in a Dictionary
# dic = {1:10, 2:20, 3:30}
# mul = 1
# for i in list(dic.values()):
#     mul *= i
# print(mul)

# Q19: Remove a Key from a Dictionary
# dic = {'a':10, 'b':20, 'c':30}
# # Solution 1
# dic_copy = {}
# # i in this case, somehow is going to be the key, not the pair
# for i in dic:
#     if i != 'a':
#         dic_copy.update({i: dic[i]})
# dic = dic_copy
# print(dic)
# # Solution 2
# del dic['a']
# # Solution 3
# dic.pop('a')

# Q20: Pass / Fail Split from Grade Dictionary

# grades_dict = {"A": 5, "B": 6, "C": 6.7, "D": 10}
# pass_grade = int(input("Enter passing grade: "))
# Solution 1
# p = {}
# f = {}
# for student in grades_dict:
#     if grades_dict[student] >= pass_grade:
#         p.update({student: grades_dict[student]})
#     else: 
#         f.update({student: grades_dict[student]})
# print(p)

# Solution 2
# p = {key : value for key, value in grades_dict.items() if value >= pass_grade}
# f = {key : value for key, value in grades_dict.items() if value < pass_grade}


#  Q21: Map Two Lists into a Dictionary

# Assuming 2 lists have the same length
# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# combine = {}
# Solution 1
# i = 0, 1, 2
# for i in range(len(list_1)):
#     combine.update({list_1[i] : list_2[i]})
# Solution 2
# for i in range(len(list_1)):
#     combine[list_1[i]] = list_2[i]
# Solution 3
# combine = {list_1[i] : list[2] for i in range(len(list_1))}
# print(combine)

# Q22: Remove Duplicates from the Dictionary

# Keys have to be unique
# Built a new list to store only unique. Use 'in'
# If the value is not in the new list, add the key:value pair to the new list
# dict = {'a': 1, 'b': 2, 'c': 2, 'd': 1}
# unique_dict = {}
# for i in dict:
#     # The values of unique_dict gets updated for every iteration
#     if dict[i] not in unique_dict.values():
#         unique_dict.update({i : dict[i]})
# print(unique_dict)

# Q23: Create Dictionary from a String (Letter Frequency)

# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
# string  = 'w3resource'
# # Create an empty list of unique keys
# unique_keys = []
# dict = {}
# # Populate this list
# for i in string:
#     # The unique_keys list gets updated for every loop iteration
#     if unique_keys.count(i) == 0:
#         unique_keys.append(i)
# # Populate the dict with the unique keys and the count of each key
# for j in unique_keys:
#     dict.update({j : string.count(j)})
# print(dict)

# Q24: filter_by_prefix(d, prefix) that takes a dictionary d and a string prefix, 
# and returns a new dictionary containing only those key–value pairs where the key starts with prefix.
# use 'string.startswith()'
# Python cannot 'return value = ...', the assignment of the value needs to be separated
# d = {"user1": 101, "user2": 102, "admin": 999, "user_test": 200}
# def filter_by_prefix(d, prefix):
#     d2 = {key : value for key, value in d.items() if key.startswith(prefix)}
#     return d2
# print(filter_by_prefix(d, 'user'))

#  Q25: Write a Python function to remove duplicates from a list while preserving the order.
# list = [3,3,5,8,6,7,3]
# uniques = []
# for i in list:
#     if i not in uniques:
#         uniques.append(i)
# print(uniques)

# Q26: Write a Python a function to find the maximum sum sub-sequence 
# in a list. Return the maximum value.
# I have to calculate 3 - 2, 3 - 2 + 5, 3 - 2 + 5 + 8, and so on
# list = [3, -2, 5, 8, 8, -7] # answer: 22

# Solution 1. Lots of computational power
# sums = []
# for i in range(len(list) - 1):
#     # Assign the sum with the value of the list at the starting positiion
#     # This value is not added to the list of sums for comparision, so it does not affect the final comparision
#     sum = list[i]
#     # I can't find any other way to ensure that the subsequent sum value is correct. 
#     for j in range(i + 1, len(list)):
#         # The first actual sum is the value of the starting position 
#         # combined with the value at the next position
#         sum += list[j]
#         # The value of "sum" is added to the list of "sums" to find the maximum sum later
#         # before moving to the next iteration. 
#         sums.append(sum)
# print(max(sums))
# Solution 2.
# By default, assume that the max_sum is the very first possible sum value
# max_sum = list[0] + list[1]
# for anchor in range(len(list) - 1):
#     current_sum = list[anchor]
#     for num in range(anchor+1, len(list)):
#         current_sum += list[num]
#         # Instead of creating a list, compare the max_sum with the latest sum. 
#         max_sum = max(max_sum, current_sum)
# print(max_sum)


