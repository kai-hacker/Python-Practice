'''
Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.
'''
def sum_of_two_integers(a,b):
    sum = a+b
    if sum>= 15 and sum <= 20:
        return 20
    else:
        return sum
print(sum_of_two_integers(7,9))