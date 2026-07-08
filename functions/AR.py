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

#postional arg and locational arg
def trip_details(total_fare,driver_name,pickup,drop):
    print(f" total fare is {total_fare} and  driver name is {driver_name} and  pickup is {pickup} and  drop is {drop}")

trip_details(1000,"theerrdha",'loc','loc') #poistional

trip_details("theerdha",1000,'mun','hyd')

trip_details(drop = 'you', total_fare= 1000,driver_name= 'mun',pickup= 'hyd') #location arg
# trip_details(drop = 'you',  1000,driver_name= 'mun',pickup= 'hyd') #syntax error
# trip_details(1000,driver_name= 'mun,'loc','loc')
