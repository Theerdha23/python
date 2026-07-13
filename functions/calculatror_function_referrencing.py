def  add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

# a=2
# b=3
# c= [add,sub,mul,div]
# c[3](a,b)
# c[1](a,b)
# c[2](a,b)
#calculator
operations = {
    '+':add,
    '-':sub,
    '*':mul,
'/':div,}
a = int(input('Enter a number: '))
z =  input('enter the operation:')
b= int(input('Enter a number: '))

print(f'{a} {z} {b}',end=" = ")
operations[z](a,b)

def square(a):
    return(a**2)
def twice(func,a):
    return func(func(a))
a=5
print(twice(square,a))

