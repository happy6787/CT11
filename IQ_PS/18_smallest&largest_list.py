# list of numbers
list1 = [10, 20, 1, 45, 99]
 
 
# printing the maximum element
print("Smallest element is:", min(list1))
print("Smallest element is:", max(list1))

##################################################################################

list1 = [10, 20, 1, 45, 99]
list1.sort() 
 
# printing the maximum element
print("Smallest element is:", list1[0])
print("Smallest element is:", list1[-1])

##################################################################################

# Python program to find smallest
# number in a list
 
# creating empty list
# list1 = []
 
# # asking number of elements to put in list
# num = int(input("Enter number of elements in list: "))
 
# # iterating till num to append elements in list
# for i in range(1, num + 1):
#     ele= int(input("Enter elements: "))
#     list1.append(ele)
     
# # print maximum element
# print("Smallest element is:", min(list1))
# print("Smallest element is:", max(list1))
##################################################################################

# l=[ int(l) for l in input("List:").split(",")]
# print("The list is ",l)
 
# Assign first element as a minimum.10 20 3
# min1 = l[0]
# max1 = l[0]
# for i in range(len(l)):
 
#     # If the other element is min than first element
#     if l[i] < min1:
#         min1 = l[i] #It will change
#     if l[i] > max1:
#         max1 = l[i]
 
# print("The smallest element in the list is ",min1)
# print("The largest element in the list is ",max1)