'''
Write a Python program to convert a month name to a number of days.

Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December                                
Input the name of Month: February                                       
No. of days: 28/29 days 
'''
months =["January", "February", "March", "April", "May", "June", "July", "August"
, "September", "October", "November", "December"]
for i in range(12):
    months[i] = months[i].lower()

days = [31,"28/29",31,30,31,30,31,31,30,31,30,31]
months_days = dict(zip(months,days))
input_m = input("Input the name of Month: ").strip()
input_m = input_m.lower()
print(f"No. of days: {months_days[input_m]} days")
