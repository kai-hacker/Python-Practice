'''
Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.
'''
S = 0
C = 0
while True:
    num = int(input())
    if num == 0:
        break
    else:
        C += 1
        S += num
print(S,S/C)
