# time=7.15
# if time==7.15:
#     print('join class')
# else: 
#     print("sleep")


# time=7.10
# if time>=7.15:
#     print('join class')
# else: 
#     print("sleep")


# time=7.14                               ###only if condition (without else)
# if time>=7.15 and time<=9:
#     print('join class')



# time=7.16
# if time>=7.15:                            ### if body  
#     print('join class')
# else:                                     ### else body          
#     print("sleep")
# print("relax")                           ### will get "relax" in result because it is out of if-else statement (indentation)


### we cannot have only else statement without if statement
### only if condition will work but only else condition will not work


####----------------------------------------------------------------------------------------------
### Multiple If statements

# a=10                      #if me sare if conditions pe jayega and end me jo true hai wo return karega
# if  a>10:                 # jab multiple conditions check karni ho tab if use karo
#     print("greater")
# if a==10:
#     print("equals to")
# if a<10:
#     print("lesser")    
# else:                       ## this else statement is only associated with if statement ("a<10") and not common to all if statements 
#     print("happy")

# ####----------------------------------------------------
# ### elif                     elif me jaise hi result True aata hai; waha se uske aage program run nai hoga 
# a=10                        #agar Flase aayega to hi next elif pe jayega nai to true wala return kar dega               
# if  a>10:
#     print("greater")            #jab ek hi condition check karni ho or result lana ho tab elif use karo  
# elif a==10:
#     print("equals to")
# elif a<10:
#     print("lesser")    
# else:                             # elif me else statement common hota hai as compare to if statement
#     print("happy")  

####----------------------------------------------------
# day=input("day ")
# if day == "Monday" or day == "monday":
#     print("today is Monday")
# elif day=="Tuesday":
#     print("today is Tuesday")
# else:
#     print("today is Holiday")    
