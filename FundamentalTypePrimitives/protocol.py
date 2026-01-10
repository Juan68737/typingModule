from typing import Protocol

class Bank(Protocol):
    _name: str
    _balance: int | float

    def withdraw(self, amount: int | float) -> None:
        ...

    def deposit(self, amount: int | float) -> None:
        ...

class WellsFargo:
    def __init__(self, name: str, starting_balance: int | float):
        self._name = name
        self._balance = starting_balance

    def withdraw(self, amount: int | float) -> None:
        self._balance -= amount

    def deposit(self, amount: int | float) -> None:
        self._balance += amount


class Chase:
    def __init__(self, name: str, starting_balance: int | float):
        self._name = name
        self._balance = starting_balance

    def withdraw(self, amount: int | float) -> None:
        self._balance -= amount

    def deposit(self, amount: int | float) -> None:
        self._balance += amount

def checkBankBalance(bank: Bank) -> None:
    print(f"Your balance is {bank._balance} from {bank._name}")

wells = WellsFargo("Wells Fargo", 1000)
chase = Chase("Chase", 500)

checkBankBalance(wells) # Your balance is 1000 from Wells Fargo
checkBankBalance(chase) # Your balance is 500 from Chase
