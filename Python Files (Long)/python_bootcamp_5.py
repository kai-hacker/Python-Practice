# WEEK 10 INCLASS EXERCISES AND CHALLENGE

# Q3 — Keep Only Non-Empty Lines
# Read from input.txt and write to clean.txt only the lines that are not empty 
# after stripping spaces.
# fname_input = 'Python Files (Long)/input.txt'
# fname_clean = 'Python Files (Long)/clean.txt'
# with open(fname_input, 'r') as f_input, open(fname_clean, 'w') as f_clean:
#     for line in f_input:
#         'if line.strip()' is equal to 'if line.strip() != ""'
#         if line.strip() != "":
#             f_clean.write(line)

# Q4: Uppercase All Lines
# fname_input = 'Python Files (Long)/input.txt'
# fname_clean = 'Python Files (Long)/clean.txt'
# with open(fname_input, 'r') as f_input, open(fname_clean, 'w') as f_clean:
#     for line in f_input:
#         f_clean.write(line.upper())

# Q5: Extract Lines Containing a Keyword
# fname_input = 'Python Files (Long)/input.txt'
# fname_clean = 'Python Files (Long)/clean.txt'
# key_word = 'input'
# with open(fname_input, 'r') as f_input, open(fname_clean, 'w') as f_clean:
#     for line in f_input:
#         # use string.find() != -1
#         if line.lower().find(key_word.lower()) != -1:
#             f_clean.write(line)

# Exercise 20 — Mini Project: Clean + Summarize CSV
# Given transactions.csv with columns: date,category,amount
# is_valid_amount(s) → checks whether s is a valid number

# Q6: Sum Numbers from a Text File. Read from numbers.txt, where each line contains one integer.
# fname = 'Python Files (Long)/txt files/numbers.txt'
# sum = 0
# with open(fname, 'r') as f:
#     # Each num is a line of type string, usually with \n at the end
#     # int() also auto ignores whitespaces and newlines
#     for num in f:
#         sum += int(num)
# print(sum)

# Q7: Write to filtered_numbers.txt only numbers greater than or equal to T
# fname_input = 'Python Files (Long)/txt files/numbers.txt'
# fname_output = 'Python Files (Long)/txt files/filtered_numbers.txt'
# t = int(input("Enter number to filter: "))
# with open(fname_input, 'r') as f_input, open(fname_output, 'w') as f_output:
#     for num in f_input:
#         # use string.find() != -1
#         if int(num) >= t:
#             f_output.write(num)

# Q8 — CSV: Copy Selected Columns
# Task: Given students.csv with columns: name,age,major,gpa. Write students_simple.csv containing only name and gpa columns.
# import to work with csv
# import csv
# fname_input = 'Python Files (Long)/txt files/students.csv'
# fname_output = 'Python Files (Long)/txt files/students_simple.csv'
# # newline='' is recommended for csv files
# with open(fname_input, 'r', newline = '') as csvinput, open(fname_output, 'w', newline = '') as csvoutput:
#     # reader = csv.reader, writer = csv.writer
#     reader = csv.reader(csvinput)
#     writer = csv.writer(csvoutput)
#     # next() get the very first row, then continue to read the rest of the files
#     first_row = next(reader)
#     # list.index(item) find the index position of the item in the list
#     name_index = first_row.index("name")
#     gpa_index = first_row.index("gpa")
#     # Because the loop starts from the 2nd row, the 1st row needs to be written manually
#     writer.writerow(["name", "gpa"])
#     # Can you "for" loop to read line by line, like .txt file
#     for row in reader:
#         writer.writerow([row[name_index], row[gpa_index]])

# Q9: Compute a New Column. Given sales.csv with columns: item,price,quantity. 
# Create sales_total.csv containing: item,price,quantity,total, where total = price * quantity.
# import csv
# fname_input = 'Python Files (Long)/txt files/sales.csv'
# fname_output = 'Python Files (Long)/txt files/sales_total.csv'
# with open(fname_input, 'r', newline = '') as csvinput, open(fname_output, 'w', newline = '') as csvoutput:
#     reader = csv.reader(csvinput)
#     writer = csv.writer(csvoutput)
#     first_row = next(reader)
#     price_index = first_row.index("price")
#     quantity_index = first_row.index("quantity")
#     writer.writerow(["item","price","quantity","total"])
#     for row in reader:
#         total = float(row[price_index]) * float(row[quantity_index])
#         # cannot use append because it will mutate the original
#         # use list + list concatenate
#         writer.writerow(row + [total])

# Q10: Count Rows Matching a Condition. Gpa >= 3.0
# import csv
# fname_input = 'Python Files (Long)/txt files/students.csv'
# fname_output = 'Python Files (Long)/txt files/students_simple.csv'
# with open(fname_input, 'r', newline = '') as csvinput, open(fname_output, 'w', newline = '') as csvoutput:
#     reader = csv.reader(csvinput)
#     writer = csv.writer(csvoutput)
#     first_row = next(reader)
#     gpa_index = first_row.index("gpa")
#     count = 0
#     for row in reader: 
#         if float(row[gpa_index]) >= 3.0:
#             count += 1
#     print(count) #should be 3

# Q11: Function: Count Keyword Occurrences. count_keyword_in_file(input_path, keyword) 
# that returns how many lines contain the keyword.
# ask the user for keyword
# call the function on input.txt
# write the count to keyword_count.txt
# keyword = input("Give a keyword to search for: ").strip()
# input_path = 'Python Files (Long)/txt files/input.txt'
# def count_keyword_in_file(input_path, keyword):
#     fname_output = 'Python Files (Long)/txt files/keyword_count.txt'
#     count = 0
#     with open(input_path, 'r') as f_input, open(fname_output, 'w') as f_output:
#         for line in f_input:
#             # string.find()
#             # if keyword in line is better
#             if keyword in line:
#                 count += 1
#         f_output.write(str(count))
# count_keyword_in_file(input_path, keyword)

# Q12: Longest Line Finder
# def longest_line(input_path):
#     longest = None
#     # line num starts at 1
#     line_num = 1
#     with open(input_path, 'r') as f_input:
#         for line in f_input:
#             if longest == None or len(longest) < len(line):
#                 longest = str(line_num) + " " + line
#             # line_num increases by 1
#             line_num += 1
#     print(longest)
# input_path = 'Python Files (Long)/txt files/input.txt'
# longest_line(input_path)

# Q13: Functions Normalize Whitespace
# Write:
# ● normalize_line(line) → replaces multiple spaces with a single space and
# strips leading/trailing spaces
# ● normalize_file(input_path, output_path) → reads input file and writes
# normalized lines
# In python, remove spaces with split & join
# def normalize_line(line):
#     line = line.strip()
#     line = ' '.join(line.split())
#     return line
# input_path = 'Python Files (Long)/txt files/input.txt'
# output_path = 'Python Files (Long)/txt files/output.txt'
# def normalize_file(input_path, output_path):
#     with open(input_path, 'r') as f_input, open(output_path, 'w') as f_output:
#         for line in f_input:
#             line = line.strip()
#             line = ' '.join(line.split())
#             # + "\n" to move to the next line and write
#             f_output.write(line + "\n")
# normalize_file(input_path, output_path)

# Q14: Merge Two Text Files Alternating Line
# Use 'while' loop with files and .readline() with .txt
# def merge_alternating(fname_input_1, fname_input_2, fname_output):
#     with open(fname_input_1, 'r') as f_input_1, open(fname_input_2, 'r') as f_input_2, open(fname_output, 'w') as f_output:
#         # A loop that does not know when it will end. 
#         # Use "while" instead of "for"
#         while True:
#             # read 1 line from a.txt
#             line1 = f_input_1.readline()
#             # read 1 line from b.txt
#             line2 = f_input_2.readline()
#             # if both line1 & line2 do not exists, meaning both files have been fully read
#             if not line1 and not line2:
#                 break
#             # check again if line1 exists:
#             if line1:
#                 # If the line does not end with a newline, add one
#                 # use .endswith("\n")
#                 if not line1.endswith("\n"):
#                     f_output.write(line1 + "\n")
#                 else:
#                     f_output.write(line1)

#             if line2:
#                 if not line2.endswith("\n"):
#                     f_output.write(line2 + "\n")
#                 else:
#                     f_output.write(line2)
# fname_input_1 = 'Python Files (Long)/txt files/a.txt'
# fname_input_2 = 'Python Files (Long)/txt files/b.txt'
# fname_output = 'Python Files (Long)/txt files/merged.txt'
# merge_alternating(fname_input_1, fname_input_2, fname_output)

# W3RESOURCES Python File Input Output
# Q4: Read Last N Lines
# fname = 'Python Files (Long)/txt files/w3q4.txt'
# with open(fname, 'r') as f:
#     n = int(input("Number of lines to read from the bottom: "))
#     # Use minus index to go backward. Then loop to print line by line
#     for line in f.readlines()[-n:]:
#         # rstrip() to remove new line after
#         print(line.rstrip())

# Q5: File to List. Write a Python program to read a file line by line and store it into a list.
# fname = 'Python Files (Long)/txt files/w3q4.txt'
# lines = []
# with open(fname, 'r') as f:
#     for line in f:
#         lines.append(line)
# print(lines)

# W3RESOURCES Python CSV File Reading and Writing
# Q8: CSV Skip Header and Count. Write a Python program that reads each row of a given csv file and 
# skip the header of the file. Also print the number of rows and the field names.
# import csv
# fname = 'Python Files (Long)/txt files/sales_total.csv'
# with open(fname, 'r', newline = '') as csvfile:
#     # import csv
#     # then use csv.function(), such as .reader() & .writer()
#     reader = csv.reader(csvfile)
#     # use next() to get the next line. At the start, will get the first line
#     header = next(reader)
#     count = 0
#     for line in reader:
#         count += 1
#     print(header)
#     print(count)

# WEEK 11

# Panda, create a dataFrame
import pandas as pd
# Each is a column
df = pd.DataFrame({
    "name": ["A", "Bob", "C"], 
    "age": [20, 21, 22],
    "score": [85, 90, 95]
})
# Selecting column
df["name"]
# Multiple columns, index a lists
# print(df[["name", "score"]])
# Select rows with .iloc[]. The answer has dtype at the end
print(df.iloc[1])



    






