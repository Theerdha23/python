


class zomato:
    res_no=0
    coupon_code="ABC"
    discount=50
    res_names=[]
    def __init__(self,r_name,r_menu):
        self.r_name=r_name
        self.r_menu=r_menu
        zomato.res_names.append(r_name)
        zomato.res_no+=1
        self.r_id=zomato.res_no
paradise=zomato('paradise',{'chips':100,'coke':140})
briyani=zomato('briyani',{'briyani': 150,'fry briyani':200})
fast_foods=zomato("fast_foods",{"chicken fried rice":100,"gobi fried rice":200})
# print(zomato.res_names)
def take_order(res,item_no):
    item=list(res.r_menu.items())
    print(item[item_no-1][1])
    pr=item[item_no-1][1]
    print(f"your cart is {pr}")
    code=input("do you have coupn code? YES or NO")
    if code=="YES":
        cp=input("enter coupon code")
        if cp==zomato.coupon_code:
            p=p-zomato.discount
            print(f"total price is {pr}")
    else:
        print(pr)

c=0
for r in zomato.res_names:
    c+=1
    print(c, r)

ch=int(input("enter your resturant:"))
if ch==1:
    c=0
    for i in paradise.r_menu:
        c+=1
        print(c,i, paradise.r_menu[i])
    od=int(input("enter your item no:"))
    take_order(paradise,od)
elif ch==2:
    c=0
    for i in briyani.r_menu:
        c+=1
        print(c,i, briyani.r_menu[i])
    od = int(input("enter your item no:"))
    take_order(briyani,od)
elif ch==3:
    c=0
    for i in fast_foods.r_menu:
        c+=1
        print(c,i, fast_foods.r_menu[i])
    od = int(input("enter your item no:"))
    take_order(fast_foods,od)
else:
    print("invalid choice")


























#
# def order(obj,item_na,coupon_code=""):
#     o=obj.r_menu[item_na]
#
#     if coupon_code==zomato.coupon_code:
#         o=o-zomato.discount
#         return o
#     else:
#         return o
# def dis():
#     for z in zomato.res_names:
#         print(z.r_name,end=":")
#         print()
#         for j,k in z.r_menu.items():
#             print(j,k)
#         print()
# dis()
#
# print(order(fast_foods,'chicken fried rice',"ABC"))




