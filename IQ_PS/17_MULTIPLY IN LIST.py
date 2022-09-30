##How to multiply all the numbers in the list? 

list = [1,2,3,4,5,6,7,8]
 
res = 1
 
for i in list:
  res = res * i
   
print(res)

# ##################################################################################################################

# def multiplyList(myList):
 
#     # Multiply elements one by one
#     result = 1
#     for x in myList:
#         result = result * x
#     return result
 
 
# # Driver code
# list1 = [1, 2, 3]
# list2 = [3, 2, 4]
# print(multiplyList(list1))
# print(multiplyList(list2))

# ##################################################################################################################


# import math
# list1 = [1, 2, 3]
# list2 = [3, 2, 4]
 
 
# result1 = math.prod(list1)
# result2 = math.prod(list2)
# print(result1)
# print(result2)
# ##################################################################################################################

 
# from operator import*
# list1 = [1, 2, 3]
# m = 1
# for i in list1:
#   # multiplying all elements in the given list
#   # using mul function of operator module
#     m = mul(i, m)
# # printing the result
# print(m)

# #################################################################################################################

# # Multiply a Python List by a Number Using a for loop
# numbers = [1, 2, 3, 4, 5]
# multiplied = []
# for number in numbers:
#     multiplied.append(number * 2)
# print(multiplied)

#################################################################################################################

nums = []
print("Enter 5 Numbers: ")
for i in range(5):
  nums.append(int(input()))
mul = 1
for i in range(5):
  mul = mul*nums[i]
print("\nMultiplication Result: ")
print(mul)

#################################################################################################################

