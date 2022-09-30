#OPERAND VALUES OTHER THAN OPERATORS (A+B>> A&B ARE OPERAND)


###ARTITHMATIC OPERATOR###
# print("5 + 5 is ", 5+5)
# print("15 - 5 is ", 15-5)
# print("5 * 5 is ", 5*5)
# print("5 ** 3 is ", 5**3)   #exponential operator(raise to the power)
# print("20 / 5 is ", 20/5)
# print("28 // 5 is ", 28//5)  #double divide shows only integer and not decimal
#print("32 % 5 is ", 32%5)   #moduls oprator shows only remainder
#print("-28 // -5 is ", 28//5)
####--------------------------------------------------================================================

# ###ASSIGNMENT OPERATOR###
# # ALWAYS WATCH FOR RIGHT SIDE OF EQUALS TO(=).... AND ASSIGN THE LEFT VALUE TO THE RIGHT VARIABLE

# a=10
# print(a)

# a+=7
# print(a)

# a-=8
# print(a)

# a/=2
# print(a)

# a*=2
# print(int(a))

######_------------------------------=================================================------------
###COMPARISION OPERATORS###########
#COMPARISION OPERATOR WILL WORK ON BOOLEAN (TRUE/FALSE); BUT IF THERE ARE DIGITS, PYTHON WILL TREAT THEM AS BOOLEAN

# a=10
# print(a!=5)

# a=10
# print(a==5)

# a=10
# print(a<=5)

# a=10
# print(a>=5)

# a=10
# print(a>5)

# a=10
# print(a<5)

####----------------------------------------------------=======================================\
###LOGICAL OPERATORS#####
# a=10
# b=100
# print(a and b)  ### and will result in 2nd value as it need to satisfy both conditions
# print(a or b)   ### or will result in 1st value as it needs to satisfy only one condition 
###---------------------

# a=True
# b=False

# print(a and b)
# print(a or b)


# print(True and False)
# print(True or False)

a=10   #python will consider as True
b=20   #python will consider as True

print(a == b or b == 20)    #True
print(a == b and b == 10)   #False
print(a == 10 and a == b)   #False
print(a == b or b == 10)    #False

### "OR" K CASE ME AGAR PEHLE TRUE HAI TO AGE CHECK NAI KIYA JAYEGA....RESULT WILL BE "TRUE"
### "AND" K CASE ME EK B FLASE RAHA TO RESULT "FALSE" DEGA

#####------------------=-==-=-======================================---------------------------------
####IDENTITY OPERATORS#################
# a=5
# print(5 is a)

# a=5
# print(5 is not a)

######------------------=-==-=-======================================---------------------------------
####MEMBERSHIP OPERTAOR#################
# list = {10,20,30,40,50}
# print(600 not in list)

# list = {10,20,30,40,50}
# print(60 in list)


