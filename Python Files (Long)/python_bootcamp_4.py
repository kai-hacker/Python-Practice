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
    