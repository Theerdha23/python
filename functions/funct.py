def  say_hello():
    print("welcome to my python")
say_hello()
print(say_hello())

def add(a,b):
    return a+b

a = int(input("enter first number"))
b = int(input("enter second number"))
print(add(a,b))

def area(a,b):
    return a*b
a=int(input("enter first number"))
b=int(input("enter second number"))
print(area(a,b))

def mult(a,b,c):
    return a*b*c
a = int (input())
b = int (input())
c = int (input())

print(mult(a,b,c))


def describe_pet(animal_type, pet_name):
    return f"my {animal_type} is named {pet_name}"

print(describe_pet("dog","bhaai"))

def power(b,e):
    return b**e
a = int(input())
b = int(input())
print(power(a,b))

def full_name(first,middle,last):
    return f"{first} {middle} {last}"

print(full_name("yerra","theerdha","reddy"))

