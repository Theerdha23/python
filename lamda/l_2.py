l =[100,200,300,400,500,600,700,800,900]
updated_prices= list(map(lambda x: x+x*0.1,l))
print(updated_prices)

list_of_user=["theerdha","rahul","you"]
uppercase_list=list(map(lambda x:x[0].upper()+x[1:],list_of_user))
print(uppercase_list)

pr=[100,2000,500,6000,699]
dis= list(filter(lambda x:x>=500,pr))
print(dis)

lis=[1,2,3,4,5,6,7,8,9,10]
mul_5 = list(map(lambda x:x*5,lis))
print(mul_5)

list_of_user=["theerdha","rahul","you"]
calculate_length=list(map(lambda x : len(x),list_of_user))
print(calculate_length)

lis=[10,20,30,40,50,60,70,80,90]
greater_than_50=list(filter(lambda x:x>50,lis))
print(greater_than_50)

lis=[10,20,30,40,50,60,70,80,90,16]
m_4 = list(filter(lambda x:x%4==0,lis))
print(m_4)
m_4.sort(key=lambda x:x)
print(m_4)
