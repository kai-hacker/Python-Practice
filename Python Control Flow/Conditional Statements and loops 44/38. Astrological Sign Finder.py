'''
Write a Python program to display the astrological sign for a given date of birth.

Expected Output:

Input birthday: 15                                                      
Input month of birth (e.g. march, july etc): may                        
Your Astrological sign is : Taurus 
'''
# Request input from the user for the day of birth and convert it to an integer, assigning it to the variable 'day'
day = int(input("Input birthday: "))

# Request input from the user for the month of birth and assign it to the variable 'month'
month = input("Input month of birth (e.g. march, july etc): ")

# Determine the astrological sign based on the provided day and month

# Check for December and assign the astrological sign as 'Sagittarius' if the day is less than 22, else 'Capricorn'
if month == 'december':
    astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
# Check for January and assign the astrological sign as 'Capricorn' if the day is less than 20, else 'Aquarius'
elif month == 'january':
    astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
# Check for February and assign the astrological sign as 'Aquarius' if the day is less than 19, else 'Pisces'
elif month == 'february':
    astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
# Check for March and assign the astrological sign as 'Pisces' if the day is less than 21, else 'Aries'
elif month == 'march':
    astro_sign = 'Pisces' if (day < 21) else 'Aries'
# Check for April and assign the astrological sign as 'Aries' if the day is less than 20, else 'Taurus'
elif month == 'april':
    astro_sign = 'Aries' if (day < 20) else 'Taurus'
# Check for May and assign the astrological sign as 'Taurus' if the day is less than 21, else 'Gemini'
elif month == 'may':
    astro_sign = 'Taurus' if (day < 21) else 'Gemini'
# Check for June and assign the astrological sign as 'Gemini' if the day is less than 21, else 'Cancer'
elif month == 'june':
    astro_sign = 'Gemini' if (day < 21) else 'Cancer'
# Check for July and assign the astrological sign as 'Cancer' if the day is less than 23, else 'Leo'
elif month == 'july':
    astro_sign = 'Cancer' if (day < 23) else 'Leo'
# Check for August and assign the astrological sign as 'Leo' if the day is less than 23, else 'Virgo'
elif month == 'august':
    astro_sign = 'Leo' if (day < 23) else 'Virgo'
# Check for September and assign the astrological sign as 'Virgo' if the day is less than 23, else 'Libra'
elif month == 'september':
    astro_sign = 'Virgo' if (day < 23) else 'Libra'
# Check for October and assign the astrological sign as 'Libra' if the day is less than 23, else 'Scorpio'
elif month == 'october':
    astro_sign = 'Libra' if (day < 23) else 'Scorpio'
# Check for November and assign the astrological sign as 'Scorpio' if the day is less than 22, else 'Sagittarius'
elif month == 'november':
    astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'

# Display the determined astrological sign based on the provided day and month of birth
print("Your Astrological sign is :", astro_sign) 