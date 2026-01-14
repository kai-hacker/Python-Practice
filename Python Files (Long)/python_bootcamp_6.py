# Sample test 4
# Q1:
# n = int(input("Enter a positive number: "))
# starting_num = 1
# while starting_num**2 <= n:
#     if starting_num != 1:
#         print(", ", end = "")
#     print(starting_num**2, end = "")
#     starting_num += 1
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

# Q2:
# fname_1 = "Python Files (Long)/txt files/file.txt"
# fname_2 = "Python Files (Long)/txt files/substring.txt"
# with open(fname_1, 'r') as f1, open(fname_2, 'w') as f2:
#     inp = f1.read()
#     f1.seek(0) 
#     for line in f1:
#         if inp.count(line.strip()) >= 2:
#             f2.write(line)

# Q3: 
# import csv
# def highest_score(student_id):
#     fname = "Python Files (Long)/txt files/scores.csv"
#     with open(fname, 'r', newline = "") as csvfile:
#         score = None
#         subject = None
#         headers = next(csvfile)
#         for row in csvfile:
#             row_list = row.strip().split(",")
#             if (row_list[0] == student_id):
#                 if score == None or int(row_list[2]) > score:
#                     score = int(row_list[2])
#                     subject = row_list[1]
#         return subject
# student_id = 'S002'
# s = highest_score(student_id)
# print(s)

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

# Q5:
# Solution 1
# def most_similar(query):
#     fname = "Python Files (Long)/txt files/words.txt"
#     with open(fname, 'r') as f:
#         # Get the 1st list of [word in the file, number of similar characters]
#         # A list of lists
#         lists = []
#         for word in f:
#             word = word.strip()
#             shorter_word = None
#             longer_word = None
#             if len(query) > len(word):
#                 shorter_word = word #abs
#                 longer_word = query #about
#             else: 
#                 shorter_word = query
#                 longer_word = word
#             count = 0
#             for char in range(len(shorter_word)):
#                 if shorter_word[char] == longer_word[char]:
#                     count += 1
#                 else:
#                     break
#             lists.append([word, count])
#         similar_chars = None
#         for i in range(len(lists)):
#             if similar_chars == None or lists[i][1] > similar_chars:
#                 similar_chars = lists[i][1]
#         final_list = []
#         for i in range(len(lists)):
#             if lists[i][1] == similar_chars:
#                 final_list.append(lists[i][0])
#         return final_list
# query = 'band'
# print(most_similar(query))
# Solution 2
def most_similar(query):
    fname = "Python Files (Long)/txt files/words.txt"
    with open(fname, 'r') as f:
        # Count matching characters from the start for each word
        word_matches = []
        for word in f:
            word = word.strip()
            count = 0
            for i in range(min(len(query), len(word))):
                if query[i] == word[i]:
                    count += 1
                else:
                    break
            word_matches.append((word, count))
        
        # Find maximum match count
        max_count = max(match[1] for match in word_matches)
        
        # Return all words with maximum matches
        return [word for word, count in word_matches if count == max_count]




