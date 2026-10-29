from abc import ABC, abstractmethod


# 1. ABSTRACTION
class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


# 2. ENCAPSULATION (Base Class)
class BankAccount(Account):
    def __init__(self, acc_number, initial_balance):
        # Private attributes (cannot be accessed directly outside the class)
        self.__acc_number = acc_number
        self.__balance = initial_balance

    # Getter method to safely view the balance
    def get_balance(self):
        return self.__balance

    # Helper method for child classes to adjust the balance internally
    def _set_balance(self, amount):
        self.__balance = amount

    def deposit(self, amount):
        if amount > 0:
            current = self.get_balance()
            self._set_balance(current + amount)
            print(f"Deposited ${amount}. New Balance : ${self.get_balance()}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance():
            current = self.get_balance()
            self._set_balance(current - amount)
            print(f"Withdrew ${amount}. Remaining Balance : ${self.get_balance()}")
            return True
        else:
            print("Withdrawal denied: Insufficient funds or invalid amount.")
            return False


# 3. INHERITANCE
class SavingsAccount(BankAccount):
    def __init__(self, acc_number, initial_balance, interest_rate):
        # Inherit properties from BankAccount
        super().__init__(acc_number, initial_balance)
        self.interest_rate = interest_rate  # Unique attribute for savings

    def add_interest(self):
        # Calculate interest based on current balance
        interest = self.get_balance() * self.interest_rate
        current = self.get_balance()
        self._set_balance(current + interest)
        print(f"Added {self.interest_rate*100}% interest (${interest:.2f}). \nNew Balance : ${self.get_balance():.2f}")


# 4. POLYMORPHISM (Overriding the withdraw method)
class CurrentAccount(BankAccount):
    def __init__(self, acc_number, initial_balance, overdraft_limit):
        super().__init__(acc_number, initial_balance)
        self.overdraft_limit = overdraft_limit  # Unique attribute for current account

    # Overriding the parent withdraw method to allow negative balances
    def withdraw(self, amount):
        available_total = self.get_balance() + self.overdraft_limit
        
        if 0 < amount <= available_total:
            current = self.get_balance()
            self._set_balance(current - amount)
            print(f"Withdrew ${amount} (Overdraft used if negative). Current Balance: ${self.get_balance()}")
            return True
        else:
            print(f"Withdrawal denied : Exceeded overdraft limit of ${self.overdraft_limit}.")
            return False


# TEST SECTION
print("--- Testing Savings Account ---")
# Create a savings account with a $1,000 balance and a 5% (0.05) interest rate
savings = SavingsAccount(acc_number="SAV123", initial_balance=1000, interest_rate=0.05)
savings.deposit(500)
savings.add_interest()
savings.withdraw(200)

print("\n--- Testing Current Account ---")
# Create a current account with a $500 balance and a $300 overdraft allowance
current = CurrentAccount(acc_number="CUR789", initial_balance=500, overdraft_limit=300)
current.deposit(100)
# This will dip into the overdraft allowance (leaves balance at -$100)
current.withdraw(700) 
# This will fail because it exceeds the allowed -$300 limit
current.withdraw(500) 