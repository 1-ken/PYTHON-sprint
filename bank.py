class BankAccount:
    def __init__(self, account_number, balance=0, date_of_opening=None, customer_name=None):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print("Deposit successful. Your new balance is:", self.balance)

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print('You have insufficient balance.')
        else:
            self.balance -= withdraw_amount
            print(f"You have withdrawn {withdraw_amount}. Your new balance is: {self.balance}")

    def check_balance(self):
        print("Your balance is:", self.balance)

    def customer_details(self):
        print(f"Your name is: {self.customer_name}\nYour account number is: {self.account_number}\nThe date of opening of your account is: {self.date_of_opening}")


customer_name = input("Please enter your name: ")
account_number = int(input('Enter your account number: '))
balance = int(input('Enter your start up balance: '))
date_of_opening = input('Enter the date today: ')
customer1 = BankAccount(account_number, balance, date_of_opening, customer_name)

# Deposit
deposit_amount = int(input("Enter the deposit amount: "))
customer1.deposit(deposit_amount)

# Withdraw
withdraw_amount = int(input("Enter the withdrawal amount: "))
customer1.withdraw(withdraw_amount)

# Check balance
customer1.check_balance()

# Customer details
customer1.customer_details()
