#### sort into ascending order(deafult)

# a=[10,12,15,8,9,20,23,"happy"]  #### either int or str can be used and not both at a time
# a.sort()             #### print(a.sort()) is not possible as it will display "None".... (MUTUABLE DATA TYPE)
#                            #because sort function khud  ko hi sort kar dega same variable me
# print(a)

# b=["happy","is","good"]
# b.sort()
# print(b)

# #-----------------------------------------
# ### decending order
# a=[10,12,15,8,9,20,23]
# a.sort(reverse=True)            ####"True" nahi daalna hai qki wo string banjayega
# print(a)

#-------------------------------------------------------------------------------------------------

### reverse

# a=[10,12,15,8,9,20,23,"happy"]                          #### both str and int can be used at a time 
# print(a[::-1])    ###using indexing
# a.reverse()        ###using reverse function
# print(a)                  #### print(a.reverse()) is not possible as it will display "None"....(MUTUABLE DATA TYPE)
#                                        #because reverse function khud  ko hi reverse kar dega same variable me

# for element in a:    ### output can be seen vertically
#     print(element)

# a=["happy", "shyam", "ram"]
# (a.reverse())
# print(a)

#-------------------------------------------------------------------------------------------------------------------------------------

##An object whose internal state/CONTENT can be changed is mutable.(LISTS, SETS, DICTIONARIES,ETC) (can be altered/modified)
    #(MUTUABLE ME SEPARATE VARIABLE ME NEW/UPDATED VALUE DALNE KI ZARURAT NAI HAI)

#On the other hand, immutable doesn’t allow any change in the object/CONTENT once it has been created.( INT, STRING, TUPLES, FLOAT)
            #(cannot be altered/modified)
     #(IMMUTUABLE ME SEPARATE VARIABLE ME NEW/UPDATED VALUE DALNE PADEGAA QKI NEW/UPDATED VALUE PURANE VARIABLE ME STORE NAI HOGI)

# MUTUABLE
# l1=[10,20,30]                  #list (mutuable)
# l1[2]=50
# print(l1)

#IMMUTABLE
# l2=(10,20,30)                  #tuple(immutable)
# l2[2]=50
# print(l2)

# l3=(10)                                #int(immutable)
# l3[0]=50
# print(l3)

# l4=("happy is a good boy")                   #str(immutable)
# l4[0]=("P")
# print(l4)
             #STRING AS A WHOLE IS MUTUBALE(REPLACE FUNCTION) HOWEVER STRING ELEMENTS ARE IMMUTABLE
#-------------------------------------------------------------------------------------------------------------------------------------

#append adding int to the last

# a=[10,12,15,8,9,20,23]
# a.append(42)
# print(a)

# l4=("happy is a good boy")  ####cannot be applied on str
# l4.append("boy")
# print(l4)

#-------------------------------------------------------------------------------------------------------------------------------------

#insert #This will add 8 at 3 index and rest items will shift index by 1

# a=[10,12,15,8,9,20,23]
# a.insert(3,99)
# print(a)

# l4=("happy is a good boy")  ####cannot be applied on str
# l4.insert(5,"boy")
# print(l4)

#-------------------------------------------------------------------------------------------------------------------------------------

# remove(21) – It will remove 9 from the list (will remove first occurance)

# a=[10,12,15,8,9,20,23,9]
# a.remove(9)
# print(a)

# l4=("happy is a good boy")  ####cannot be applied on str
# l4.remove("is")
# print(l4)

#-------------------------------------------------------------------------------------------------------------------------------------

### pop >>> remove last element from existing list

# a=[10,12,15,8,9,20,23,9]
# a.pop()    #by default it take default last index if not provided
# print(a)

# a=[10,12,15,8,9,20,23,9]
# a.pop(2)   #It will delete the element at index 2 and return its value
# print(a)

# take second element for sort
# def takeSecond(elem):
#     return elem[1]

# # random list
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# # sort list with key
# random.sort(key=takeSecond)

# # print list
# print('Sorted list:', random)