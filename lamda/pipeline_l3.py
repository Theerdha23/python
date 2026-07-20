
print(list(map(lambda x:x*3,list(filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9,10])))))

print(list(map(lambda x:x**2,list(filter(lambda x:x>20,[15,16,20,22,23,24,25,26,])))))

print(list(map(lambda x:x.upper(),list(filter(lambda x:len(x)>4,['hi','theerdha','you','rrrrr'])))))

print(list(map(lambda x:x+5,list(filter(lambda x:x%5==0,[1,2,3,4,5,6,7,8,9,10])))))

print(list(map(lambda x:x+5,list(filter(lambda x:x>40,[20,30,40,50,60,70,80,90])))))

from functools import reduce

print(reduce(lambda x,y:x+y,["theerdha","you","rrrrr"]))

print(reduce(lambda x,y:x*10+y,[1,2,3,4,5,6,7,8,9]))

print(reduce(lambda x,y:x-y,[9,8,7,6,5]))

print((reduce(lambda x,y:x+y,[1,2,3,4,5,6,7,8,9,10]))/len([1,2,3,4,5,6,7,8,9,10]))


print(list(map(lambda x:x-x*0.1,list(filter(lambda x:x>500,[400,800,9000,666,66,])))))