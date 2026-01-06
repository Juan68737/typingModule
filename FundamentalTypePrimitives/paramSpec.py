from typing import ParamSpec, Callable, TypeVar, List

P = ParamSpec("P")
R = TypeVar("R")

def validate_int_list(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:

        return func(*args, **kwargs)
    return wrapper


@validate_int_list
def sum_of_list(values: List[int]) -> int:
    return sum(values)


print(sum_of_list([1, 2, 3, 4, 5]))    # 15
print(sum_of_list([1, 2.2, 3, 4, 5]))  # error: List item 1 has incompatible type "float"; expected "int" 

