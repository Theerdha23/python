# def simple_interest(p,r=5,time=1):
#     s_i=p*time*r/100
#     print(s_i)
#
# simple_interest(20000)
# simple_interest(20000,10,5)
# simple_interest(20000,10,5)

# def student_info(name,*sub,**details):
#     print(name)
#     print(f"subjects enrolled:",end="")
#     for s in sub:
#         print(f"{s} ",end="")
#     print()
#     for k,v in details.items():
#         print(f"{k}:{v}")
#
# student_info("theerdha","english","telugu","social",grade=10,school='narayana')

# def order_food(*items,**preferrences):
#     for item in items:
#         print(item)
#     for k,v in preferrences.items():
#         print(k,v)
#
# order_food("idly",'dosa',spice_level='hot',delivery_time="before 7p.m")

# def shopinf_cart(dis=0,*prices):
#     total=0
#     for price in prices:
#         total+=price
#     total=total-dis
#     print('total price:', total)
#
# def shopinf_cart1(*prices,dis=0):
#     total = 0
#     for price in prices:
#         total += price
#     total = total - dis
#
#     print('total price:',total)

# shopinf_cart(100,2000,200,30)
# shopinf_cart1(100,2000,200,30,dis=0)

# def register_user(username, role="user",*permissions,**details):
#     print(username)
#     print(role)
#     for permission in permissions:
#         print(permission)
#     for k,v in details.items():
#         print(k,v)
# register_user("ther","user",'location','media',active_user='yes')
# import copy
# original_list=[
#     {'age':21,'DOB':1999},
#     {'age':30,'DOB':1899},
# ]
# s_copy=copy.copy(original_list)
# s_copy[0]['age']=22
# print(s_copy)
# d_copy=copy.deepcopy(original_list)
# d_copy[0]['age']=23
# print(d_copy)

# def login(username,password='12344'):
#     print(username)
#     print(password)
#
# login('username','password')

# def func(length,breadth=None):
#     if breadth is None:
#         breadth = length
#     print(breadth*length)
# func(20)

# def caluclate_score(base_score=0,*bonus,**penalties):
#     final_score = 0
#     final_score += base_score
#     for bonu in bonus:
#         final_score += bonu
#     for value in penalties.values():
#         final_score -= value
#     print(final_score)
#
# caluclate_score(2,200,300,ext=22,wides=233)