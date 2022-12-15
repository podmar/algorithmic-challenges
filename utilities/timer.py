from time import perf_counter_ns

def timer(my_func):

    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        result = my_func(*args, **kwargs)
        finish = perf_counter_ns()
        execution_time = finish - start
        print(f'Function {my_func.__name__} ran in {execution_time} nanoseconds:\nargs: {args}\nkwargs: {kwargs}')
        return result

    return wrapper