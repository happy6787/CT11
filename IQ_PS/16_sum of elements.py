# #16. Find the sum of the elements in list

# list1 = [11, 5, 17, 18, 23]
 
# # using sum() function
# total = sum(list1)
 
# # printing total value
# print("Sum of all elements in given list: ", total)

##################################################################################################################

list = [1,2,3,4,5,6,7,8]
 
res = 0
 
for i in list:
  res = res + i
   
print(res)

# # ##################################################################################################################

# def addList(myList):
 
#     # add elements one by one
#     result = 0
#     for x in myList:
#         result = result + x
#     return result
  
# # Driver code
# list1 = [1, 2, 3]
# list2 = [3, 2, 4]
# print(addList(list1))
# print(addList(list2))

# # #################################################################################################################

# from operator import*
# list1 = [12, 15, 3, 10]
# result = 0
# for i in list1:
#   # Adding elements in the list using
#   # add function of operator module
#     result = add(i, 0)+result
# # printing the result
# print(result)

#################################################################################################################

# NumList = []
# total = 0

# Number = int(input("Please enter the Length : "))
# for i in range(1, Number + 1):
#     value = int(input("Please enter the Value : "))
#     NumList.append(value)

# for j in range(Number):
#     total = total + NumList[j]

# print("\n The Sum of All Element in this List is : ", total)

#################################################################################################################

