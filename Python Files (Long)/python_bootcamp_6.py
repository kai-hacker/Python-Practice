# Sample test 4
# n = int(input("Enter a positive number: "))
# if n != 0:
#     print("1", end=", ")
#     # The next perfect square is 4
#     # Find the square of 2, then 3, and so on
#     num = 2
#     square = 2**2
#     while square <= n:
#         print(square, end=", ")
#         num += 1
#         square = num ** 2 
# 
# n = int(input("Enter a positive number: "))
# num = 1
# first = True
# # 0 will be eliminated by this loop condition
# # While because we don't know when to end
# # Check num * num right in the while condition
# while num * num <= n:
#     # if first = false
#     # This if condition gives us "1" instead of ", 1"
#     if not first:
#         # print ", " before the number, so ", 4", ", 9", ...
#         print(", ", end="")
#     print(num * num, end="")
#     first = False
#     num += 1

fname_1 = 'Python Files (Long)/txt files/input.txt'
fname_2 = 'Python Files (Long)/txt files/output.txt'
# try: 
#     f_input = open(fname_1, 'r')
#     f_output = open(fname_2, 'w')
#     for line in f_input:
#         f_output.write(line)
# except:
#     print('Files cannot be opened:', f_input, ",", f_output)
#     exit()

with open(fname_1, 'r') as f_input, open(fname_2, 'w') as f_output:
    for line in f_input:
        f_output.write(line)
