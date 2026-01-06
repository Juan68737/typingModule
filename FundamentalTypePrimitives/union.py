from typing import Union, Literal
class Venmo:
    # def __init__(self, amount: Union[int, float]): Python 3.9 and ealier
    def __init__(self, amount: int | float): # Python 3.10 and up
        self.total_amount = amount
    
    def action(
        self,
        amount: Union[int, float],
        action: Literal["Withdraw", "Deposit"],
    ) -> None:
        if isinstance(amount, bool):
            raise TypeError("amount must be int or float, not bool")
    
        if action == "Withdraw":
            if amount <= self.total_amount:
                self.total_amount -= amount
            else:
                raise ValueError("Insufficient funds")
        
        elif action == "Deposit":
            self.total_amount += amount
        
    def print_total_amount(self) -> None:
        print(self.total_amount)


Jhons_Venmo = Venmo(24.5)
Jhons_Venmo.print_total_amount()
Jhons_Venmo.action(30, "Deposit")
Jhons_Venmo.action(400.23, "Deposit")
Jhons_Venmo.action(20.22, "Withdraw")
Jhons_Venmo.print_total_amount() # 434.51

