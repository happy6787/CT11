# # def decor (func):
# #     def inner():
# #         a=func()
# #         add=a+5
# #         return add
# #     return inner

# # def num():
# #     return 10

# # result_fun=decor(num)
# # print(result_fun())         

# ###############################################

# def decor (num):
#     def inner():
#         a=num()
#         add=a+5
#         return add
#     return inner
# @decor
# def num():
#     return 10

# print(num())

# ###############################################

# def decor1 (num):
#     def inner():
#         a=num()
#         multi=a*5
#         return multi
#     return inner

# def decor (num):
#     def inner():
#         b=num()
#         add=b+5
#         return add
#     return inner


# @decor
# @decor1
# def num():
#     return 10

# print(num())
