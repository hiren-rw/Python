# Q.5: Custom InsufficientBalanceError in withdraw(amount)

class InsufficientBalanceError(Exception):
    pass

def withdraw(amount):
    balance = 5000

    if amount > balance:
        raise InsufficientBalanceError("Not Enough Balance!")
    print(f"\nRs. {amount} Withdrawn Successfully")

withdraw(1000)      # Valid input
withdraw(8000)      # Invalid input (Raises Error)