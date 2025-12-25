'''
Write a Python program to find the median of three values.

Expected Output:

Input first number: 15                                                  
Input second number: 26                                                 
Input third number: 29                                                  
The median is 26.0   
'''
x = float(input("Input first number: "))
y = float(input("Input second number: "))
z = float(input("Input third number: "))

if x>y:
    if x<z:
        median = x
    elif y>z:
        median = y
    else:
        median = z
else:
    if y<z:
        median = y
    elif z<x:
        median = x
    else:
        median = z

print(f"The median is {median} ")