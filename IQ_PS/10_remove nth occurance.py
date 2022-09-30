#10_How to remove the Nth occurrence of a given word list? 

list = ['is', 'at', 'is', 'is','at']
element = 'is'
count = 3

def del_word(list,element,count):
    n = 0
    for i in range(0,len(list)):
        if list[i] == element:
            n = n+ 1
# Check for nth occurence and del if found
            if n == count:
                del(list[i])
                return list
               

print(del_word(list,element,count))

##################################################################################################

