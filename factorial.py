def mult(a, b):
    """
        Multiplies two numbers without using the * operator
    """
    res = 0
    for i in range(b):
        res += a
    return res


def factorial(n):
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res = mult(res, i)
    return res

assert factorial(3) == 6
assert factorial(0) == 1
assert factorial(5) == 120
print("All test passed.")
