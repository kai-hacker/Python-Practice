'''
Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma separated sequence.

Sample Data : 0100,0011,1010,1001,1100,1001

Expected Output : 1010
'''
value_input = input("Enter a sequence of comma separated 4 digit binary numbers: ")

L_input = value_input.split(',')

def check_divisble_by_5(value):
    S = 0
    reversed_value = value[::-1]
    for i in range(len(reversed_value)):
        S += int(reversed_value[i])* (2**i)
    if S % 5 == 0:
        return True
    else:
        return False

def filter_nums(values):
    for value in values:
        if check_divisble_by_5(value):
            print(value, end = " ")

filter_nums(L_input)
