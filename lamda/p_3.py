# print(list(map(lambda x:(x*9/5)+32,[33,44,55,55,55,])))
#
# print(list(filter(lambda x:x[0]==x.upper()[0],['Theerdha','the','work','eat'])))
#
from functools import reduce
# print(reduce(lambda x,y:x*y,[1,2,3,4,5]))

# print(list(sorted([('theerdha',22),('rahul',23)],key=lambda x:-x[1])))#x is the index of the list

# print(list(map(lambda x:x**2,filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,10]))))

# def my_func_map(fun,l):
#         return fun(l)
#
# def square(i):
#     result = []
#     for item in i:
#         result.append(item**2)
#     return result
#
# print(my_func_map(square,[1,2,3]))

print(reduce(lambda x,y: x if len(x)>len(y) else y, ['cat', 'elephant', 'dog', 'rhinoceros']))





