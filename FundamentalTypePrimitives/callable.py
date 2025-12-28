from typing import Callable, List

def sumDictValue(function: Callable[[dict], int], data: dict) -> int:
    return function(data)

def addDict(dictionary: dict) -> int:
    return sum(dictionary.values())

values = {"a": 1, "b": 2, "c": 3}

result = sumDictValue(addDict, values)
print(result)  # 6


def validate_int_list(func: Callable[[List[int]], int]) -> Callable[[List[int]], int]:
    def wrapper(values: List[int]) -> int:
        if not isinstance(values, list):
            raise TypeError("Input must be a list")

        if not all(isinstance(v, int) for v in values):
            raise ValueError("All elements must be integers")

        return func(values)
    return wrapper

@validate_int_list
def sum_of_list(values: List[int]) -> int:
    return sum(values)

print(sum_of_list([1,2,3,4,5]))

