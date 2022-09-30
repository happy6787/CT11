#3_How to find factorial of a number 

#0will not work with 0
num = int(input("Enter the number: "))
factorial = 1
for i in range(1,num+1):
        factorial = factorial * i
 
print("The factorial is: ",factorial)

###############################################################################


import math

num = int(input("Enter the number: "))
print("The factorial is: ")
print (math.factorial (num))

###############################################################################
