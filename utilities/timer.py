from time import perf_counter

def timer(my_func):

    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = my_func(*args, **kwargs)
        finish = perf_counter()
        execution_time = finish - start
        print(f'Function {my_func.__name__} ran in {execution_time} seconds.')
        return result

    return wrapper