# def getdata(a,b):
#     print(a,b)

# getdata(10,20)    
# getdata(20,30)  


##IF USER WANT TO ADD ANOTHER VARIABLE "c"...HOW WILL HE MANIPULATE THE SAME IN ABOVE FUNCTION???

def getdata(a,b,c=0):
    print(a,b,c)

getdata(10,20)    
getdata(20,30)
getdata(10,20,30)
getdata(10,20,"")