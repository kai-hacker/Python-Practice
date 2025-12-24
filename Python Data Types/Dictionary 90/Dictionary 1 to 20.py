# 1. Sort Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.

# 2. Add Key to Dictionary
# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
dict1 = {0: 10, 1: 20}
dict1[3] = 30
print(dict1)

# 3. Concatenate Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic ={}
dic.update(dic1)
dic.update(dic2)
dic.update(dic3)
print(dic)

# 4. Check Key Existence in Dictionary
# Write a Python script to check whether a given key already exists in a dictionary.
dict4 = {"Kai":42,"SMW":43,"Poh":12}
check_key = input("Enter a key: ")
def check_key_existence(key_check,dict):
    for key in dict.keys():
        if key_check == key:
            return True
    return False

print(check_key_existence(check_key,dict4))

# 5. Iterate Over Dictionary Using For Loops
# Write a Python program to iterate over dictionaries using for loops.
dict5 = {"Kai":42,"SMW":43,"Poh":12}
for key in dict5.keys():
    print(key)
for value in dict5.values():
    print(value)
for key,value in dict5.items():
    print(key,value)

# 6. Generate Dictionary of Numbers and Their Squares
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n = int(input())
dict6 = {}
for i in range(1, n+1):
    dict6[i] = i**2
print(dict6)

# 7. Dictionary with Keys 1 to 15 and Their Squares
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
dict7 = {}
for i in range(1,16):
    dict7[i] = i**2
print(dict7)

# 8. Merge Two Python Dictionaries
# Write a Python script to merge two Python dictionaries.

# 9. Iterate Over Dictionaries (Alternative)
# Write a Python program to iterate over dictionaries using for loops.
# Create a dictionary 'd' with color names as keys and corresponding numerical values as values.
d = {'Red': 1, 'Green': 2, 'Blue': 3}
# Iterate through the key-value pairs in the dictionary 'd' using a for loop.
for color_key, value in d.items():
    # Print the color name, 'corresponds to', and its corresponding numerical value.
    print(color_key, 'corresponds to ', d[color_key]) 

# 10. Sum All Items in a Dictionary
# Write a Python program to sum all the items in a dictionary.
dict10 = {'Red': 1, 'Green': 2, 'Blue': 3}
S = sum([value for value in dict10.values()])
print(S)

# 11. Multiply All Items in a Dictionary
# Write a Python program to multiply all the items in a dictionary.
M = 1
dict11 = {'Red': 1, 'Green': 2, 'Blue': 3}
for key in dict11.keys():
    M = M * dict11[key]
print(M)

# 12. Remove a Key from a Dictionary
# Write a Python program to remove a key from a dictionary.
remove_key = 'Red'
dict12 = {'Red': 1, 'Green': 2, 'Blue': 3}
remove_dict12 = dict12.copy()
for key in dict12.keys():
    if key == remove_key:
        remove_dict12.pop(key)
print(remove_dict12)

# 13. Map Two Lists into a Dictionary
# Write a Python program to map two lists into a dictionary.
# Create a list 'keys' containing color names.
keys = ['red', 'green', 'blue']

# Create another list 'values' containing corresponding color codes in hexadecimal format.
values = ['#FF0000', '#008000', '#0000FF']

# Use the 'zip' function to pair each color name with its corresponding color code and create a list of tuples.
# Then, use the 'dict' constructor to convert this list of tuples into a dictionary 'color_dictionary'.
color_dictionary = dict(zip(keys, values))

# Print the resulting 'color_dictionary' containing color names as keys and their associated color codes as values.
print(color_dictionary)

# 14. Sort Dictionary by Key
# Write a Python program to sort a given dictionary by key.
