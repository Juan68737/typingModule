from typing import Concatenate, ParamSpec, Callable, TypeVar, List

P = ParamSpec("P")
R = TypeVar("R")

def validate_int_list(func: Callable[P, R]) -> Callable[Concatenate[str, P], R]:
    def wrapper(name: str, *args: P.args, **kwargs: P.kwargs) -> R:
        print(f"{name} is calling this function")
        return func(*args, **kwargs)
    return wrapper


@validate_int_list
def sum_of_list(values: List[int]) -> int:
    return sum(values)

'''
Bruno is calling this function
15
'''
print(sum_of_list("Bruno",[1, 2, 3, 4, 5]))    
