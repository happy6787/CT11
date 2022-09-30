# #======= Function approach # without class
# id = 101            ## variable
# name = "Abhinav"    ## variable
# address = "Banglore"    ## variable
# salary = "60000000"   ## variable


#       #(function)
# def getempdetails()-> int: ##we can give command to print output as int /str etc (-> int) but python will give output based on program only 
#     print(f"Id = {id}, name : {name}, address : {address}, salary :{salary}")  

# temp=getempdetails()    #(function call)
# print(temp,type(temp))


######----------========================================================================

## Apporach with class
class Employee:  ### Class : keyword... Employee : name of class and first letter should be capital
    id = 202                ## Attribute
    name = "Abhinav"        ## Attribute
    address = "Banglore"    ## Attribute
    salary = "60000000"     ## Attribute

    def getempdetails(self):       ###Object Method 
        print(f"Id = {self.id}, name : {self.name}, address : {self.address}, salary :{self.salary}, Mobile :{self.Mobile}")    ##object attribute
        #print(f"Id = {Employee.id}, name : {Employee.name}, address : {Employee.address}, salary :{Employee.salary}")  #class attribute
                #self nahi dete to class k andar k attributes ko capture nahi karat
                # self is as good as object/parameter of class Employee
                # only after creating objecct/instatiation, memory will be allocated to attributes

    #def getcodetails():      ###class Method    ### self nahi diya kuki we are not usig attributes from class isliye print hogaya
       # print("Co name is Pathway")
#Employee.getcodetails()           ### we get output coz we have not used self init

   # def getempbonus(self,percent):
      #  bonus = int(self.salary) * percent   
      #  print("bonus is ", bonus)

####################################################


#getempdetails()                  ### we can not call class method directly outside without class name or object

#########

## To call method which is inside class, we have 2 approach 
## approach 1: Call mehtod with class name

#Employee.getempdetails()          ###object is required else we get type error

# Employee.getcodetails()                       ### we get output coz we have not used self in it

#emp=Employee()                        ###objject creation or instatiation
# Employee.getempdetails(emp)           ### instead of emp we can also use self as object name

# #########

# ##approach 2 : call method with emp 
# emp.getempdetails()

#emp.getempbonus(0.10)
#Employee.getempbonus(emp,0.10)

#################################################################################################################################


# a = "happy"
# print(a.find('p'))          ## 2nd approach
# print(str.find(a, 'p'))    ## 1st approch

#################################################################################################################################

### MODIFICATION IN ATTRIBUTES AT OBJECT LEVEL

emp1=Employee()    
emp1.Mobile=7758856787
emp1.getempdetails()


emp2=Employee()   ### new object will get new memory location with all attributes
emp2.name="Umesh"   ###we can change/modify/alter attributes based on new and individual object created
emp2.address="Dubai"   ###changes in attributes or output will only be limited to particular/modified object and not all objects.
emp2.salary=70000000

emp3=Employee()

# emp1.getempdetails()
# emp2.getempdetails()
# emp3.getempdetails()

##########################################################

### MODIFICATION IN ATTRIBUTES AT CLASS LEVEL

Employee.salary = 80000000
Employee.address = "Germany"

emp1.getempdetails()
emp2.getempdetails()
emp3.getempdetails()

### If there are changes in both object and class level as seen above; 
### priority will be given to object level changes and then class level
### CHANGES AT OBJECT LEVEL WILL NOT CAPTURE CLASSGLOBALL LEVEL CHANGES WITHIN IT

#################################################################################################################################

### IT IS NOT NECESSARY THAT ALL GOLBAL/CLASS LEVEL ATRRIBUTES WILL BE PRESENT AT OBEJCT LEVEL
### DURING RUN TIME ALSO WE CAN ADD ATTRIBUTES TO THE PARTICULAR OBJECTS

#emp1.Mobile=7758856787 ###will not be accessable as we have not given mobile attribute in method (line no 26/27)
                        #post this we have to add attribute at object level (line no 77) and then print  
