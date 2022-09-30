##ADDITION OF TWO NUMBERS####
# a=10
# b=20
# result=(a+b)
# print(result)

####---------------------------------------------------------------------------------

###INPUT FUNCTION IS USED TO TAKE OR ACCEPT INPUTS FROM USER IN REAL TIME 
### IT ONLY ACCEPTS INPUT TYPE AS "STRING"

####---------------------------------------------------------------------------------

# a=input()
# b=input()
# result=a+b
# print(result)

####--------------------------------------------------------------------------------

# a=input()
# b=input()
# result=int(a+b)           ####will not work as it will convert contatination of a&b into string (10101010)
# print(result)

####---------------------------------------------------------------------------------

# a=input()
# b=input()
# result=int(a)+int(b) 
# print(result)

####---------------------------------------------------------------------------------

# a=input("enter first number:")
# b=input("enter second number:")
# result=int(a)+int(b)   ### result will not change the type of a and b but for sake of calculation purpose it will convert value into int 
# print(result)

####---------------------------------------------------------------------------------

# a=input("enter first number:")
# b=input("enter second number:")

# a=int(a) 
# b=int(b)

# result=a+b        ### here result got a&b into int type only as we have already changed there type above line no (45/46)
# print(result)

####---------------------------------------------------------------------------------

# a=int(input("enter first number:"))
# b=int(input("enter second number:"))

# result=a+b      
# print(result)

####---------------------------------------------------------------------------------

# print("Addition of Two Numbers")
# result=(int(input("enter first number:"))+int(input("enter second number:")))

# print(result)

####---------------------------------------------------------------------------------


print("Addition of Two Numbers:",int(input("enter first number:"))+int(input("enter second number:")))


