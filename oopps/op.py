class a:
    pass
obj=a()
print(type(obj))
obj2=a()
print(id(obj))
print(id(obj2))


class student:
    def __init__(self,age):
        if age>=18:
            self.age=age
        else:
            # print("not eligible to vote")
            raise ValueError("Age must be less than or equal to 18")
mahesh=student(20)
print(mahesh.age)
mahi=student(10)
print(mahi)

class bankaccount:
    bank_name="ABC Bank"
    def __init__(self,ac_holder,ac_number,balance):
        if balance<0:
            self.balance=0
        else:
            self.balance=balance
        self.ac_holder=ac_holder
        self.ac_number=ac_number
ac_1=bankaccount("theerdha",13124132,-900)
ac_2=bankaccount("kiran",2343242331,1000)
print(ac_1.ac_holder)
print(ac_1.ac_number)
print(ac_1.bank_name)
print(ac_1.balance)
print(ac_2.ac_holder)
print(ac_2.ac_number)
print(ac_2.bank_name)
print(ac_2.balance)
def f(ac):
    print(ac.ac_holder)
    print(ac.ac_number)
    print(ac.bank_name)
    print(ac.balance)
f(ac_1)
f(ac_2)

class student:
    college="ABC college"
    def __init__(self,name,roll_no,marks):
        if 0<=marks<=100:
            self.marks=marks
        else:
            self.marks=0
        self.name=name
        self.roll_no=roll_no
s_1=student("theerdha",12,90)
s_2=student("lakshman",34,-10)
s_3=student("kiran",20,101)
def s(st):
    print(st.college)
    print(st.marks)
    print(st.name)
    print(st.roll_no)
s(s_1)
s(s_2)
s(s_3)

product=[]
class products:
    store_name="ABC store"
    def __init__(self,name,price,quantity):
        self.name=name
        if price>=0 and quantity>=0:
            self.price=price
            self.quantity=quantity
            product.append(self.name)
p1 = products("Laptop", 50000, 2)
p2 = products("Mobile", 20000, 5)
p3 = products("Headphones", 2000, 10)
def s(f):
    print(f.price)
    print(f.quantity)
    print(f.name)
    print(product)
s(p1)
s(p2)
s(p3)
