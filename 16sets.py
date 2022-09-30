# a=[10,]
# print(a,type(a))

# a={20}
# print(a,type(a))

##########################################################################################

##SETS

###It can have any number of items and they may be of different types (integer, float, tuple, string etc.). 
# But a set cannot have mutable elements like lists, sets or dictionaries as its elements.

# a={"happy","raj", 10.25,True,{'id':42}}
# print(a,type(a))

# a={}                    ### empty curly brace >>> dictionary
# print(a,type(a))


# a={10,20,30,25,15,5,10,20}
# print(a,type(a))        ### will not print duplicate values
# print(len(a))       ### length for sets will not consider duplicate values
# #print(a[1])         ### unindexed
# a[1]=42
# print(a)            ###immutable >>> elements cannot be changes

##########################################################################################

# a={10,20,30,25,15,5,10,2052,49,86,77,16,8,59,99,21,39}
# b={10,20,21,39,59,99}
# d={1,2,3}
#print(len(a))
#print(a.remove(2052))           ### removes defined element from list; if not there, will get key error
#print(a.pop())          ### removes rendon element from list and returns it
#print(a.clear()         ### clear the set(empty)
#c=(a.union(a,b))        ### Returns a new set with all items from both sets except duplicates or repitation
#print(c,len(c))
#print(a.intersection(a,b))          ### will return common from both sets
#print(a.add(111),a,len(a))          ### will add new element in sets
#print(a.copy())                 ### will return set itself (copy)
#print(b.difference(a))    ###returns items only in first sets and not in both sets(jo a & b me common hai wo cchod k baki b wale sab lega)
#print(a.difference(b))    ###returns items only in first sets and not in both sets(jo a & b me common hai wo cchod k baki a wale sab lega)
#print(a.issubset(b))        ### will return true if all items of a exists in b else false
#print(b.issubset(a))            ### will return true if all items of a exists in b else false
#print(a.issuperset(b))       ### will return true if all elemnts of b are there is a else false
#print(a.isdisjoint(d))      ### will return true if no common element is found else false
#print(a.discard(10))        ### will remove defined element from set
#print(a.discard(444))       ### if out of set element is defined it will show none

###########################################################################################################################################

# employees = [
#                 [101, 'Firoj','Pune'],
#                 [102, 'Ajay','Pune'],
#                 [103, 'Arpan','Delhi'],
#                 [104, 'Elon','Pune'],
#                 [105, 'Obama','Mumbai'],
#                 [106, 'Putin','Pune']
#             ]

# print(employees[5])
# print(employees[4][1])



# employees = {
#                 101 : [101, 'Firoj','Pune'],
#                 102 : [102, 'Ajay','Pune'],
#                 103 : [103, 'Arpan','Delhi'],
#                 104 : [104, 'Elon','Pune'],
#                 105 : [105, 'Obama','Mumbai'],
#                 106 : [106, 'Putin','Pune']}

# print(employees[105])

#######################################################################################

# a=[10, 20, 4, 45, 99,10, 20, 4, 45, 99,55,58,89,74,10, 20, 4, 45, 99]
# b=enumerate(a)      #dds a counter to an iterable and returns it (the enumerate object).
# print(list(b))

# a,b,c,d=1,2,3,4
# print(b)

# x=2.5
# print(type(x))

# a="happy is agood boy"
# #print(a.())
x = 50
def fun1():
    x = 25
    print(x)
    
fun1()
print(x)

aTuple = (1, 'Jhon', 1+3j)
print(type(aTuple[2:3]))

print(type(0xFF))

print('any'.encode())