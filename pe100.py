"""
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.
The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.
By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
"""

import math
from decimal import *

getcontext().prec = 128

n = 120
b = 85
dn = Decimal(n)
db = Decimal(b)
while dn < 10 ** 12:
    new_n = int(dn * ( dn / db + 1 ) ** 2)
    new_b = int(db * ( dn / db + 1 ) ** 2) - 1
    print(new_b)
    print(new_n)
    print('--------')
    dn = Decimal(new_n)
    db = Decimal(new_b)
print('Done')



# n = 10 ** 12
# n = 1059592727822
# b = int(n * 0.7071045)

# while True:
#     b = b + 1
#     x = Decimal(1+8*(b**2-b))
#     x2 = Decimal.sqrt(x)
#     # x = (1+8*(b**2-b))
#     # x2 = math.sqrt(x)    
#     if int(x2) % 2 == 1 and int(x2) == x2:
#         x = (x2 + 1) / 2
#         if x < n:
#             continue
#         break
#         p = Decimal(x * x - x)
#         p1 = Decimal(2 * (b*b - b))
#         if p1 == p:
#             print(p, p1)
#             break


# print(b)
# print(x)


