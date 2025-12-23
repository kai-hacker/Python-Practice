'''
Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
n = int(input("Enter a maximum edge: "))
for i in range(n):
    for j in range(i):
        print("* ", end ='')
    print('')
for i in range(n, 0, -1):
    for j in range(i):
        print("* ", end ='')
    print('')    
for i in range(0):
    print(i)