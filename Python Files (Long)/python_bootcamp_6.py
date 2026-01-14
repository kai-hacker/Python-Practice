# Sample test 4
# Q1:
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

# Q4:
# import numpy as np
# scores_subjects = np.array([
#  [80, 85, 85],
#  [85, 88, 85],
#  [85, 85, 88]
# ])
# # compute the average score for each student
# index_position = None
# for student in range(len(scores_subjects)):
#     student_score = scores_subjects[student].mean()
#     print(f"Student at index {student}'s averge score: {student_score}")
#     if index_position == None or student_score > scores_subjects[index_position].mean():
#         index_position = student
# print(f"Answer: {index_position}")