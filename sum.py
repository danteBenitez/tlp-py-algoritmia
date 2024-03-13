def sum(a, b):
    """
        Sum two numbers without using the + operator
    """
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

assert sum(0, 1) == 1
assert sum(3, 2) == 5
assert sum(1, 2) == 3
assert sum(4, 5) == 9
print("All test passed.")