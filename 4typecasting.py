a=15
print(a+int('10'))

a='15'
print(a+str(10))

a=1.5
print(a+int(float('5')))

a=1.5
print(a+float(int('5')))

a=10
b=12.5
print(a+b)

### INTERGER AND FLOAT HAVING PARTIAL COMPATIBILITY ###
### RESULT WILL ALWAYS BE IN FLOAT ###

a=10
b="12.5"
print(a+int(float(b)))

### WE CANNOT CONVERT STRING HAVING FLOAT VALUE DIRECTLY INTO INTERGER   ####

a=10.5
b=44
print(b-a)

# a=10dfd
# b=15
# print(a+b)
### any string can be converted into integer only if it is a valid number ####

a=True
a=bool(a)
print(a)
print(type(a))

a="False"        #### BOOLEAN RETURNS FALSE ONLY FOR EMPTY STRING ###
a=bool(a)
print(a)
print(type(a))


a=""        #### BOOLEAN RETURNS FALSE ONLY FOR EMPTY STRING AND FOR ANYTHING ELSE IT WILL RETURN TRUE ###
a=bool(a)
print(a)
print(type(a))

####----------------------------------

a=eval('10.2+20.3+30.5')
print(a,type(a))

a=eval('10+20+30')
print(a,type(a))

a=eval('True')
print(a,type(a))

a=eval('False')
print(a,type(a))

#a=eval('happy')
#print(a,type(a))

a=10.1
print(eval(a),type(a))





