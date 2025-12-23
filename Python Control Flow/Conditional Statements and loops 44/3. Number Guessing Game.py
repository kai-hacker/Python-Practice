'''
Write a Python program to guess a number between 1 and 9. Python programming course

Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
'''

import random
lucky_num = random.randint(0,9)
input_num = int(input("Enter a number between 1 and 9: "))
while input_num != lucky_num:
    input_num = int(input("Please guess again: "))

print("Well guessed!")