class bank:

    def __init__(self,ac_number,balance,pin):
        self.ac_number=ac_number
        self.balance=balance
        self.pin=pin

    def deposit(self,amount):
        self.amount=amount
        if amount<0:
            print("you cannot deposit negative amount")
        else:
            self.balance+=amount
    def withdraw(self,amount):
        self.amount = amount
        if self.amount<0:
            print("you cannot withdraw negative amount")
        elif self.amount>self.balance:
            print("you cannot withdraw ")
        else:
            self.balance-=amount
            return self.balance
    def check_balance(self):
        return self.balance

# b1=bank(1,1000,124)
# print(b1.check_balance())
# b1.deposit(1000)
# print(b1.check_balance())
# b1.withdraw(1000)
# print(b1.check_balance())
bhaai=bank(1111,20000,123)
print("account creation succesful")
if bhaai.ac_number==int(input("enter account number")):
    if bhaai.pin==int(input("enter pin number")):
        print("1.withdraw\n2.deposit\n3.check balance")

        while True:
            ch = int(input("enter choice"))
            if ch==1:
                print(bhaai.withdraw(int(input("enter amount "))))
            elif ch==2:
                print(bhaai.deposit(int(input("enter amount "))))
            elif ch==3:
                print(bhaai.check_balance())
            else:
                break
    else:
        print("invalid pin")
else:
    print("acc does not exist")

