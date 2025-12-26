# 21. Convert List to String
# Write a Python program to convert a list of characters into a string.
list21 = ["K", "a", "i ", "k49 ", "PBC"]
string21 = "".join(list21)
print(string21)

# 22. Find Index of List Item
# Write a Python program to find the index of an item in a specified list.
list22 = ['a','b', 1, 4, 6]
print(list22.index('a'))

# 23. Flatten Shallow List
# Write a Python program to flatten a shallow list.
# Original list elements:
# [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
# Flatten the said list:
# [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]
def flatten_shollow_list(nums):
    return [x for y in nums for x in y]
nums = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
flatten_list = flatten_shollow_list(nums)
print(flatten_list)

# 24. Append One List to Another
# Write a Python program to append a list to the second list.
a = [1,2,4,5,6]
b = [2,4,6]
a.extend(b)
print(a)

# 25. Select Random Item from List
# Write a Python program to select an item randomly from a list.
import random
a = [1,2,4,5,6]
r = random.randint(0,len(a))
print(a[r])

'''
26. Check Circularly Identical Lists
Write a Python program to check whether two lists are circularly identical.
'''
# 27. Find Second Smallest Number in List
# Write a Python program to find the second smallest number in a list.
def find_smallest_number(nums):
    smallest = nums[0]
    for num in nums:
        if smallest > num:
            smallest = num
    return smallest
a27 = [1,5,7,5,9,10,11]
c = a27.copy()
sorted_a27 = []
for i in range(len(a27)):
    smallest_num = find_smallest_number(c)
    sorted_a27.append(smallest_num)
    c.remove(c[c.index(smallest_num)])
print(sorted_a27)
print(f"The second smallest num: {sorted_a27[1]}")

#w2
a27 = [1,5,7,5,9,10,11]
sorted_a27 = a27.copy()
sorted_a27.sort()
print(sorted_a27)

# 28. Find Second Largest Number in List
# Write a Python program to find the second largest number in a list.
def find_largest_number(nums):
    largest = nums[0]
    for num in nums:
        if largest<num:
            largest = num
    return largest

a28 = [1,5,7,5,9,10,11]
d = a28.copy()
sorted_a28 = []
for i in range(len(a28)):
    largest_num = find_largest_number(d)
    sorted_a28.append(largest_num)
    d.remove(d[d.index(largest_num)])
print(sorted_a28)

# 29. Get Unique Values from List
# Write a Python program to get unique values from a list.
a29 = [1,5,7,5,9,10,11]
unique_vals = set(a29)
unique_vals = list(unique_vals)
print(unique_vals)

# 30. Count Frequency of List Elements
# Write a Python program to get the frequency of elements in a list.
def count_freq(nums, val):
    count = 0
    for num in nums:
        if val == num:
            count += 1
    return count

a30 = [1,5,6,7,3,5,3,1, 'Kai', 'Kai']
unique_a30 = set(a30)
dict_freq = {}
for key in unique_a30:
    dict_freq[key] = count_freq(a30, key)
print(dict_freq)

# 31. Count Elements in List Within Range
# Write a Python program to count the number of elements in a list within a specified range.
def count_freq(nums, val):
    count = 0
    for num in nums:
        if val == num:
            count += 1
    return count
def find_list_freq_within_range(list, start, end):
    i = list.index(start)
    j = list.index(end)
    new_list = list[i:j+1]
    print(new_list)
    unique = set(new_list)
    dict_freq = {}
    for key in unique:
        dict_freq[key] = count_freq(new_list, key)
    return dict_freq

#Given list:
a31 = [1,5,7,56,4,'a', 'ba', 5,3,1]
start = 7
end = 3
print(find_list_freq_within_range(a31,start,end))

'''
32. Check if List Contains Sublist
Write a Python program to check whether a list contains a sublist.
'''

'''
33. Generate All Sublists
Write a Python program to generate all sublists of a list.
'''
'''
34. Compute Primes Using Sieve of Eratosthenes
Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.
Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.
'''
# 35. Create List with Range Concatenation
# Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
def add_str_to_num(values, num):
    return [v + str(num) for v in values]
n =5
org_list = ['p','q']
new_list = []
for i in range(1, n+1):
    new_list.extend(add_str_to_num(org_list,i))
print(new_list)

'''
36. Get Variable ID or String
Write a Python program to get a variable with an identification number or string.
'''

# 37. Find Common Items in Lists
# Write a Python program to find common items in two lists.
a37 = [1,4,5,6,7,9]
b37 = [2,5,4,3,1,4]
common_a_b37 = []
for item in a37:
    if item in b37:
        common_a_b37.append(item)
print(set(common_a_b37))

# 38. Swap Every n-th and (n+1)th Values
# Write a Python program to change the position of every n-th value to the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
a38 = [0,1,2,3,4,5,6]
b38 = a38[0::2]
c38 = a38[1::2]
d38 = []
for i in range(len(c38)):
    d38.append(c38[i])
    d38.append(b38[i])
if len(a38) % 2 == 1:
    d38.append(b38[len(b38)-1]) 
print(d38)

# 39. Convert Integers List to Single Integer
# Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
L39 = [11,33,50]
x = int(''.join(map(str,L39)))
print(x)

'''
40. Split List by First Character
Write a Python program to split a list based on the first character of a word.
'''
