'''
Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
Expected Output:

Input the month (e.g. January, February etc.): july                     
Input the day: 31                                                       
Season is autumn  
'''
# Request input from the user for the name of the month and assign it to the variable 'month'
month = input("Input the month (e.g. January, February etc.): ")

# Request input from the user for the day and convert it to an integer, assigning it to the variable 'day'
day = int(input("Input the day: "))

# Check the input 'month' to determine the season based on the month and day provided

# Check if the input month falls within the winter season
if month in ('January', 'February', 'March'):
    season = 'winter'
# Check if the input month falls within the spring season
elif month in ('April', 'May', 'June'):
    season = 'spring'
# Check if the input month falls within the summer season
elif month in ('July', 'August', 'September'):
    season = 'summer'
# For other months, assign the season as autumn by default
else:
    season = 'autumn'

# Adjust the season based on the specific day within certain months

# Check if the input month is March and the day is after March 19, updating the season to spring
if (month == 'March') and (day > 19):
    season = 'spring'
# Check if the input month is June and the day is after June 20, updating the season to summer
elif (month == 'June') and (day > 20):
    season = 'summer'
# Check if the input month is September and the day is after September 21, updating the season to autumn
elif (month == 'September') and (day > 21):
    season = 'autumn'
# Check if the input month is December and the day is after December 20, updating the season to winter
elif (month == 'December') and (day > 20):
    season = 'winter'

# Display the determined season based on the provided month and day
print("Season is", season) 