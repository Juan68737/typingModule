from typing import ClassVar

class Car:
    total: ClassVar[float] = 0.0
    avarage: ClassVar[float] = 0.0
    amount: ClassVar[int] = 0

    def __init__(self, price: float):
        self._price = price
        Car.total += price
        Car.amount += 1
    
    @classmethod
    def getAverage(cls) -> float:

        cls.average = round(cls.total / cls.amount, 2)
        print(f'The average price of all the cars in the garage is: {cls.average}')

c1 = Car(22000)
c2 = Car(15500.50)
c3 = Car(150000)

Car.getAverage() #62500.17

