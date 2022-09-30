#How to reverse a list?

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

###########################################################################

# # input list
# lst = [10, 11, 12, 13, 14, 15]
# # the above input can also be given as
# #lst=list(map(int,input().split()))
# l = []  # empty list
 
# # iterate to reverse the list
# for i in lst:
#     # reversing the list
#     l.insert(0, i)
# # printing result
# print(l)

###################################################################################

# Operating System List
systems = [10,20,30,40]

# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)