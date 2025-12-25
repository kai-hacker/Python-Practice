'''
Write a Python program to calculate a dog's age in dog years.

Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

Expected Output:

Input a dog's age in human years: 15                                    
The dog's age in dog's years is 73
'''
human_years = int(input("Input a dog's age in human years: "))
if human_years <= 2:
    print(f"The dog's age in dog's years is {human_years*10.5}")
else:
    print(f"The dog's age in dog's years is {int(2*10.5+(human_years-2)*4)}")