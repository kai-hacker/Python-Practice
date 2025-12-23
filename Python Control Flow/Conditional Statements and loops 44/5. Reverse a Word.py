'''
Write a Python program that accepts a word from the user and reverses it.
'''
input_text = input("Enter a string: ").strip()
reversed_string= input_text[len(input_text)::-1]
print(reversed_string)