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

