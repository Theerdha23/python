# def dec(func):
#     def wrap(*args, **kwargs):   # accept any arguments
#         print('Function started')
#         func(*args, **kwargs)    # forward them to the original function
#         print("Function ended")
#     return wrap
#
#
# def place_order(item):
#     print(f"order placed {item}")
#
# place_order = dec(place_order)
# # place_order('toy')
# def dec(func):
#     def wrap(*args,**kwargs):
#         print("welcome")
#         func(*args,**kwargs)
#         print("goodbye")
#     return wrap
# @dec
# def show_message(message):
#     print(message)
# # show_message=dec(show_message)
# show_message("to the house")

def dec(func):
    def wrap(*args,**kwargs):
        print("payment initiated")
        func(*args,**kwargs)
        print('payment completed')
    return wrap
def make_payment(amount):
    print(f"payment is {amount}")
make_payment=dec(make_payment)
make_payment(100)


