from typing import Generic, TypeVar

Key = TypeVar("Key")
Value = TypeVar("Value")

class Map(Generic[Key, Value]):
    def __init__(self, key: Key, value: Value):
        self.key = key
        self.value = value
    
    def __str__(self) -> str:
        return (
            f"The key is {self.key} with type {type(self.key).__name__} "
            f"and the value is {self.value} with type {type(self.value).__name__}"
        )

name_to_age = Map[str,int]("Avery",24)
# The key is Avery with type str and the value is 24 with type int
print(name_to_age)              

homeZipCode_to_owner = Map[int,str](52442,"William")
# The key is 52442 with type int and the value is William with type str
print(homeZipCode_to_owner)

# error: Incompatible types in assignment (expression has type "int", variable has type "str")
name_to_age.key = 24
