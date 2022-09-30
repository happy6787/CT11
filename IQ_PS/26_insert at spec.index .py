list1 = ['city', 'Hi', 'hello', 'at', 'why', 'this', 'there', 'from']
list2 = [3,5,7,1]

list1 = list1[:3] + list2 + list1[3:]
print(list1)
     
#######################################################################################

list3 = ['city', 'Hi', 'hello', 'at', 'why', 'this', 'there', 'from']
list4 = [3,5,7,1]

 # Insert all the elements in list2 to list1 between 3 to 4 th element
for elem in reversed(list4) :
    list3.insert(3, elem)
    # Print the List
print(list3)         