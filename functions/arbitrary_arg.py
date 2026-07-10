# #postional args
# def  add(*args):
#     print(args)
#     sum = 0
#     for arg in args:
#         sum += arg
#
#     print(sum)
#
# add(1,2,3)
# add(20,11)
#
# #keyword args
# def order_details(**kwargs):
#     print(kwargs)
# order_details(age=12,name='guest')
#
#

# def register_details(**kwargs):
#
#     print(("-------register details-------"))
#     for k,v in kwargs.items():
#         print(f'{k} : {v}')
#
# register_details(paitent_name='rahul',age=22, symptoms={'ttt'},doctor_assigned='vijay')
# register_details(paitent_name=input('enter your name:'),age=int(input('enter your age:')), symptoms=input('enter your symptoms:'),doctor_assigned='vijay')


# def print_arg(a,b='theer',*args,**kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)
#
# print_arg('w','ree','rerer','rahul',key='rr',you='love')
#
# def mul_all(*args):
#     mul = 1
#     for arg in args:
#         mul *= arg
#     print(mul)
#
# mul_all(1,2,3,4,5)

# def dispaly_tags(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# dispaly_tags(name="name", value="value",age="age")

'''crate a py application to develop a hospital billing system crate fun like calculate bill with arbitarty postional
arg called charges crate another function apply insurance with arbitary keyword args and another add taxes with
arbitarty key args the program should accept multiple charges apply insurance reduction then add taxes'''
print('----------------bill details-----------------')
def calculate_bill(*charges):
    total = 0
    for charge in charges:
        print(charge)
        total += charge
    print(f'total charges : {total}')
    return total
def apply_insurance(total,**insurance):
    insurance_a = 0
    for key, value in insurance.items():
        print(key,'         : ', value)
        insurance_a += value
    print(f'total insurance : {insurance_a}')
    total=total-insurance_a
    return total

def apply_taxes(total,**taxes):
    tax_a = 0
    for key, value in taxes.items():
        print(key,':', value)
        tax_a += value
    print(f'total taxes: {tax_a}')
    total=total+tax_a
    print(f'total bill is: {total}')

# calculate_bill(float(input("enter charges 1: ")),float(input("enter charges2: ")),float(input("enter charges3: ")))
# apply_insurance(calculate_bill(float(input("enter charges 1: ")),float(input("enter charges2: ")),float(input("enter charges3: "))),lic="2000",sbi='2000')
apply_taxes(apply_insurance(calculate_bill(float(input("enter charges 1: ")),float(input("enter charges2: ")),float(input("enter charges3: "))),lic=2000,sbi=2000),gst=200,others=200)





