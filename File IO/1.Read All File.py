# 1. Read Entire File
# Write a Python program to read an entire text file.

file1 = "File IO/ex1.txt"
with open(file1, "r") as f:
    print(f.read())

# f = open(file1)
# print(f.read())