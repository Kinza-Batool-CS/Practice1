class InsufficientFundsError(Exception):
    pass
class BankAccount:
    def __init__(self, owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self, amount):
         self.balance +=amount

    def withdraw(self, amount):
        if amount> self.balance:
          raise InsufficientFundsError(f"Cannot withdraw  {amount}, balance is {self.balance}")
        self.balance-=amount
BA=BankAccount("ABC",1000)
BA.deposit(500)
BA.withdraw(300)
print(BA.balance)

try:
    BA.withdraw(5000)
except InsufficientFundsError as e:
    print("Error : ", e)
