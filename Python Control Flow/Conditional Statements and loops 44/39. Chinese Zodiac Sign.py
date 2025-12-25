'''
Write a Python program to display the sign of the Chinese Zodiac for the given year in which you were born.

Expected Output:

Input your birth year: 1973                                             
Your Zodiac sign : Ox  
'''
# Request input from the user for the birth year and convert it to an integer, assigning it to the variable 'year'
year = int(input("Input your birth year: "))

# Determine the Chinese zodiac sign based on the provided birth year

# Check if the year corresponds to the Chinese zodiac sign 'Dragon'
if (year - 2000) % 12 == 0:
    sign = 'Dragon'
# Check if the year corresponds to the Chinese zodiac sign 'Snake'
elif (year - 2000) % 12 == 1:
    sign = 'Snake'
# Check if the year corresponds to the Chinese zodiac sign 'Horse'
elif (year - 2000) % 12 == 2:
    sign = 'Horse'
# Check if the year corresponds to the Chinese zodiac sign 'Sheep'
elif (year - 2000) % 12 == 3:
    sign = 'Sheep'
# Check if the year corresponds to the Chinese zodiac sign 'Monkey'
elif (year - 2000) % 12 == 4:
    sign = 'Monkey'
# Check if the year corresponds to the Chinese zodiac sign 'Rooster'
elif (year - 2000) % 12 == 5:
    sign = 'Rooster'
# Check if the year corresponds to the Chinese zodiac sign 'Dog'
elif (year - 2000) % 12 == 6:
    sign = 'Dog'
# Check if the year corresponds to the Chinese zodiac sign 'Pig'
elif (year - 2000) % 12 == 7:
    sign = 'Pig'
# Check if the year corresponds to the Chinese zodiac sign 'Rat'
elif (year - 2000) % 12 == 8:
    sign = 'Rat'
# Check if the year corresponds to the Chinese zodiac sign 'Ox'
elif (year - 2000) % 12 == 9:
    sign = 'Ox'
# Check if the year corresponds to the Chinese zodiac sign 'Tiger'
elif (year - 2000) % 12 == 10:
    sign = 'Tiger'
# If the year doesn't correspond to any specific sign, assign it to 'Hare'
else:
    sign = 'Hare'

# Display the determined Chinese zodiac sign based on the provided birth year
print("Your Zodiac sign :", sign) 