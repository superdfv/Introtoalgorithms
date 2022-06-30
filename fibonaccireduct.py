# Fibonacci function reduce to polynomial time P

def fib(n):
    current = 0
    parent = 1
    grandparent = 0
    if n <= 1:
        return n

    for i in range(n-1):
        current = parent + grandparent
        grandparent = parent
        parent = current
    return parent


n = 8
fib(160)