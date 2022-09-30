# def isadult(age):
#     if age > 18:
#         return True
#     else:
#         return False

# print(isadult(20))

################################################################################

## syntax of lambda

# lambda agruments : expression

# ### when return type of lambda is boolean
# lambda age : age > 18

# #print((lambda age : age > 18) (18))   ### the way to execute while defining

# isadult = lambda age : age > 18
# print("is adult(16) : ",isadult(16))
# print("is adult(17) : ",isadult(17))
# print("is adult(18) : ",isadult(18))
# print("is adult(19) : ",isadult(19))
# print("is adult(20) : ",isadult(20))

# #########################################################################################

# ### when return type of lambda is not boolean

# # True = adult : False = minor

# isadultstr = lambda age :"adult" if age > 18 else "minor"
# print("is adultstr(16) : ",isadultstr(16))
# print("is adultstr(17) : ",isadultstr(17))
# print("is adultstr(18) : ",isadultstr(18))
# print("is adultstr(19) : ",isadultstr(19))
# print("is adultstr(20) : ",isadultstr(20))

# ###########################################################################################

# #listnumber[10,20,25,35,45,15,30]

# listnumber = [[10,20],[25,35],[45,15],[30,44]]
# listnumber.sort()
# print(listnumber) ### will sort based on first element

# listnumber.sort(key=lambda b : b[1])
# print(listnumber) ### will sort based on second element as we gave b[1] as index

###########################################################################################

### filter() function


# listnumber = [10,20,25,35,45,15,30]

# newlistodd=list(filter(lambda a:(a%2 != 0),listnumber)) ###odd list
# newlisteven=list(filter(lambda a:(a%2 == 0),listnumber)) ###even list
# print(newlistodd , newlisteven)

# ####################################

# tempList = ['asdf','hello','credence','Never be overconfident','be confident', 'dont forget roots ever'] 

# newList = list(filter(lambda item : "a" in item, tempList) )
# print(newList)

###########################################################################################

### map() function

# tempList = ['asdf','hello','credence','Never be overconfident','be confident', 'dont forget roots ever'] 

# newList = list(map(lambda item : "a" in item, tempList) )
# print(newList)


# listnumber = [10,20,25,35,45,15,30]

# newlistodd=list(map(lambda a:(a*2),listnumber)) ###odd list
# newlisteven=list(map(lambda a:(a*6),listnumber)) ###even list
# print(newlistodd , newlisteven)

###########################################################################################

# reduce() function

# from functools  import *
# listnumber = [10,20,25,35,45,15,30]

# newlist=reduce(lambda a,b:(a+b),listnumber)
# newlistinto=reduce(lambda a,b:(a-b),listnumber) 
# print(newlist , newlistinto)

###########################################################################################

##List Comprehension

h_letters = [ letter for letter in 'happyisagoodboy' ]
print( h_letters)

numlisteven = [x for x in range(20)if x % 2 == 0]
numlistadd = [x for x in range(20)if x % 2 != 0]        ### works same as filter    
numlistsq = [x*x for x in range(21)]                    #### works same as map
print(numlisteven)
print(numlistadd)
print(numlistsq)

