#6. How to find maximum and minimum elements in an array?.

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
# to get position
list1 = [10, 20, 1, 45, 99]

# min element's position/index
min = list1.index(min(list1))
 
# max element's position/index
max = list1.index(max(list1))
 
# printing the position/index of min and max elements
print("position of minimum element: ", min)
print("position of maximum element: ", max)

##################################################################################

arr = [10, 89, 9, 56, 4, 80, 8]
mini = arr[0]
maxi = arr[0]

for i in range(len(arr)):
  if arr[i] < mini: mini = arr[i] 
  
  if arr[i] > maxi: maxi = arr[i]

print (mini)
print (maxi)

##################################################################################

arr = [12, 1234, 45, 67, 1]
n = len(arr)

def getMin(arr, n):
    res = arr[0]
    for i in range(1,n):
        res = min(res, arr[i])
    return res
 
# Maximum Function
def getMax(arr, n):
    res = arr[0]
    for i in range(1,n):
        res = max(res, arr[i])
    return res
 
# Driver Program

print ("Minimum element of array:", getMin(arr, n))
print ("Maximum element of array:", getMax(arr, n))
 