'''
21. Create Combinations of Letters from Dictionary Keys

Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.

Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd
'''
# 22. Find Highest 3 Values of Corresponding Keys in a Dictionary
# Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
values = list(my_dict.values())
values.sort(reverse= True)
for key in my_dict.keys():
    if my_dict[key] == values[0] or my_dict[key]==values[1] or my_dict[key]==values[2]:
        print(key, end=' ')
print()

# 23. Combine Values in a List of Dictionaries
# Write a Python program to combine values in a list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})
Dicts = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Count = {}
for dict in Dicts:
    if dict['item'] not in Count.keys():
        Count[dict['item']] = dict['amount']
    else:
        Count[dict['item']] += dict['amount']
print(Count)

# 24. Create Dictionary from a String (Letter Frequency)
# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
input = 'w3resource'
x = set('w3resource')
output ={}
for val in x:
    output[val] = input.count(val)
print(output)

'''
25. Print Dictionary in Table Format
Write a Python program to print a dictionary in table format.
'''

# 26. Count Values Associated with a Key in a Dictionary
# Write a Python program to count the values associated with a key in a dictionary.
# Create a list 'student' containing dictionaries, each representing a student with 'id', 'success', and 'name' information.
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]

# Print the sum of 'id' values for all students in the 'student' list.
print(sum(d['id'] for d in student))

# Print the sum of 'success' values (True/False) for all students in the 'student' list.
print(sum(d['success'] for d in student))

'''
27. Convert List into Nested Dictionary of Keys
Write a Python program to convert a list into a nested dictionary of keys.
'''
# 28. Sort a List Alphabetically in a Dictionary
# Write a Python program to sort a list alphabetically in a dictionary.
# Create a dictionary 'num' with keys 'n1', 'n2', and 'n3', and associated lists of numbers as values.
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

# Use a dictionary comprehension to create a new dictionary 'sorted_dict'.
# Iterate through the key-value pairs in 'num' and sort the lists of numbers ('y') for each key ('x').
sorted_dict = {x: sorted(y) for x, y in num.items()}

# Print the 'sorted_dict' dictionary, which contains the same keys with sorted lists of numbers as values.
print(sorted_dict)

# 29. Remove Spaces from Dictionary Keys
# Write a Python program to remove spaces from dictionary keys.


# 38. Match Key Values in Two Dictionaries
# Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
dict381 = {'key1': 1, 'key2': 3, 'key3': 2}
dict382 = {'key1': 1, 'key2': 2}
for key in dict381.keys():
    if key in dict382.keys():
        if dict381[key]==dict382[key]:
            print(f"{key}:{dict381[key]} is present in both dicts")
'''
39. Store Dictionary Data in a JSON File

Write a Python program to store dictionary data in a JSON file.

Original dictionary:
{'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
<class 'dict'>
Json file to dictionary:
{'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}

'''

# 40. Create Dictionary with Keys 'x', 'y', 'z' and List Values

# Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.

# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]
k= {'x':list(range(11,20)),
 'y':list(range(21,30)),
 'z':list(range(31,40))}
print(k['x'][4])
print(k['y'][4])
print(k['z'][4])
print(f"x has value {k['x']}")
print(f"y has value {k['y']}")
print(f"z has value {k['z']}")

print(set('a b c'))