'''
Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included). for Conditional Statements and loops.1. Divisible by 7 and Multiples of 5
'''
valid_nums = []
for x in range(1500, 2701):
    if(x % 7 == 0) and (x % 5 == 0):
        valid_nums.append(str(x))

print(", ".join(valid_nums))
    