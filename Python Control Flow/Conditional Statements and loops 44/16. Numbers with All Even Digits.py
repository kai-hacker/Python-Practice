'''
Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.
'''
valid_list =[]
for i in range(100,401):
    if i % 2 == 0 and (i // 10) % 2 == 0 and (i//100) % 2 == 0:
        valid_list.append(str(i))
output = ",".join(valid_list)
print(output)