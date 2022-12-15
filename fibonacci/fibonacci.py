def fib(n):
    """ Computes n-th Fibonacci number. """
    if n == 0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)