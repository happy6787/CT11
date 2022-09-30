# class Addition:
    
#     def __init__(self, first, second ) -> None:
#         self.firstNum = int(input(first))
#         self.secondNum = int(input(second))

#     def getResult(self)-> int:
#         return self.firstNum + self.secondNum
        
# addObj = Addition('firstNum ', 'secondNum ') 


# result = addObj.getResult()
# print("Addition is ", result) 

############################################################################################################

# print('''please Select the Operation you  want to Perfom
#       1 = Add
#       2 = Subtract
#       3 = Multiply
#       4 = Divide''')
      
# opt = int(input("Choose Operation from 1, 2, 3, 4 = "))

# n1 = int(input("First Number        = "))
# n2 = int(input("Second Number = "))

# if opt == 1:
#     print(n1, ' + ', n2, '  =  ', n1 +  n2)
# elif opt == 2:
#     print(n1, ' - ', n2, '  =  ', n1 -  n2)
# elif opt == 3:
#     print(n1, ' * ', n2, '  =  ', n1 *  n2)
# elif opt == 4:
#     print(n1, ' / ', n2, '  =  ', n1 /  n2)
# else:
#     print('Invalid Input')

############################################################################################################

# def addition(x, y):
#     return x + y

# def subtraction(x,  y):
#     return x - y

# def multiplication(x,  y):
#     return x * y

# def division(x,  y):
#     return x / y

# opt = int(input("Choose Operation from 1(Add), 2(Sub), 3(Multi), 4(Div) = "))

# n1 = int(input("First Number        = "))
# n2 = int(input("Second Number = "))

# if opt == 1:
#     print(n1, ' + ', n2, '  =  ', addition(n1, n2))
# elif opt == 2:
#     print(n1, ' - ', n2, '  =  ', subtraction(n1, n2))
# elif opt == 3:
#     print(n1, ' * ', n2, '  =  ', multiplication(n1, n2))
# elif opt == 4:
#     print(n1, ' / ', n2, '  =  ', division(n1, n2))
# else:
#     print('Invalid Input')

############################################################################################################

# num_1 = int(input('Enter your first number: '))
# num_2 = int(input('Enter your second number: '))
 
# # Addition
# #print(f'{num_1} + {num_2}')
# print("Addition will be = " ,num_1 + num_2)
 
# # Subtraction
# #print(f'{num_1} - {num_2}')
# print("Subtraction will be = " ,num_1 - num_2)
 
# # Multiplication
# #print(f'{num_1} * {num_2}')
# print("Multiplication will be = " , num_1 * num_2)
 
# # Division
# #print(f'{num_1} / {num_2}')
# print("Division will be = " ,num_1 / num_2)

############################################################################################################

# choice = input('''
# Please select the type of operation you want to perform:
# + for addition
# - for subtraction
# * for multiplication
# / for division
# ''')
 
# num_1 = int(input('Enter your first number: '))
# num_2 = int(input('Enter your second number: '))
 
# if choice == '+':
#     print(f'{num_1} + {num_2}')
#     print(num_1 + num_2)
 
# elif choice == '-':
#     print(f'{num_1} - {num_2}')
#     print(num_1 - num_2)
 
# elif choice == '*':
#     print(f'{num_1} * {num_2}')
#     print(num_1 * num_2)
 
# elif choice == '/':
#     print(f'{num_1} / {num_2}')
#     print(num_1 / num_2)
 
# else:
#     print('Enter a valid operator, please run the program again.')

#################################################################################################################

# def calculate():
#     operation = input('''
# Please type in the math operation you would like to complete:
# + for addition
# - for subtraction
# * for multiplication
# / for division
# ''')

#     num_1 = int(input('Please enter the first number: '))

#     num_2 = int(input('Please enter the second number: '))

#     if operation == '+':
#         print(f'{num_1} + {num_2}')
#         print(num_1 + num_2)

#     elif operation == '-':
#         print(f'{num_1} - {num_2}')
#         print(num_1 - num_2)

#     elif operation == '*':
#         print(f'{num_1} * {num_2}')
#         print(num_1 * num_2)

#     elif operation == '/':
#         print(f'{num_1} / {num_2}')
#         print(num_1 / num_2)

#     else:
#         print('You have not typed a valid operator, please run the program again.')
#     again()
# def again():

#     # Take input from user
#     calc_again = input('''
# Do you want to calculate again?
# Please type Y for YES or N for NO.
# ''')

#     # If user types Y, run the calculate() function
#     if calc_again == 'Y':
#         calculate()

#     # If user types N, say good-bye to the user and end the program
#     elif calc_again == 'N':
#         print('See you later.')

#     # If user types another key, run the function again
#     else:
#         again()

# # Call calculate() outside of the function
# calculate()

###############################################################################################################

