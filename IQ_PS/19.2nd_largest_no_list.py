#19. How to find the second largest number in a list?

# a=[10,20,30]
# print(a)
# print(min(a))
# print(max(a))
# ##########################
# a=min(10,20,30)
# print(a)
# ##########################

# a=[10,20,30]
# a.remove(max(a))
# print(max(a))

########################################################################################################
# a=[10, 20, 4, 45, 99]
# a.sort()
# print(a)
# print(a[-2])

########################################################################################################

# a=[10, 20, 4, 45, 99,10, 20, 4, 45, 99,55,58,89,74,10, 20, 4, 45, 99]
# a=list(set(a))
# a.sort()   ###sort canges original list whereas sorted() will not
# print(a[-2])

########################################################################################################

# a=[]
# n=int(input("Enter number of elements:"))
# for i in range(1,n+1):
#     b=int(input("Enter element:"))
#     a.append(b)
# a.sort()
# print("Second largest element is:",a[n-2])

########################################################################################################

# list_of_numbers = [2, 1, 9, 8, 6, 3, 1, 0, 4, 5]
  
# def findSecondLargest(lst):
#     firstLargest = max(lst[0],lst[1])
#     secondLargest = min(lst[0],lst[1])
#     for i in range(2,len(lst)):
#         if lst[i] > firstLargest:
#             secondLargest = firstLargest
#             firstLargest =lst[i]
#         elif lst[i] > secondLargest and firstLargest > lst[i]:
#             secondLargest = lst[i]
#     return secondLargest

# print(findSecondLargest(list_of_numbers))

########################################################################################################
