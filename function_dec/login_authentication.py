def dec(func):
    def wrapper(*args,**kwargs):
        print("login started")

        print("login finished")
        func(*args, **kwargs)
    return wrapper

user_name="hi"
pass_word="hii"
s=0
u=0

def login(username,password):
    global s
    global u
    if username == user_name and password == pass_word:
        s+=1
        print("Login Successful")
        return
    elif user_name != username:
        u+=1
        if u<=3:
            username = input("Please enter your username again: ")
            login(username,password)
        else:
            print("try again")
            return
    else:
        u+=1
        if u<=3:
            password = input("Please enter your password again: ")
            login(username,password)
        else:
            print("you are not logged in out of attmepts")
login(input("Enter your username: "),input("Enter your password: "))
print(f"unsuccesful attempt {u}")
print(f"succesful attempt {s}")

