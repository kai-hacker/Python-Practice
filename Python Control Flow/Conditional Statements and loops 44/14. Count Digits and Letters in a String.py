'''
Write a Python program that accepts a string and calculates the number of digits and letters.

Sample Data : Python 3.2

Expected Output :

Letters 6
Digits 2
'''
text_input = input("Enter a string: ")
count_letter = 0
count_digit = 0
for i in range(len(text_input)):
    if text_input[i].isdigit():
        count_digit+=1
    elif text_input[i].isalpha():
        count_letter +=1
print(count_letter," ", count_digit)