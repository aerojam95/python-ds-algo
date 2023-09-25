# A recursive funtion that find the greatest common denominator of two integer
# numbers

# Date   : 25-09-2023
# Written by: JAM

def gcd(x: int, y: int):
    assert x >= 0 and isinstance(x, int), "gcd only operates on positive integers"
    assert y >= 0 and isinstance(y, int), "gcd only operates on positive integers"
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
        
print(gcd(3, 5))