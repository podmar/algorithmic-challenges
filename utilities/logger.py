from functools import wraps
import logging


def logger(my_func):
    logging.basicConfig(level=logging.INFO)

    @wraps(my_func)
    def wrapper(*args, **kwargs):
        logging.info(
            f'Function {my_func.__name__} ran with:\nargs: {args}\nkwargs: {kwargs}')
        return my_func(*args, **kwargs)

    return wrapper


@logger
def test(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum


if __name__ == '__main__':
    test(6)
