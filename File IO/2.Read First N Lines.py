# 2. Read First N Lines
# Write a Python program to read first n lines of a file.
file2 = "File IO/ex2.txt"
# def read_n_lines(file2, num):
#     with open(file2, "r") as f:
#         lines = []
#         for i, line in enumerate(f,1):
#             print(i)
#             lines.append(line)
#             if i >= num:
#                 break
#     for line in lines:
#         print(line, end ='')

# read_n_lines(file2, 5)

def read_n_lines(file2, num):
    with open(file2, 'r') as f:
        for i in range(num):
            print(f.readline(),end='')

read_n_lines(file2, 5)