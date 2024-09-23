"""Write a  Python class BankAccount with attributes like account_number, balance, 
date_of_opening and customer_name, and methods like deposit, withdraw, and 
check_balance."""

class BankAccount:
    def __init__(self,acc_no,customer_name,open_date,balance=0):
        self.acc_no=acc_no
        self.customer_name=customer_name
        self.open_date=open_date
        self.balance=balance

        print("Your account number:",acc_no)
        print("Your name:",customer_name)
        print("Your account opening date:",open_date)
        print("Your Current balance:",balance)
    
    def deposit(self,depositamt):
        self.balance += depositamt
        print("Balance after deposite:",self.balance)
    
    def withdraw(self,withdrawamt):
        self.balance -= withdrawamt
        print("Balance after withdrawal:",self.balance)

    def check_balance(self):
        print("Your Balance:",self.balance)

acc_no=int(input("Enter your account number:"))
customer_name=input("Enter your name:")
open_date=input("Enter account opening date:")
balance=float(input("Enter your balance:"))

obj=BankAccount(acc_no,customer_name,open_date,balance)
while True:
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")

    choice=int(input("Enter your choice:"))

    if(choice==1):
        depositamt=int(input("Enter amount to deposite:"))
        obj.deposit(depositamt)
    elif(choice==2):
        withdrawamt=int(input("Enter amount to withdraw:"))
        obj.withdraw(withdrawamt)
    elif choice == 3:
        obj.check_balance()
    else:
        print("Invalid choice")
        break