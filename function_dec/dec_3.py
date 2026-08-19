def log_operation(func):
    def wrap(*args,**kwargs):
        print("opertions started")
        re=func(*args,**kwargs)
        print("operation finished")
        return re
    return wrap



def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
square=lambda a,b: a**2
cube=lambda a,b: a**3
double=lambda a,b: a*2


@log_operation
def calculate(operation,a,b):
    return operation(a,b)
print(calculate(add,2,3))
print(calculate(mul,2,3))
print(calculate(square,2,3))



def dec(func):
    def wrap(*args,**kwargs):
        print("Processing started")
        print("Processing ended")
        return func(*args,**kwargs)
    return wrap
add_5marks=lambda a:a+5
double=lambda a:a*2
greater_than_40=lambda a:a>40
@dec
def process_marks(marks,operation):
    return operation(marks)
print(process_marks(55,greater_than_40))
print(process_marks(5,double))

def dec(func):
    def wrapper(*args, **kwargs):
        print("Notification started")
        print("Notification sent")
        return func(*args, **kwargs)
    return wrapper
upper=lambda x:x.upper()
lower=lambda x:x.lower()
add=lambda x:x+"!!!"
@dec
def send_notification(message,formatter):
    return formatter(message)

print(send_notification("hi how are you?",upper))
print(send_notification("hi how are you?",lower))
print(send_notification("hi ",add))

def order_logger(func):
    def wrapper(*args, **kwargs):
        print("oder is processing")
        return func(*args, **kwargs)
    return wrapper
def payment_check(func):
    def wrapper(*args, **kwargs):
        s=func(*args, **kwargs)
        print("Payment verification completed")
        return s
    return wrapper

discount_10=lambda a:round(a*1.1,2)
discount_20=lambda a:round(a*1.2,2)
discount_100=lambda a:a-100
@payment_check
@order_logger
def function_process_order(price,discount_function):
    return discount_function(price)

print(function_process_order(100,discount_10))
print(function_process_order(100,discount_20))


# n=int(input())
# if n<=0:
#     print("Invalid Input")
# else:
#     for i in range(1,n+1):
#         for j in range(1,i):
#             if j+1>10:
#                 print("   ",end="")
#             else:
#                 print(" ",end=" ")
#         for j in range(i,n+1):
#             print(j,end=" ")
#         print()


# elif user_name != user:
# if uns <= 3:
#     login(input("enter username again"), passw)
#     uns += 1
# else:
#     print("no ")
#     return
# else:
# if uns <= 3:
#     login(user, input("enter password again"))
#     uns += 1
# na = uns + sa