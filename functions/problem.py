# print('-----------billing detials---------')
# def calculate_bill(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     print(f'total charges are: {total}')
#     return total
# def apply_discount(total):
#     sum = 0
#     if total > 1500:
#         sum = total*0.10
#         print('total discount is: ',sum)
#         total = total-sum
#     else:
#         total = total-sum
#     return total
# def final_bill(total,*details):
#     p_c = 100
#     for detail in details:
#         print('taxes are : ',detail)
#         total += detail
#     print(f'service charges are: {p_c}')
#     total = total+p_c
#     print(f'total payable bill is: {total}')
#
# final_bill(apply_discount(calculate_bill(500,1000,1500)),300,500,600)


# print('-----------billing detials---------')
# def calculate_bill(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     print(f'total charges are: {total}')
#     return total
# def apply_discount(total):
#     sum = 0
#     if total > 1500:
#         sum = total*0.10
#         print('total discount is: ',sum)
#         total = total-sum
#     else:
#         total = total-sum
#         print('*discount is not apllicable on this order*')
#     return total
# def final_bill(total,**details):
#     p_c = 100
#     for k,detail in details.items():
#         print(k,':',detail)
#         total += detail
#     print(f'service charges are: {p_c}')
#     total = total+p_c
#     print(f'total payable bill is: {total}')
#
# final_bill(apply_discount(calculate_bill(50,100,150)),gst=300,sgst=500,others=600)



print('-----------billing detials---------')
def billing_detials(cus_name,order_type='regular',*items,**addtional_details):
    print(f' cus_name: {cus_name}')
    print(f' order_type: {order_type}')
    i=1
    for item in items:
        print(f'{i}.item: {item}')
        i+=1
    for k,v in addtional_details.items():
        print(f'{i}.{k}: {v}')
        i+=1

billing_detials('theerdha','premium','dosa','idly','upma','hot coffe',address='near kphb,roadno:2',
                payment_status='paid through UPI',delivery_instructions='deliver the items on time',discount='10%')



