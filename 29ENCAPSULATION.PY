
class Dad:
    def __init__(self) -> None: 
        self.__superpassword = "dad can have only access"     ### __ double underscore >>>  private attribute ###only same access   
        self._childpass = "if you are first in class"  ### _ single underscore >>> protected from outside world only accessed by child
                                                        ### only accessable to same class and child class    
        self.passwordforall = "public"                 ### public attribute
           ### private
        self.hobby = "imyown"           

    def hobby(self):
        print("newspaper")

    def getaccoountpassword(self):                  ### getter >>> will get private attribute outside class
        return self.__superpassword                 ### to make pvt attribute public we use getter

    #def setaccouontpassword(self,oldpass,newpassword):  ### setter >>> will set new password
      #  if (oldpass == self.__superpassword):
      #      self.__superpassword = newpassword
      #  else:
       #     print("enter valid old password")



    def bankaccount(self):
        accountpassword = input("Enter account no.")
        if (accountpassword == self._childpass):
            print("account is malamaal")
        else:
            print("wrong password")

        
class Mom:
    def __init__(self) -> None:
        print("Mom init")

    def hobby(self):
        print("cooking")

    def bankaccount(self):
        print("account is super malamaal")


class Beta(Mom, Dad):   #### method order resolution ### jo first likha wo class se lega (based on sequence)
    def __init__(self) -> None:
        print("Beta init")

    def hobby(self):    #### method overriding >>> requires inheritance, same method with different class
        print("party, insta, facebook")

    def toys(self):   #### method overloading   >>> same method same class
                        ### not supported in python
        print("cars")

    def toys(self):
        print("xbox")   ### will call latest one

objdad = Dad()
#print(objdad.__superpassword) ### unable to access __superpassword with dad class because it is outside class
                                ### __superpassword is only accessable within dad class as it is private 

# print(objdad.getaccoountpassword())
# objdad.__superpassword = "I will update password"
# print(objdad.getaccoountpassword())

obj = Beta()
obj.bankaccount()
obj._childpass = "my money only"


obj.hobby()


obj.toys()
# objDad = Dad()

# objMom = Mom()

# print(Dad._childpass)
