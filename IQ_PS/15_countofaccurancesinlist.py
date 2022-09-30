#15. How to count occurrences of an element in a list?

# Alist = ['Mon', 'Wed', 'Mon', 'Tue', 'Thu']
# cnt = Alist.count('Mon')
# print("Number of times the element is present in list:\n",cnt)

#################################################################################################################

from collections import Counter

# blist=[1,1,2,3,5,5,4,6,9,9,5,1,6,6,6]   #list
# d=dict(Counter(blist))
# print (d)


#################################################################################################################

# def get_count(lst, num):
#     return lst.count(num)
    
# my_list = ['Mon', 'Wed', 'Mon', 'Tue', 'Thu']
# num = 'Mon'
# print(f'Count of {num} has occurred {get_count(my_list, num)} times')

#################################################################################################################

# names=['Deepak','Reema','John','Deepak','Munna','Reema','Deepak','Amit','John','Reema','Happy']
# nameset=set(names)
# d={name:names.count(name) for name in nameset}
# print(d)

#################################################################################################################

# names=['Deepak','Reema','John','Deepak','Munna','Reema','Deepak','Amit','John','Reema','Happy']
# d=dict(Counter(names))
# print (d)

#################################################################################################################

