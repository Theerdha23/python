def power(base, exponent=2):
    return base ** exponent

print(power(2))
print(power(3,2))
print(power(3,exponent=34))

def connect(host,port = 3306,protocal='tcp'):
    print(f"connection host is {host}")
    print(f"connection port is {port}")
    print(f"connection protocal is {protocal}")

connect('user')
connect('thhh',protocal='http',port=8080)
connect('local',protocal='http')

def func(age,name=  'guest'):
    print(name)
    print(age)

func(age=12)

def discount_pric(price,discount=10):
    print(f'discounted price is {price-discount}')

discount_pric(120)