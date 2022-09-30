
# def happy(a):
#     return(a.upper())   ##return will give back back a vlaue as soon as it is executed
#     a="any command after return will be unreachable"    
# #option 1------------
# print(happy(a="niknav"))

# #option 2------------
# result=happy(a="niknav")
# print(result)
# print("Upper value is:",result)
# #print("test case result ?:", "NIKNAV" is result)
# print("test case result ?:", "NIKNAV" == result)

# print(id(result))
# print(id("NIKNAV"))

####----------------------------------------------------------------------------------------------

def happy(a="world"):
    return "hello " + (a.upper())   ##return will give back back a vlaue as soon as it is executed
result=happy(a="niknav")
print(happy())      #if no argument is given to to function it will print default("world")
print(happy("niknav"))   #if argument is given to to function it will print the argument("niknav")

####----------------------------------------------------------------------------------------------

