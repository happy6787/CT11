#14_How to clone or copy a list?

### Deep Copy means that any changes made to a copy of the object do not reflect in the original object. 
### Shallow copy eans that any changes made to a copy of an object do reflect in the original object

#########################################################################
#deep
# L1 =[ 1,2,3,4]
# L2 = L1.copy()
# print(id(L1))
# print(id(L2))

# print(f"{L1} \n, {L2}")
# L1[0] = 8
# print(f"{L1} \n, {L2}")
# L2[0] = 99
# print(f"{L1} \n, {L2}")

#########################################################################
#shallow

# L1 =[ 1,2,3,4]
# L2 = L1
# #print(id(L1))
# #print(id(L2))
# print(f"{L1} \n, {L2}")
# L1[0] = 8
# print(f"{L1} \n, {L2}")
# L2[0] = 99                                ### changes in first will be reflected in 2nd
# print(f"{L1} \n, {L2}")                   ### changes in second will be reflected in 1st
#########################################################################
#cloning
L1 =[ 1,2,3,4]
L2 = L1[:]
# print(id(L1))
# print(id(L2))
print(f"{L1} \n, {L2}")
L1[0] = 8
print(f"{L1} \n, {L2}")
L2[0] = 99                              
print(f"{L1} \n, {L2}") 
#########################################################################
