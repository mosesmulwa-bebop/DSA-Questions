def fib(n, memo={}):
    """Return the nth element of the fibonacci sequence
    first two elements are 1
    1,1,2,3.....
    elements start from 1 such that fib(1) = 1
    Create new memo on initialization, this memo(a dictionary works best since it is fast access) 
    will be passed to subsequent calls preventing re-computing already calculated values
    """
    if memo.get(n) is not None:
        return memo[n]
    if n <= 2: # first two elements are 1
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2,memo)
    return memo[n]


if __name__ == "__main__":
    print(fib(3))
    print(fib(7))
    print(fib(50))