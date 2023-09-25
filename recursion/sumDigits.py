# A recursive funtion that finds the sum of the digits of an integer number

# Date   : 25-09-2023
# Written by: JAM

def sumDigits(n: int):
    assert n > 0 and isinstance(n, int), "sumDigits only operates on positive integers"
    if n < 10:
        return n
    else:
        return (n % 10) + sumDigits((n - (n % 10)) // 10)
    