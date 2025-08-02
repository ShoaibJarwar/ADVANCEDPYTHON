class NegativeBalanceError(Exception):
    """Raised when balance goes negative"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise NegativeBalanceError("❌ Withdrawal would result in negative balance.")
        self.balance -= amount
        print(f"✅ Withdrawn: {amount} | Remaining balance: {self.balance}")

# Test
account = BankAccount(1000)

try:
    account.withdraw(200)
    account.withdraw(1000)
except NegativeBalanceError as e:
    print(e)
