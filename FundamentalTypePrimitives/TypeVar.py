from typing import TypeVar

T = TypeVar("T")

def printItem(item: T) -> T:
    print(f'Item: {item}')
    return item

printItem("hi")
printItem(67)