'''
Write a Python program to create the multiplication table (from 1 to 10) of a number.

Expected Output:

Input a number: 6                                                       
6 x 1 = 6                                                               
6 x 2 = 12                                                              
6 x 3 = 18                                                              
6 x 4 = 24                                                              
6 x 5 = 30                                                              
6 x 6 = 36                                                              
6 x 7 = 42                                                              
6 x 8 = 48                                                              
6 x 9 = 54                                                              
6 x 10 = 60 
'''
num = int(input("Input a number: "))
if num > 10 or num < 1:
    print("Enter a number in range from 1 to 10")
else:
    for i in range(1,11):
        result = num * i
        print(f"{num} x {i} = {result}")
