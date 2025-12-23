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