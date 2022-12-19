from time import perf_counter_ns
from functools import wraps

from logger import logger


def timer(my_func):

    @wraps(my_func)
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        result = my_func(*args, **kwargs)
        finish = perf_counter_ns()
        execution_time = finish - start
        print(
            f'Function {my_func.__name__} ran in {execution_time} nanoseconds:\nargs: {args}\nkwargs: {kwargs}')
        return result

    return wrapper


@logger
@timer
def test(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum


if __name__ == '__main__':
    test(6)
