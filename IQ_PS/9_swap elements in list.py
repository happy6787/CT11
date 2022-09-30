#9_How to swap any two elements in the list?

# mylist  = [10,20,30,40,50]

# posOne = 1
# posTwo = 4

# posOneElement = mylist[posOne]
# posTwoElement = mylist[posTwo]

# mylist[posOne] = posTwoElement
# mylist[posTwo] = posOneElement

# print(mylist)

######################################################################################

# list = [6, 2, 7, 8]
# print('list before swapping:', list)
# list[1], list[3] = list[3], list[1]
# print('list after swapping:', list)

######################################################################################

list = [6, 2, 7, 8, 5, 9, 10, 3, ]
print('list before swapping:', list)
for i,j in [(0,3),(4,6)]:
    list[i], list[j] = list[j], list[i]
print('list after swapping:', list)

######################################################################################