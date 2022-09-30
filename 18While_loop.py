#a loop is a sequence of instruction s that is continually repeated until a certain condition is reached. 


#while condition:
##     body

# while True:           ###infinite loop
#     print("Niknav")

####----------------------------------------------------------------------------

# a=1
# while a<=5:                   ### will get infinite output as condition is "True" (a=1 is less than or equal to 5)
#     print("niknav")

# ####------------------------------

# a=6
# while a<=5:                   ### will get no result as condition is not staisfied (a=6 is greater than 5)/program will stop
#     print("niknav")


# ####------------------------------

# a=4
# while a<=5:                 
#     print("niknav")
#     a=a+1               # we will get results two times as a=4 and max a can be a=5 so (a=a+1:a=4=niknav) and (a=a+1=4+1=5=niknav)

# ####------------------------------

# a=10
# b=1
# while b<=10:
#     print(a*b)
#     b=b+1         # incremental condition
    
# ####------------------------------

# a=10
# b=1
# while b==10:       ### will not run as b=1 so condition b==10 is not satisfied.
#     print(a*b)
#     b=b+2         # incremental condition
    
####--------------------------------------------------------------------------------------------

from typing import Counter


# counter=100
# while counter:          ###non zero value will be considered as true
#     print(counter)
#     counter = 0             ##setting counter to 0 so loop will execute 1 
    
# list=[10,20,30,25,15,5]
# counter=0
# while counter < len(list) :      ##counter <= len(list)-1 or    counter < len(list)
#     print(list[counter])            ## this is nothing but print(a[index])
#     counter +=1  


 

