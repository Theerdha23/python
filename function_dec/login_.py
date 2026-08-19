def dec1(func):
    def wrapper(*args,**kwargs):
        print("login stared")
        func(*args,**kwargs)
        print("login finished")
    return wrapper
uns=0
sa=0
na=0
user_name="Theerdha"
password="theerdha"

@dec1
def login(user,passw):
    global uns
    global sa
    global na
    if user_name==user and passw==password:
        print("login successful")
        sa+=1
    else:
        print("login failed")
        uns+=1
    na=uns+sa
for i in range(3):
    login(user=input("enter username:"),passw=input("enter password:"))
    if sa==1 or uns==3:
        break
if sa>=1:
    print(f"login successful in {na} attempts ")
else:
    print(f"login failed in {uns} attempts ")


attempts=0
def dec(func):
    def wrapper(*args,**kwargs):
        global attempts
        attempts+=1
        func(*args,**kwargs)
    return wrapper
@dec
def login(username,password):
    print(f"Login attempted by {username}")

login("admin","th")
login("username","24")
login("password","34")
print(f"total attempts: {attempts}")
balance = 12000

def dec(func):
    def wrapper(username, password, amount):
        if username == "admin" and password == 1234:
            func(username, password, amount)
        else:
            print("Invalid credentials")
    return wrapper
@dec
def withdraw_s(username, pin, amount):
    global balance

    if balance >= 10000:
        if amount > 0 and amount <= balance:
            balance = balance - amount
            print(f"remaining balance is {balance}")

withdraw_s("admin", 1234, 1000)

attempts = 0
def track_attempt(func):
    def wrapper(*args, **kwargs):
        global attempts
        attempts += 1
        return func(*args, **kwargs)
    return wrapper

def login_required(func):
    def wrapper(username, password, exam_name):
        if username == "admin" and password == "1234":
            return func(username, password, exam_name)
        else:
            print("Invalid credentials")
    return wrapper
@track_attempt
@login_required
def start_exam(username, password, exam_name):
    print(f"Exam started for {username}")
    print(f"Exam name: {exam_name}")
start_exam("admin", "1234", "Python")
start_exam("admin", "1234", "Java")
start_exam("student", "1111", "Python")
print("Total number of exam attempts:", attempts)






