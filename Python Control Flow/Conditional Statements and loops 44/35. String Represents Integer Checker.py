'''
Write a Python program that checks whether a string represents an integer or not.

Expected Output:

Input a string: Python                                                  
The string is not an integer.  
'''
x = input("Input a string: ").strip()
if len(x) == 0:
    print("Enter a valid string")
else:
    if all([i in "0123456789" for i in x]):
        print("The string is an integer.")
    else:
        print("The string is not an integer.")