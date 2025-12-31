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
import csv
fname_input = 'Python Files (Long)/txt files/sales.csv'
fname_output = 'Python Files (Long)/txt files/sales_total.csv'
with open(fname_input, 'r', newline = '') as csvinput, open(fname_output, 'w', newline = '') as csvoutput:
    reader = csv.reader(csvinput)
    writer = csv.writer(csvoutput)
    first_row = next(reader)
    price_index = first_row.index("price")
    quantity_index = first_row.index("quantity")
    writer.writerow(["item","price","quantity","total"])
    for row in reader:
        total = float(row[price_index]) * float(row[quantity_index])
        # cannot use append because it will mutate the original
        # use list + list concatenate
        writer.writerow(row + [total])


    






