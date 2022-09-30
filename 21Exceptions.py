#print("happy")
#Print("happy")          #NameError: name 'Print' is not defined. SYNTAX ERROR (Error)


# a=[10,20,30,40,50]
# print(a[1])
# print(a[6])                ##IndexError: list index out of range. CORRECT SYNTAX (Exception)

#####################################################################################################

# a=[10,20,30,40,50]
# try:
#     print(a[1])
#     print(a[6])         ###Runtime Exception
#     print(a[3])         ### this statement will not be executed as exception has occured before this statement
# except:
#     print("given index not available")          ### line 14 pe program break hua isliye except print hua
#     print("something is wrong")

##############################################################################################################

# a=[10,20,30,40,50]
# try:
#     print(a[1])
    
#     try:
#         print(a[6])         ###Runtime Exception
#     except:
#         print("index 6 not available")

#     print(a[3])         ### this statement will not be executed as exception has occured before this statement
#     except:                       ### GENERIC EXCEEPTION BLOCK but isme hmko error kya wo pata nai chalega
#     print("given index not available")    #line 27 pe program break nahi hua isliye except bhi print nahi hua
#     print("something is wrong")

######################################################################################################################

# a=[10,20,30,40,50]
# try:
#     print(a[1])
#     print(a[6])         ###Runtime Exception
#     print(a[3])         ### this statement will not be executed as exception has occured before this statement
# except IndexError as obj:     ###exception gives with class and object
#     print(obj)         
#     print("something is wrong")

#######################################################

#from tkinter import EXCEPTION
### sab ka baap exception

# a=[10,20,30,40,50]
# try:
#     print(a[1])
#     print(a[6])         ###Runtime Exception
#     print(a[3])         ### this statement will not be executed as exception has occured before this statement
# except EXCEPTION as obj:     ### GENERIC EXCEPTION BLOCK
#     print(obj)         
#     print("something is wrong")

##############################################################################################################
### sab ka baap exception

# a=[10,20,30,40,50,10,20,30,40,50]
# try:
#     userinput=int(input("enter any nummber"))
#     result=100/userinput
#     print(a[userinput])
#     print(result)

# except ZeroDivisionError as obj:
#     print(obj)
# except Exception as obj:            ### WE SHOULLD BE WRITING EXCEPTION BLOCK ALWAYS AT THE END
#     print(obj)
# except ValueError as obj:   
#     print(obj)                  ### this block will never execute as above there is exception block; all errors
#                                         #  except zerodivisionerror will be handled by exception block 

# print("all well")        

#################################################################################################################
## raise exception

# a=[10,20,30,40,50,10,20,30,40,50]
# try:
#     userinput=int(input("enter any nummber"))
#     result=100/userinput
#     raise ZeroDivisionError   #agar input galat dala ya condition ke hisab se nai dala to code raise pe hi atak jayega and error bata dega
#     print(result)

# except ValueError as obj:   
#     print(obj)                  ### this block will never execute as above there is exception block; all errors
#                                         #  except zerodivisionerror will be handled by exception block 

# print("all well")        

#################################################################################################################################

#else and finally

#try
#except
#else                #agar exception nai hota hai koi to else print hoga and we cannot have only else block
#finally            ### FINALLY WILL BE EXECUTED REGARDLESS OF EXCEPTION OCCURED OR NOT