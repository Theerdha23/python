class PasswordUtils:
    def __init__(self,password,email):
        self.password=password
        self.email=email

    @staticmethod
    def is_strong(password):
        digit_check=False
        upper_check=False
        for i in password:
            if i.isdigit():
                digit_check=True
            if i.isupper():
                upper_check=True
        return len(password)>=8 and digit_check and upper_check
    @staticmethod
    def hint(password):
        return password[:2]+"****"
    @staticmethod
    def check_email(email):
        return "@" in email and "." in email

pwd = "ABCWYSS@123"
print(PasswordUtils.hint(pwd))
print(PasswordUtils.check_email("abccd@gmail.com"))
print(PasswordUtils.is_strong(pwd))




class library:
    library_name="hislib"
    def __init__(self,books_list,member_name):
        if member_name =="":
            print("Please enter a member's name"
            )
        else:
            self.books_list=books_list
            self.member_name=member_name

    def is_vaid(title):
        return title != ""
    def add_t(self,title):
        if library.is_vaid(title):
            self.books_list.append(title)
    @classmethod
    def guest(cls):
        return library(["bef","grgr"],"guest")
user1 = library(["ABC", "DEF"], "User1")
user2 = library(["LMN", "OPQ"], "User2")

user1.add_t("PQL")
print(user1.books_list)

guest = library.guest()
print(guest.member_name)
# print(type(guest))

class student:
    count=0
    def __init__(self,s_name,s_roll,marks):
        self.s_name=s_name
        self.s_roll=s_roll
        self.marks=marks
        student.count+=1
    def display(self):
        print(self.s_name,self.s_roll,self.marks)
    def per(self,total_marks):
        return (sum(self.marks)/total_marks)*100
    @classmethod
    def count_s(cls):
        print(cls.count)
    @staticmethod
    def re(marks):
        return print("pass") if marks>40 else "fail"
s1 = student("Theerdha", 101, [80, 75, 90, 85, 70])
s2 = student("Rahul", 102, [60, 55, 45, 70, 65])
s3 = student("Kiran", 103, [35, 30, 45, 38, 32])

s1.display()
print("Percentage:", s1.per(500))
print()

s2.display()
print("Percentage:", s2.per(500))
print()

s3.display()
print("Percentage:", s3.per(500))
print()
print("Total students:", student.count_s())

print("Result:", s1.re(40))
print("Result:", student.re(35))

class BankAccount:
    bank_name="accc bank"
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if BankAccount.check_withdrawal(amount) and amount<=self.balance:
            self.balance-=amount
            return self.balance
        return "Invalid withdrawal"
    def display_balance(self):
        print(self.balance)
    @classmethod
    def display_bank(cls):
        print(cls.bank_name)
    @staticmethod
    def check_withdrawal(amount):
        return amount>0

a1=BankAccount("Theerdha",101,5000)
a2=BankAccount("Rahul",102,8000)
a1.deposit(2000)
a1.withdraw(1000)
a1.display_balance()
a2.deposit(3000)
a2.withdraw(2000)
a2.display_balance()
BankAccount.display_bank()
print(BankAccount.check_withdrawal(500))
print(BankAccount.check_withdrawal(-100))

class Appointment:
    hospital_name="Apollo Hospital"
    def __init__(self,patient_name,doctor_name,fee):
        self.patient_name=patient_name
        self.doctor_name=doctor_name
        self.fee=fee
    def display(self):
        print(self.patient_name,self.doctor_name,self.fee)
    def final_amount(self):
        return self.fee
    @classmethod
    def hospital(cls):
        print(cls.hospital_name)
    @staticmethod
    def check_fee(fee):
        return fee>0

a1=Appointment("Theerdha","Dr.Ravi",500)
a2=Appointment("Rahul","Dr.Kiran",800)
a1.display()
print(a1.final_amount())
a2.display()
print(a2.final_amount())
Appointment.hospital()
print(Appointment.check_fee(500))
print(Appointment.check_fee(0))

