
### without using regex function
str1=input('enter your string to seperate numbers, alphabets and special characters: ')
n=0
s=0
a=0
numberslist=[]
alphabetslist=[]
speciallist=[]
numbers= '1234567890'
alphabets='abcdefghijklmnopqrstuvwxyz'
for i in range(len(str1)):
    if str1[i] in numbers:
        n+=1
        numberslist.append(str1[i])
        continue
    if str1[i] in alphabets:
        a+=1
        alphabetslist.append(str1[i])
        continue
    else:
        s+=1
        speciallist.append(str1[i])
print('count of elements present in your string are : ',len(str1))
print(f'There are {n} numbers  in your string, those numbers are {numberslist}')
print(f'There are {a} alphabets  in your string, those alphabets are {alphabetslist} ')
print(f'There are {s} special characters in your string, those special characters are {speciallist}')
