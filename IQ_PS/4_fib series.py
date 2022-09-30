#4_Print Fibonacci series.

# till n
# n = int(input("enter number "))
# x=0
# y=1
# z=0
# while z<=n:
#     print(z)
#     x=y
#     y=z
#     z=x+y

######################################################################################################################


# first 10 fib numbers

n = int(input("enter number "))
x=0
y=1
print(x)
print(y)
for i in range(2,n):
    z=x+y
    x=y
    y=z
    print(z)

######################################################################################################################
