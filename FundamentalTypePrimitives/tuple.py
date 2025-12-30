from typing import Tuple

class User:
    def __init__(self, name: str, age: int):
        self._name: str= name
        self._age: int = age
    
    def getInfo(self) -> Tuple[str,int]:
        return (self._name,self._age)

user1 = User("Adam",25)
print(user1.getInfo()) #('Adam', 25)

example1: Tuple[int,str] = ("Adam", 25) #Type checker will catch error
exmaple2: Tuple[str,int] = ("Adam", 25) #Correct
example1[1] = 26 #TypeError



