import logging

def logger(my_func):
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(f'Function {my_func.__name__} ran with:\nargs: {args}\nkwargs: {kwargs}')
        return my_func(*args, **kwargs)

    return wrapper