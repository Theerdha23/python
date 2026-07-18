cube = lambda x: x**3
print(cube(5))

large = lambda x,y:x if x>y else y

print(large(3,4))



even = lambda x: x % 2 == 0
print(even(5))
print(even(10))

print_even= lambda x:even(x)
print(print_even(4))

sim=lambda p,r,t:p*r*t/100
print(sim(100,100,100))

con=lambda c: print(f"{(c*9/5)+32}F")
con(38)

ele=lambda u: print("5*u") if u<=100 else print("8*u")
ele(100)
ele(200)
l=[1,7,14,29,6,9,15]
l.sort( key=lambda x:x)
print(l)

login_check=lambda u,p: "login success" if u=="admin" and p=="1234" else "invalid"
print(login_check("admin","1234"))
print(login_check("admin","12349"))


