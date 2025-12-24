# Assessment 3: In-class Programming Challenges

# Q1: A password must satisfy all of the following conditions in this order:
# 1. It contains no spaces
# 2. It has at least 10 characters
# 3. It contains at least one uppercase letter
# 4. It contains at least one lowercase letter
# 5. It contains at least one digit
# 6. It contains at least one special character from ! @ # $ %
# islower(), isupper(), isdigit()
# or >= 'a' and <= 'z', >= 'A' and <= 'Z'
# or re.search(list, string), but not taught in class
# 
# pw = input("Enter password: ")
# # Check no space
# no_space = pw.find(" ") == -1 #True or False
# correct_length = len(pw) >= 10 #True or False
# upper_case = False #By default
# # .upper() counts digits & symbol as uppercase; 
# # char.isupper() / is supper checks whether the char, or the string, only has upper case letters
# # and works for letters only
# for char in pw:
#     if char >= 'A' and char <= 'Z':
#         upper_case = True
#         break
# lower_case = False #By default
# # .upper() counts digits & symbol as uppercase; 
# # char.isupper() / is supper checks whether the char, or the string, only has upper case letters
# # and works for letters only
# for char in pw:
#     if char >= 'a' and char <= 'z':
#         lower_case = True
#         break
# has_digit = False
# for char in pw:
#     if char.isdigit():
#         has_digit = True
#         break
# special_chars = "!@#$%" #Using a list instead would provide no extra benefits
# contain_special = any(char in special_chars for char in pw) #True or False. Use any()
# if not no_space: 
#     print("Contain space")
# elif not correct_length:
#     print("Too short")
# elif not upper_case:
#     print("Missing upper case character")
# elif not lower_case:
#     print("Missing lower case character")
# elif not has_digit:
#     print("Missing digit")
# elif not contain_special:
#     print("Missing special character")
# else:
#     print("Valid")

# Q5: Most Frequent Element
# If multiple elements have the same highest frequency, return the smallest such element.
# digits = [1, 1, 1, 8, 8, 8]
# # Solution 1: Get a dictionary of key-value pairs of digit-frequency
# # Then initialize max_digit and max_count variables, using .items() to extract the keys & values for comparision
# def most_frequent_element(numbers):
#     # Get a dictionary of key-value pairs of digit-frequency
#     digit_count = {}
#     for d in numbers:
#         digit_count[d] = digit_count.get(d, 0) + 1
#     print(digit_count)
#     max_digit = None #Initalize with no assignment
#     max_count = 0
#     for key, value in digit_count.items():
#         # Assign max_digit & max_count as first with the first pair of key-value
#         if max_digit == None:
#             max_digit = key
#             max_count = value
#         elif value > max_count:
#             max_digit = key
#             max_count = value
#         elif value == max_count and int(key) < int(max_digit):
#             max_digit = key
#             max_count = value
#     print(max_digit)
# most_frequent_element(digits)
# Solution 2: Get a list of uniques, then get a list of digit frequencies
# The lists have the same length and list2[i] is the freq of list1[i]. Make comparisions

# Lesson 10: File
# fhand = open('Python Files (Long)/mbox2.txt')

# for loop to read line by line
# line_count = 0
# for line in fhand:
#     line_count += 1
#     print(line)
# print(line_count)

# read the entire file. Should only use when file is small enough
# inp = fhand.read()
# print(inp)

# Check for information in a line
# for line in fhand:
#     if line.startswith("From"):
#         print(line)

# try and except
# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()

# open to write, write with new line, close
# fhand = open('Python Files (Long)/mbox3.txt', 'r+')
# # fhand.write("Ass\n") #\n to add a new line at the end
# # fhand.write("This should be on the next line.")
# # print(fhand.read())
# fhand.close()
# print(fhand.read()) #File is closed

# Q1: read line by line and print all in uppercase
# fname = 'Python Files (Long)/mbox2.txt'
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
# for line in fhand:
#     print(line.upper())
# inp = repr(fhand.read())
# print(inp)

# Q2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart 
# the line to extract the floating-point number on the line. Count these lines and then 
# compute the total of the spam confidence values from these lines. When you reach the end of the file,
# print out the average spam confidence.
# Before every number, there's a space, so look for the index of that final space

# filename = input("Enter the file name: ") # Python Files (Long)/mbox.txt
# try:
#     fname = open(filename)
# except:
#      print('File cannot be opened:', filename)
# count = 0
# sum = 0
# for line in fname:
#     if line.startswith("X-DSPAM-Confidence:"):
#         count += 1
#         final_space_index = line.rfind(" ")
#         sum += float(line[final_space_index+1:])
# print(f"Count: {count}. Sum: {sum}. Average: {sum / count}")

# Q3: prints a funny message when the user types in the exact file name "na na boo boo". 
# filename = input("Enter the file name: ")
# try:
#     fname = open(filename)
# except:
#     if filename == "na na boo boo":
#         print("NA NA BOO BOO TO YOU - You have been punk'd!")
#     else: 
#         print('File cannot be opened:', filename)

# W3RESOURCES Python Conditional Statements and loops
# Q2: Write a Python program to read first n lines of a file.
fname = 'Python Files (Long)/mbox2.txt'
# Solution 1:
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
n = int(input("> "))
count = 0
for line in fhand:
    # r.strip() removes the extra line
    print(line.rstrip())
    count += 1
    if count == n:
        break

# Solution 2
try:
    # try, with, as
    # with open(...) = open(fname), close(fname). Auto close
    with open(fname) as fhand:
        n = int(input("> "))
        # .readlines returns all the lines as a list of strings [line1, line2, ...]
        # [:] slice the list. Slice can be used with list.
        # [:n] from the 1st element to the nth element, so n number of lines
        for line in fhand.readlines()[:n]:
            print(line.rstrip())
except:
    print('File cannot be opened:', fname)



    