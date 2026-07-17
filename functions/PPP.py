# count = len
# list = [1,2,2,2,2]
# print(count(list))
#
#
# string_methods={
#     'upper' : str.upper,
#     'lower' : str.lower,
#     'len':len,
# }
#
# a= input("Enter a choice upper or lower: ")
# b= input("Enter your string: ")
# print(string_methods[a](b))
#
# def func(n):
#     def mul(x):
#         print(x*n)
#     return mul
#
# print(func(3)(12))

# def add(a,b):
#     return a+b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     return a/b
#
# v = sum
# l = [add(2,2),multiply(2,2),divide(2,2)]
# print(v(l))

# def min():
#     return 1
# def max():
#     return 2
# def sum():
#     return 3
#
# dic = {'min':min,'max':max,'sum':sum}
# z = input("enter choice:")
# print(dic[z]())

def repeat(func,n,value):
    for i in range(n):
        func(value)