from os import remove
from tkinter import E


class Employee:  # parent class
    Name = "unknown"
    Address = "unknown"

    def getempdetails(self):
        print("Name : ", self.Name, "Address :",self.Address)



### Single Inheritance >>> one parent one child

class TempEmployee(Employee):  ###Child Class >>> mention class name which we want to inherit to class
    stipend = "unknown"

    def getstipend(self):
        print(self.stipend)



tempobj = TempEmployee()   ### this method has been inherited from Partent class (Employee) as we have added parent access
tempobj.getempdetails()                                         ###  to child in class TempEmployee(Employee)
tempobj.getstipend()

empobj = Employee()   ###   we habe only one method in parent i.e getempdetails
empobj.getempdetails()

###############################################################################################################

#Multi level Inheritance >>> one parent >>> child >>> child

class BenchEmployee(TempEmployee):  #child of tempemployee
    stipend = "unknown"

    def getstipend(self):
        print(self.stipend)


benobj = TempEmployee()   ### this method has been inherited from Partent class (Employee) as we have added parent access
benobj.getempdetails()                                         ###  to child in class TempEmployee(Employee)
benobj.getstipend()



empobj = Employee()   ###   we habe only one method in parent i.e getempdetails
empobj.getempdetails()


###############################################################################################################

### Hierachical Inheritance >>> one parent two or more child

class PermEmployee(Employee):    ###Child Class
    salary = "unknown"
    perq = "unknown"

    def getsalary(self):
        print(self.salary)
       
    def getperq(self):
        print(self.perq)

permobj = PermEmployee()   ### this method has been inherited from Partent class (Employee) as we have added parent access
permobj.getempdetails()                                         ###  to child in class TempEmployee(Employee)
permobj.getsalary()

empobj = Employee()   ###   we habe only one method in parent i.e getempdetails
empobj.getempdetails()

###############################################################################################################
    
##Multiple Inheritance >>> Father & Mother >>> child


class RemoteEmployee(PermEmployee):    ###Child Class
    salary = "unknown"

    def getsalary(self):
        print(self.salary)


remobj = RemoteEmployee()   ### this method has been inherited from Partent class (Employee) as we have added parent access
remobj.getempdetails()                                         ###  to child in class TempEmployee(Employee)
remobj.getsalary()
remobj.getperq()     #### perq from premnant employee

empobj = Employee()   ###   we habe only one method in parent i.e getempdetails
empobj.getempdetails()
