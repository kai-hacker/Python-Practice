# 1. Sum Items in List
# Write a Python program to sum all the items in a list.
a = [1,2,3,4,5,6]
sum_a = sum(a)
print(sum_a)

# 2. Multiply Items in List
# Write a Python program to multiply all the items in a list.
def multiply_list(items):
    if len(items) == 0:
        return 0
    else:
        m = 1
        for item in items:
            m *= item
    return m
print(multiply_list([1,4,5,7]))

# 3. Get Largest Number in List
# Write a Python program to get the largest number from a list.
def find_max(items):
    max = items[0]
    for item in items:
        if max <= item:
            max = item
    return max
print(find_max([1,6,5,43,2,1]))

# 4. Get Smallest Number in List
# Write a Python program to get the smallest number from a list.
def find_min(items):
    min = items[0]
    for item in items:
        if min >= item:
            min = item
    return min
print(find_min([1,6,5,43,2,1]))

# 5. Count Strings with Same Start and End
# Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
def find_strings(items):
    count = 0
    for item in items:
        if len(item)>= 2 and item[0]==item[len(item)-1]:
            count +=1 
    return count
print(find_strings(['abc', 'xyz', 'aba', '1221']))

# 6. Sort Tuples by Last Element
# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# def sort_list(items):
#     sorted_list= []
#     for item in items:

# 7. Remove Duplicates from List
# Write a Python program to remove duplicates from a list.
def remove_dup(items):
    removed_list = []
    for item in items:
        if item not in removed_list:
            removed_list.append(item)
    return removed_list
print(remove_dup([1,2,5,3,5,3,2,1]))

# 8. Check if List is Empty
# Write a Python program to check if a list is empty or not.
def check_valid_list(items):
    if len(items) == 0:
        return "Empty"
    else:
        return "Not Empty"
print(check_valid_list([]))

# 9. Clone or Copy a List
# Write a Python program to clone or copy a list.
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

# 10. Find Words Longer Than n
# Write a Python program to find the list of words that are longer than n from a given list of words.
def find_words(n, string):
    input_string = string.split()
    valid_list = []
    for item in input_string:
        if len(item) > n:
            valid_list.append(item)
    return valid_list
print(find_words(3,"welcome to the jungle"))

# 11. Check Common Member Between Two Lists
# Write a Python function that takes two lists and returns True if they have at least one common member.

#Way1: Using set
def check_common_member1(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection_part = set1.intersection(set2)
    if len(intersection_part) == 0:
        return False
    else:
        return True
    
x = ["apple", "banana", "cherry"]
y = ["google", "microsoft", "apple", "apple"]
print(check_common_member1(x,y))

#Way2: Using loops
def check_common_member2(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

x = ["apple", "banana", "cherry"]
y = ["google", "microsoft"]
print(check_common_member2(x,y))

# 12. Remove Specific Elements from List
# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

def Remove_Specific_Elements(items):
    removed_list = []
    if len(items) > 0:
        for i in range(len(items)):
            if i != 0 and i != 4 and i != 5:
                removed_list.append(items[i])
    else:
        return "Blank List"
    return removed_list

print(Remove_Specific_Elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

# 13. Generate 3D Array
# Write a Python program to generate a 3*4*6 3D array whose each element is *.
width = 3
Length = 4
Height = 6
One_D = ["*" for x in range(width)]
print(One_D)
Two_D = [One_D for y in range(Length)]
print(Two_D)
Three_D = [Two_D for z in range(Height)]
print(Three_D)
#All in one
Array =[[["*" for x in range(width)] for y in range(Length)] for z in range(Height)]
print(Array)

# 14. Remove Even Numbers from List
# Write a Python program to print the numbers of a specified list after removing even numbers from it.
def remove_even_nums(values):
    removed_list = []
    for value in values:
        if int(value) % 2 == 1:
            removed_list.append(value)
    return removed_list

x = [1,2,5,6,7,4,3,5,7,2,1]
print(remove_even_nums(x))

# 15. Shuffle List
# Write a Python program to shuffle and print a specified list.

# Import the 'shuffle' function from the 'random' module, which is used for shuffling the elements in a list
from random import shuffle
# Create a list 'color' with several color strings
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Use the 'shuffle' function to randomly reorder the elements in the 'color' list
shuffle(color)
# Print the shuffled 'color' list, which will have its elements in a random order
print(color)

# 16. Generate Square Numbers in Range
# Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).
def generate_square_numbers():
    square_list = []
    for i in range(1,31):
        square_list.append(i**2)
    print(square_list[:5:])
    print(square_list[-5::])
generate_square_numbers()

# 17. Check If All Numbers Are Prime
# Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False

import math
def check_prime (value):
    if value == 0 or value == 1:
        return False
    for i in range(2, math.floor(math.sqrt(value))+1):
        if value % i == 0:
            return False
    return True

def check_list (values):
    for value in values:
        if not check_prime(value):
            return False
    return True

print(check_list([5, 3, 13,21, 7]))

# 18. Generate All List Permutations
# Write a Python program to generate all permutations of a list in Python.
# Import the 'itertools' module, which provides various functions for working with iterators
import itertools
# Use 'itertools.permutations' to generate all permutations of the list [1, 2, 3], and convert the result to a list
# This will produce all possible orderings of the elements in the list
print(list(itertools.permutations([1, 2, 3])))

# 19. Calculate Difference Between Lists
# Write a Python program to calculate the difference between the two lists.
def calculate_difference_lists(a,b):
    a_notin_b = []
    b_notin_a = []
    for i in a:
        if i not in b:
            a_notin_b.append(i)
    for j in b:
        if j not in a:
            b_notin_a.append(j)
    differ_list = a_notin_b + b_notin_a
    return differ_list

list19a = [1, 3, 5, 7, 9, 9]
list19b = [1, 2, 4, 6, 7, 8]
print(calculate_difference_lists(list19a,list19b))

# 20. Access List Indices
# Write a Python program to access the index of a list.
list20 = [1,4,6,4,3]
for index, value in enumerate(list20):
    print(index, value)

