class employee:
    company="techcorp"
    em_count=0
    def __init__(self,name,department,salary,experience):
        if salary<=0:
            self.salary=0
        else:
            self.salary=salary
        if experience<=0:
            self.experience=0
        else:
            self.experience=experience
        self.name=name
        self.department=department
        if experience>5:
            salary=salary*1.15
        elif 3<experience<5:
            salary=salary*1.10
        elif experience<=3:
            salary=salary*1.05
        self.pay_details={
            'nane':name,
            'department':department,
            'salary':int(salary),
            'experience':experience
        }
        employee.em_count+=1
e1=employee("theerdha","ece",15000,6)
e2=employee("k","cse",15000,3)
# print(e1.em_count)
# print(e2.em_count)
# print(e1.__dict__)
# print(e2.__dict__)
print(e1.pay_details)
e1.pay_details['nane']="ttt"
print(e1.__dict__)
print(e1.pay_details['nane'])

class mobliepurcahse:
    store_name="Smart Moblies"
    pur_count=0
    def __init__(self,customer,brand,price,storage,qunatity):
        if price<0:
            self.price=0
        if qunatity<0:
            self.qunatity=0
        if storage in [64,128,256,512]:
            self.storage=storage
        self.customer=customer
        self.price=price
        self.brand=brand
        self.qunatity=qunatity
        if price>50000:
            price=price*1.10
        else:
            price=price*1.05


        self.pur_details={
            'customer':customer,
            'brand':brand,
            'price':int(price),
            'storage':storage,
            "qunatity":qunatity,
            'total price':price*qunatity
        }
        mobliepurcahse.pur_count+=1
c1=mobliepurcahse("therdha","iphone",52000,512,1)
c2=mobliepurcahse("k","cse",50000,64,1)
print(c1.__dict__)
print(c2.__dict__)
print(c1.pur_count)

class product:
    store="shopeasy"
    def __init__(self,name,price,qunatity):
        self.name=name
        self.price=price
        self.qunatity=qunatity
        self.store_details={
            'name':name,
            'price':price,
            'qunatity':qunatity,
            'total price':price*qunatity
        }
p1=product("pen",200,1)
p2=product("fan",400,2)
print(p1.__dict__)
p1.price=500
print(p1.__dict__)
p1.store_details['price']=600
print(p1.__dict__)
print(p2.__dict__)
