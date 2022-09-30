#20. How to check string is palindrome or not?

### use this when input is word

# a=('radar')       #will not work with set, dictionary data type ###### will also work with tuple
# print(type(a))
# b=(a[::-1])
# print(b)
# if a == b:
#     print("Input is Palindrome case", b)
# else:
#     print("normal case", b)    

###################################################################################################

# use this when input is either word or sentence 

# input_anything=input("enter string ")
# split_anything=(input_anything.split())
# split_anything.reverse()
# p_case=(' '.join(split_anything))      ###(' ') >>> is separator
# if input_anything == p_case:
#     print("Input is Palindrome case")
# elif input_anything != p_case:
#     print("normal case")    

###################################################################################################

# input_anything=input("enter string ")
# split_anything=(input_anything.split())
# split_anything.reverse()
# p_case=(' '.join(split_anything)) 
# while input_anything == p_case:
#     print("Input is Palindrome case")
#     break
# else:
#     print("normal case")

###################################################################################################
