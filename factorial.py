def mult(a, b):
    """
        Multiplies two numbers without using the * operator
    """
    if a == 0 or b == 0: return 0
    return a / (1 / b)

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
