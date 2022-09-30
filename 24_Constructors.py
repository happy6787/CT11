
### __INIT__()(INITIALIZE) A SSPECIAL METHOD WHICH RUNS AS SOON AS OBJECT IS CREATED
### IT TAKES SELF ARGUMENT AND CAN ALSO TAKE FURTHER ARGUMENTS.
### The task of constructors is to initialize(assign values) to the data members(attributes) 
            # of the class when an object of the class is being created. 
### Types of constructors: 
#	default constructor
#	parameterized constructor
### Returns None 
### (use constructor to assign or make changes to class)
###############################################################################################################

# class Employee:  ### Class : keyword... Employee : name of class and first letter should be capital
  

#     def __init__(self):       ### returns none
#         self.id = 202                ## Attribute
#         self.name = "Abhinav"        ## Attribute
#         self.address = "Banglore"    ## Attribute
#         self.salary = "60000000"     ## Attribute
#         self.Mobile = 7758856787
#         print("Object Created......")

#     def getempdetails(self):       ###Object Method 
#         print(f"Id = {self.id}, name : {self.name}, address : {self.address}, salary :{self.salary}")    ##object attribute
#         #print(f"Id = {Employee.id}, name : {Employee.name}, address : {Employee.address}, salary :{Employee.salary}")  #class attribute
#                 #self nahi dete to class k andar k attributes ko capture nahi karat
#                 # self is as good as object/parameter of class Employee
#                 # only after creating objecct/instatiation, memory will be allocated to attributes

# emp=Employee()  ### constructor (__init__(self)) will be called automatically
# #emp1=Employee.__init__(emp)    #### if we use this statement to call constructor; it will be same as class and object wala:
#                                     #so need to use this statement

###############################################################################################################
###############################################################################################################

# class Addition:
#     firstNum = 0
#     secondNum = 0

#     def __init__(self) -> None:
#         pass

#     def getResult(self)-> int:
#         return self.firstNum + self.secondNum

# addObj = Addition()
# result = addObj.getResult()
# print("Addition is ", result)

# addObj = Addition()
# addObj.firstNum = 10
# addObj.secondNum = 20

# result = addObj.getResult()
# print("Addition is ", result) 

###############################################################################################################
###############################################################################################################

class Addition:
    
    def __init__(self, first, second ) -> None:
        self.firstNum = int(input(first))
        self.secondNum = int(input(second))

    def getResult(self)-> int:
        return self.firstNum + self.secondNum
        
addObj = Addition('firstNum ', 'secondNum ') 


result = addObj.getResult()
print("Addition is ", result) 