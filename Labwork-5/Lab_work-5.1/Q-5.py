class Account:
    def __init__(self,balance=0):
        self.__balance = balance        # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited: $",amount)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrew: $",amount)
        else:
            print("Invalid amount or insufficient balance.")

    def display_balance(self):
        print("Current Balance: $",self.__balance)

user_acc = Account(500)
user_acc.deposit(150)
user_acc.withdraw(100)
user_acc.display_balance()