# A recursive funtion that converts a decimal positive integer into a positive
# binary positive integer

# Date   : 25-09-2023
# Written by: JAM

def decimalToBinary(x: int):
     assert x >= 0 and isinstance(x, int), "decimalToBinary only operates on positive integers"
     if x == 0:
        return 0
     else:
         return (10 * decimalToBinary(x // 2)) + (x % 2)
         
print(decimalToBinary(104))