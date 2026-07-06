def add(a,b):
    c = a + b
    return c
def sub(a,b):
    c = a - b
    return c
def mul (a,b):
    c = a*b
    return c
def div(a,b):
    c = a/b
    return c

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


  #single line calling

print(div(mul(add(a,b),sub(a,b)),10))


