balance = 10000

def check_balance():
    print(f"Your balance is: ₹{balance}")

def deposit(amount):
    global balance

    if amount > 0:
        balance = balance + amount
        print("Amount deposited successfully.")
        check_balance()
    else:
        print("Please enter a valid amount.")

def withdraw(amount):
    global balance

    if amount > 0:
        if amount <= balance:
            balance = balance - amount
            print("Amount withdrawn successfully.")
            check_balance()
        else:
            print("Insufficient balance.")
    else:
        print("Please enter a valid amount.")


print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")

choice = int(input("Enter your choice: "))

if choice == 1:
    amount = int(input("Enter your amount: "))
    deposit(amount)

elif choice == 2:
    amount = int(input("Enter your amount: "))
    withdraw(amount)

elif choice == 3:
    check_balance()

else:
    print("Please enter a valid choice.")