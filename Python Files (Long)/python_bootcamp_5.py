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

# Q20 — Mini Project: Clean + Summarize CSV
# Given transactions.csv with columns: date,category,amount
# Some rows may have:
# ● missing category
# ● invalid amount (not a number)
# Write these functions:
# 1. is_valid_amount(s) → checks whether s is a valid number
# 2. clean_transactions(input_csv, clean_csv, bad_rows_txt) 
# → writes valid rows to clean_transactions.csv, invalid rows to bad_rows.txt
# 3. sum_by_category(clean_csv) → returns dictionary category ->
# total_amount
# 4. write_category_summary(summary, out_txt) → writes a neat summary
# report
# In main:
# ● call cleaning
# ● then compute totals per category
# ● output category_summary.tx
# import csv
# def is_valid_amount(s):
#     try:
#         value = float(s)
#         if value >= 0:
#             return True
#         else:
#             return False
#     # ValueError is a built-in python exception
#     except ValueError:
#         return False
# def clean_transactions(input_csv, clean_csv, bad_rows_txt):
#     # The 3 parameters are file names
#     with (open(input_csv, 'r', newline = "") as f_1, 
#           open(clean_csv, 'w', newline = "") as f_2, 
#           open(bad_rows_txt, 'w') as f_3):
#         # Get the first row, the column names, as a string
#         # after this, the next time we will read from the 2nd line
#         headers = next(f_1)
#         csv_writer = csv.writer(f_2)
#         for row in f_1:
#             # This list will have 3 elements, index 0 to 2
#             row_list = row.strip().split(",")
#             # The first and second column must not be empty
#             # The third column must have a valid number
#             if (row_list[0] != "" 
#                 and row_list[1] != "" 
#                 and is_valid_amount(row_list[2])):
#                 csv_writer.writerow(row_list)
#             else:
#                 f_3.write(row)
# input_csv = 'Python Files (Long)/txt files/transactions.csv'
# clean_csv = 'Python Files (Long)/txt files/clean.csv'
# bad_rows_txt = 'Python Files (Long)/txt files/bad_rows.txt'
# clean_transactions(input_csv, clean_csv, bad_rows_txt)
# def sum_by_category(clean_csv):
#     category_dict = {}
#     with open(clean_csv, 'r', newline="") as f_2:
#         next(f_2)  # skip header
#         for row in f_2:
#             row_list = row.strip().split(",")
#             category = row_list[1]
#             amount = float(row_list[2])
#             category_dict[category] = category_dict.get(category, 0.0) + amount
#     return category_dict
# summary = sum_by_category(clean_csv)
# def write_category_summary(summary, out_txt):
#     with open(out_txt, 'w') as f:
#         f.write("Category summary report\n")
#         for key, value in summary.items():
#             f.write(f"{key}: {value}\n")
# out_txt = 'Python Files (Long)/txt files/summary_report.txt'
# write_category_summary(summary, out_txt)

# WEEK 10 POSTCLASS EXERCISES AND CHALLENGE
# Q3 — Replace Words from a Mapping
# Inputs: text.txt, mapping.txt
# ● mapping.txt format: each line is old_word,new_word (one pair per line)
# Task: Create replaced.txt by replacing every occurrence of old_word with new_word
# for all pairs in mapping.txt.
# Requirement: Apply mappings in the order they appear in mapping.txt.
# 
# fname_1 = 'Python Files (Long)/txt files/text.txt'
# fname_2 = 'Python Files (Long)/txt files/mapping.txt'
# fname_3 = 'Python Files (Long)/txt files/replaced.txt'
# with open(fname_1, 'r') as f_1, open(fname_2, 'r') as f_2, open(fname_3, 'w') as f_3:
#     # All the content of f_1 is assigned to inp_1
#     inp_1 = f_1.read()
#     # Create a list of f_2 lines
#     f_2_lines = f_2.readlines()
#     # Modify f_2_lines
#     new_list = []
#     # 3 elements, each is a line
#     for line in f_2_lines:
#         line = line.strip()
#         # line is now a list
#         line = line.split(",")
#         # Create a list of lists
#         new_list.append(line)
#     print(new_list)
#     for line in new_list:
#         # replace needs assignment
#         inp_1 = inp_1.replace(line[0], line[1])
#     # write the whole modifed inp_1 into f_3
#     f_3.write(inp_1)

# Q4 Find Top 3 Longest Lines
# Find the longest lines, but 3 times
fname_1 = 'Python Files (Long)/txt files/find_lines.txt'
fname_2 = 'Python Files (Long)/txt files/top_3_longest.txt'
with open(fname_1, 'r') as f1, open(fname_2, 'w') as f2:
    list_1 = f1.readlines()
    # loop 3 times
    for i in range(3):
        # assume the 1st is the longest
        longest_line = list_1[0]
        index = 0
        for i in range(1, len(list_1)):
            if len(list_1[i]) > len(longest_line):
                longest_line = list_1[i]
                index = i
        f2.write(longest_line)
        list_1.pop(index)
        print(list_1)

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
# import pandas as pd
# # Each is a column
# df = pd.DataFrame({
#     "name": ["A", "Bob", "C"], 
#     "age": [20, 21, 22],
#     "score": [85, 90, 95]
# })
# # Selecting column
# df["name"]
# # Multiple columns, index a lists
# # print(df[["name", "score"]])
# # Select rows with .iloc[]. The answer has dtype at the end
# print(df.iloc[1])

# WEEK 11 INCLASS EXERCISES AND CHALLENGE
# Q1 Basic Statistics on a 1D Array
# .min(), .max(), .mean()
# import numpy as np
# a = np.array([12, 5, 8, 20, 15, 3, 10])
# print(a.min()) 
# print(a.max())
# print(a.mean())  

# Q2 Filter Values in a 1D Array
# import numpy as np
# # .array(range())
# a = np.array(range(1, 20+1))
# # print(a)
# # f you want to see it as a Python list with commas, print(a.tolist())
# # array[logical filtering]
# # print(a[a > 10])
# print(a[a % 2 == 0])

# Q3 Element-wise Operations
# import numpy as np
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([10, 20, 30, 40, 50])
# Element-wise plus
# print(a + b)
# print(a * b)
# print(abs(a-b))

# Q4 
# import numpy as np
# a = np.array([[3, 5, 7],
#             [2, 4, 6],
#             [1, 8, 9]])
# # Index[0] for first row, then use function
# print(a[0].sum())

# Q8 Multiple Statistics per Group
# Group by department
# Compute mean, minimum, and maximum salary for each department
# Print the resulting table
# Plot a bar chart of mean salary per department
# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.DataFrame({
#     "dept": ["HR", "HR", "Sales", "Sales", "Marketing"],
#     "salary": [1000, 2000, 500, 500, 2000]
# })

# # When you use groupby(), the grouped column 
# # becomes the index of the DataFrame
# dept_mean = df.groupby("dept")["salary"].mean()
# dept_min = df.groupby("dept")["salary"].min()
# dept_max = df.groupby("dept")["salary"].max()
# # Create a new df, assign values to columns
# result = pd.DataFrame({
#     # There's result.index
#     "mean": dept_mean,
#     "min": dept_min,
#     "max": dept_max
# })
# # print(result)
# # Use result.index, then result["col_name"]
# # plt.chart_type(), plt.xlabel, plt.ylabel
# plt.bar(result.index, result["mean"])
# # plt.xlabel("Department")
# plt.ylabel("Mean Salary")
# plt.show()

# Q9 Time-based Grouping and Line Plot
# Create a DataFrame with columns:
# month (values like Jan, Feb, Mar, …)
# sales
# Tasks:
# 1. Group by month
# 2. Compute total sales per month
# import pandas as pd
# import matplotlib.pyplot as plt
# a = pd.DataFrame({
#     "month": ["Jan", "Feb", "Jan", "Mar", "Feb", "Mar", "Jan"],
#     "sales": [100, 150, 200, 300, 120, 180, 50]
# })
# # df row filtering
# # print(a[a["month"] == "Jan"])
# # .groupby()
# # .groupby("col") + [col].function()
# total_sales = a.groupby("month")["sales"].sum()
# print(total_sales)
# # total_sales is a Series (not a DataFrame), so it doesn't have columns named "sales" or "month" anymore. 
# # The month names are in the index
# plt.plot(total_sales)
# plt.show()

# Q10 Grouping with Filtering and Plot
# 1. Group by category
# 2. Compute the average price per category
# 3. Filter categories whose average price is greater than 50
# 4. Plot a bar chart of the remaining categories and their average prices
# import pandas as pd
# import matplotlib.pyplot as plt
# data = {
#   "product": ["pen", "pencil", "battery", "cake"],
#   "category": ["stationery", "stationery", "others", "food"],
#   "price": [50, 40, 80, 10]
# }
# df = pd.DataFrame(data)
# # groupby, then find average
# # new_df is a series. 1 dimensional, index & values
# new_df = df.groupby("category")["price"].mean()
# # panda series boolean indexing. Vì lí do nào đó giống numpy array indexing
# # chứ ko có tài liệu giải thích
# new_df_2 = new_df[new_df > 50]
# new_df_3 = new_df[new_df <= 50]
# print(new_df_3)
# # syntax: plt.bar(x,y)
# # series.index & series.values
# plt.bar(new_df_3.index, new_df_3.values)
# plt.show()

# WEEK 11 POST CLASS EXERCISES AND CHALLENGE
# Q1 Mean and Threshold Filter (1D Array)
# Create a 1D NumPy array containing the values:
# [4, 12, 7, 25, 9, 16, 3, 20]
# Tasks:
# 1. Compute the mean of the array
# 2. Create a new array containing only values greater than the mean
# 3. Print the mean and the filtered array
# import numpy as np
# a = np.array([4, 12, 7, 25, 9, 16, 3, 20])
# print(a.mean())
# b = a[a > a.mean()]
# print(b)

# Q2 Create a 1D NumPy array with values from 10 to 30 (inclusive).
# Tasks:
# 1. Select elements at odd indices
# 2. Select elements at even indices
# 3. Print both resulting arrays
# import numpy as np
# a = np.array(range(10,31))
# odd_array = a[a % 2 == 1]
# even_array = a[a % 2 == 0]
# print(odd_array)
# print(even_array)

# Q3 Row-wise Computation (2D Array)
# import numpy as np
# a = np.array(
#     [[10, 20, 30],
#     [5, 15, 25],
#     [2, 4, 6],
#     [7, 14, 21]]
# )
# # sum of each row, 0 - 3
# print(a[0].sum())
# print(a[1].sum())
# # mean of each row, 0 - 3
# # print(a[0].mean())
# # print(a[1].mean())
# # sum of each col, 0 - 2
# print(a[:,0].sum())
# # mean of each row, 0 - 3

# Q4 Conditional Replacement
# Create a 2D NumPy array with shape (4, 4) containing integers from 1 to 16.
# 1. Replace all values divisible by 3 with -1
# 2. Count how many values were replaced
# 3. Print the modified array and the count
# import numpy as np
# # arrange and reshape
# a = np.arange(1, 17).reshape(4, 4)
# # Python array assignment syntax
# a[a % 3 == 0] = -1
# # Easy to use len(). All the values to count has changed to -1
# count = len(a[a == -1])
# print(a)
# print(count)
# # 1. Create a mask for values divisible by 3
# mask = (a % 3 == 0)
# # 2. Count how many values will be replaced
# count = np.sum(mask)
    

    






