# def dec(func):
#     def wrap(*args,**kwargs):
#         s=func(*args,**kwargs)
#
#         return s.upper()
#     return wrap
# @dec
# def get_message(message):
#     return message
# print(get_message("hello user"))
#
# def dec(func):
#     def wrap(*args,**kwargs):
#         s=func(*args,**kwargs)
#         return 2*s
#     return wrap
# @dec
# def get_number(number):
#     return number
# print(get_number(10))
#
# def dec(func):
#     def wrap(*args,**kwargs):
#         print('Authenticating user')
#         func(*args,**kwargs)
#         print('login successful')
#     return wrap
# @dec
# def login(username,password):
#     print(f'{username} and {password} is logged in')
# login('username','password')
#
# def dec(func):
#     def wrap(*args,**kwargs):
#         print("Sending messag")
#         func(*args,**kwargs)
#         print("message sent")
#     return wrap
# @dec
# def send_message(message):
#     print(message)
# send_message("hello")
#
# def dec(func):
#     def wrap(*args,**kwargs):
#         print("Calculating sum…")
#         func(*args,**kwargs)
#         print("Calculation done")
#     return wrap
# @dec
# def add(a,b):
#     print(a+b)
# add(3,4)
#
# def dec(func):
#     def wrap(*args,**kwargs):
#         print("Applying discount")
#         func(*args,**kwargs)
#         print("discount applied")
#     return wrap
# @dec
# def discount(x):
#     print(x)
# discount(10)
#
#
# import functools
# def dec1(func):
#     @functools.wraps(func)
#     def wrap1(*a,**kwargs):
#         print("hi")
#         func(*a,**kwargs)
#     return wrap1
# def dec2(func):
#     @functools.wraps(func)
#     def wrap2(*a,**kwargs):
#         func(*a,**kwargs)
#         print("bye")
#     return wrap2
# @dec2
# @dec1
# def say_hello(name):
#     print("hello", name)
# x=dec1(say_hello)
# z=dec2(x)
# z('mahesh')
# say_hello("Jon")
# print(say_hello.__name__)

# def m1():
#     print("hi")
# print(m1.__name__)
import functools
def dec1(func):
    @functools.wraps(func)
    def wrap1(*a,**kwargs):
        func(*a,**kwargs)
        print("hi")
    return wrap1
def dec2(func):
    @functools.wraps(func)
    def wrap2(*a,**kwargs):
        print("bye")
        func(*a,**kwargs)
    return wrap2
@dec2
@dec1
def say_hello(name):
    print("hello", name)
say_hello = dec1(say_hello)
say_hello = dec2(say_hello)
say_hello(123)

