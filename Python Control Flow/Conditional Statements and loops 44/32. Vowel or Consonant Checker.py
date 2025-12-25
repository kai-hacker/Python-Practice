'''
Write a Python program to check whether an alphabet is a vowel or consonant.

Expected Output:

Input a letter of the alphabet: k                                       
k is a consonant.
'''
input_letter = input("Input a letter of the alphabet: ")
if input_letter in ("a", "e", "i", "o", "u"):
    print(f"{input_letter} is a vowel")
else:
    print(f"{input_letter} is a consonant")

