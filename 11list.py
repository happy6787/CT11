# a=10                         #int
# a=10,20                      #tuple
# print(type(a))

###----------------------------------------------------------------------------------------------------------------------------

# #####List

# a=[10,20,30]          #List
# print(type(a))

# a=[10.2,20,30]      #List
# print(type(a))

###----------------------------------------------------------------------------------------------------------------------------

#a=[10,12,15,8,9,20,23]
#print(len(a))      
#print(len(a)-1)  
#print(a[0:4])            ##10,12,15,8 
#print(a[6])               ##23
#print(a[2:4])           ## 15,8 
#print(a[-5:3])           ## 15   
#print(a[:4])           ## 10, 12, 15, 8
#print(a[4:])             ##9,20,23
#print(a[:])             ## pura aayega
#print(a[::2])           ## 10,15,9,23
#print(a[::3])            ## 10, 9 ,23
#print(a[::4])              ##10 9
#print(a[0:-3])          ##10 12 15 8
#print(a[0:-3:2])          ##10 15
#print(a[-1:-8:-2])        ## 23 9 15 10
#print(a[::1])           ### pura aayega
#print(a[::-1])        ### ulta pura aayega
#print(a[::3])           ##10 8 23
#print(a[:5:1])        ##10 12 15 8 9
#print(a[3:3])          ##empty   
#print(a[:-4:-1])      ##23 20 9
#print(a[-4:-8:-1])     ### 8 15 12 10

###----------------------------------------------------------------------------------------------------------------------------

# a=[10,12,15,"hello",[10, 8, 7], 8.7,9,"True",23,""]
# print(a[4][1])       ###inner portion we will get by using indexing
# print(a[4][::-1])    ###[7,8,10]
# print(a[::-1])       ### pura ulta aayega

###----------------------------------------------------------------------------------------------------------------------------

c=[10,20,"happy",10.25,1,0,0,10, True, False] 
#print(c.count(10))
 # 0  1    2     3 4 5 6 7     8    9   10     
c=[10,20,"happy",10,1,0,0,10, True, 10, False] 
print(c.index(10))   #### first occurance
# print(c.index(10,c.index(10)+1))   ### second occurance 
# print(c.index(10,c.index(10)+4))   ### third occurance  >>> when list is known
# print(c.index(10,c.index(10)+8))   ### fourth occurance 
print(c.append())
# print(c.index(10))
# print(c.index(10,c.index(10)+1))
# print(c.index(10,c.index(10,c.index(10)+1)+1))      ### when list is unknown
# print(c.index(10,c.index(10,c.index(10,c.index(10)+1)+1)+1))  







 