from typing import Final

class Car:
    
    def __init__(self, wheels_amount: int):
        self.wheels_amount: Final[int] = wheels_amount
        self.WHEELS_AMOUNT_V2: int = wheels_amount # This is better practice
    
BMW = Car(4)

print(BMW.wheels_amount) #4
BMW.wheels_amount = 6
print(BMW.wheels_amount) 
