'''
Docstring for 2. Temperature Converter
Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

Expected Output :

60°C is 140 in Fahrenheit
45°F is 7 in Celsius
'''
user_text = input("Enter type of temperatures [C or F]: ").strip()
user_num = int(input("Enter a number of temperatures to convert: ").strip())

if (user_text.upper() == "C"):
    F = int(user_num*9/5 + 32)
    print(f"{user_num}°C is {F} in Fahrenheit")
elif (user_text.upper() == "F"):
    C = int((user_num - 32)/9 * 5)
    print(f"{user_num}°F is {C} in Celsius")
else:
    print("Invalid input")