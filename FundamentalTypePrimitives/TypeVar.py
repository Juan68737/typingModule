from typing import TypeVar, Iterable

'''
TypeVar(
    name,                    # Can be any name
    *constraints,            # Specify exact types
    bound=None,              # Upper type limit (subclasses allowed)    
    covariant=False,         # More specific types
    contravariant=False,     # More general types
    infer_variance=False,    # Type variables is inferred by type checkers
    default=typing.NoDefault # Provide default type if not provided 
)
'''


T = TypeVar('T')  # Can be anything
S = TypeVar('S', bound=Iterable)  # Can be any subtype of Iterable
A = TypeVar('A', int, float)  # Must be an int, float,

'''
T
'''
def printItem(item: T) -> T:
    print(f'Item: {item}')
    return item

printItem("hi")
printItem(67)

'''
S
'''
def printIterable(iterable: S) -> S:
    print(f'Print Iterable: {[item for item in iterable]}')
    return iterable

printIterable([1,2,3])
printIterable((1,2,3))

'''
A
'''
def printNumbers(numbers: A) -> A:
    print(f"Print Number: {numbers}")
    return numbers

printNumbers(4)
printNumbers(4.2)


