import time

FIB_CONST = 28


def fib(n):
    """Use the slow, recursive formula to calculate Fibonacci numbers.
    
    Arguments:
        n {int} -- Calculate the nth Fibonacci number.
    
    Returns:
        int -- The resulting Fibonacci number.
    """
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


def profile_cpu(n = FIB_CONST):
    """Computes Fibonacci numbers and returns the time elapsed.
    
    Keyword Arguments:
        n {int} -- Calculate the nth Fibonacci number (default: {FIB_CONST})
    
    Returns:
        float -- The total time elapsed in seconds.
    """
    start = time.time()
    fib(n)
    return time.time() - start
