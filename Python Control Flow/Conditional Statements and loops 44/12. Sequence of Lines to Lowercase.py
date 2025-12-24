'''
Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
'''
L = []
while True:
    text = input()
    L.append(text)
    if len(text.strip()) == 0:
        break
L.remove(L[len(L)-1])
for value in L:
    print(value.lower())

