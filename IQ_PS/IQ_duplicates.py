# astr="c5re8de1n9c7e"           ##str
# print(astr,type(astr))

# blist=[1,1,2,3,5,5,4,6,9,9,5,1,6,6,6]   #list
# print(blist,type(blist))

#1 find duplicate char and its count >>> c:2, e:3

# from collections import Counter

# word_length=Counter(blist)
# print(word_length,type(word_length))
# for d,c in word_length.items():
#     if c>1:
#        print(f"{d}:{c}")

############------------------------------------------------------------------------------------

#2 find count of digit in string >>> count:5

# astr='c5re8de1n9c7e' 
# count=0

# adigits=['0','1','2','3','4','5','6','7','8','9']

# for dig in astr:
#     if (dig in adigits):
#         count=count+1
# print(count)
######################################################################################

# count=0
# for dig in astr:
#     if dig.isdigit():
#         count=count+1
# print(count)

############------------------------------------------------------------------------------------

#3 find sum of digits from string >>> 30
# astr='c5re8de1n9c7e'

# sum=0
# for dig in astr:
#     if dig.isdigit():
#         sum=sum+int(dig)
# print(sum)


