def fib(n: int) -> int:
    """ The funtion returns the n-th number in the Fibonacci sequence
    """
    result: int

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fib(n-2) + fib(n-1)

    return result
