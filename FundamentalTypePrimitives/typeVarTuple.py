from typing import TypeVarTuple, Tuple, Generic


'''
https://docs.python.org/3/library/typing.html#typing.Annotated
x: Ts          # Not valid
x: tuple[Ts]   # Not valid
x: tuple[*Ts]  # The correct way to do it
'''
Ts = TypeVarTuple("Ts")

def s3Bucket(*args: *Ts) -> Tuple[*Ts]:
    for item in args:
        print(f"You want to store: {item} \n")
    
    return args

savedItems = s3Bucket("Textbook.pdf", 23000.50, True)
'''
You want to store: Textbook.pdf 

You want to store: 23000.5 

You want to store: True 
'''
print(savedItems) # ('Textbook.pdf', 23000.5, True)

'''
savedItems[2] = False

    savedItems[2] = False
    ~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment

'''


As = TypeVarTuple("As")

class Vector(Generic[*As]):
    def __init__(self, *items: *As):
        self.items = items

    def returnItems(self) -> Tuple[*As]:
        return self.items

vector1 = Vector("Snoopy", 24, True)
print(vector1.returnItems()) # ('Snoopy', 24, True)
print(tuple(type(x) for x in vector1.returnItems())) # (<class 'str'>, <class 'int'>, <class 'bool'>)





