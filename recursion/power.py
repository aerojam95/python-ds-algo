# A recursive funtion that calculates the power of a given number

# Date   : 25-09-2023
# Written by: JAM

def power(x: int, n: int):
    assert n >= 0 and isinstance(n, int), "power only operates on positive integers for the index"
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)