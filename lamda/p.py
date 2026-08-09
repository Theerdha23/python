# #1
# def apply_func(a,b,op):
#     return op(a,b)
# add = lambda a,b:a+b
# sub = lambda a,b:a-b
# mul = lambda a,b:a*b
#
# print(apply_func(1,2,add))
# print(apply_func(2,1,sub))
from cachetools import keys

##2
# def sum_of(*args):
#     if len(args)==0:
#         return 0
#     return args[0]+sum_of(*args[1:])
#
# print(sum_of(1,2,3,4,5,6,7,8,9))

## 3
# def make_greeting(name,prefix="hello",format=lambda x:x):
#     return format(prefix+' '+name)
# print(make_greeting('theerdha','hi',str.upper))
#
# # #4
# print(list(map(lambda x: x**2, list(filter(lambda x:x%3==0,[1,2,3,4,5,6,7,8,9])))))

# #5
def func_apply(funcs,value):
    for func in funcs:
         value =func(value)
    return value

funcs=[lambda x:x*2,
        lambda x:x*3,
        lambda x:x*4]
#
print(func_apply(funcs,2))
# print(func_apply(triple,3))
# print(func_apply(quadruple,4))

#6
# def flat(lis,depth=1):
#     result = []
#     for elem in lis:
#
#         if type(elem)==list and depth>0:
#             return flat(elem,depth-1)
#         else:
#             result.append(elem)
#     return result
# print(flat([1,[2,[3]],4],depth=2))
# 7
# from functools import reduce
# def wegithed_averages(**args):
#     # c=0
#     # for k in args:
#     #     c+=1
#     e= reduce(lambda x,y: x+y, args.values())
#     return e/len(args)
#
# print(wegithed_averages(maths=200,scien=150,use=200))

#8

# print(sorted(list(map(lambda x :{**x ,'grade' :'pass'},filter(lambda x:x['score']>=60,[{'name':'Theerdha','score':69},{"name":"rr","score":71}]))),key= lambda x:x['score'],reverse=True))

# def cal(*args,operations='add',**options):
#     op = {'add':lambda a,b: a+b,
#           'mul':lambda a,b: a*b,
#           'min':lambda a,b: min(a,b),
#           'max':lambda a,b: max(a,b),}
#     f=op[operations]
#     res=args[0]
#     for a in args[1:]:
#         old_resul=res
#         res=f(res,a)
#         if options.get('show_steps'):
#             print(f" {old_resul} {a} {operations} =  {res}")


# cal(1,2,3,4,operations='add',show_steps=True)
# cal(1,2,3,operations='mul',show_steps=True)
# cal(1,2,3,operations='min',show_steps=True)
# cal(1,2,3,operations='max',show_steps=True)

# print(sorted(list(map(lambda x: {**x, 'grade': 'Pass'},filter(lambda x: x['score'] >= 60,[{'name': 'theerdha', 'score': 90},{'name': 'rahul', 'score': 69}]))),key=lambda x: -x['score']))








