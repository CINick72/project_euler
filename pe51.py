"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, 
this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, 
by replacing part of the number (not necessarily adjacent digits) with the same digit, 
is part of an eight prime value family
"""

from pe3 import is_prime

def digits(n):
    tmp = n
    z = []
    for _i in range(0, 5):
        z.append(tmp % 10)
        tmp = int(tmp / 10)
    z.reverse( )
    return z

# cnt = 0
# for i in range(10000, 99999):
#     d = digits(i)
#     for k in [0,1,2]:
#         if d.count(k) == 3:
#             for j in [1,3,7,9]:
#                 c = i * 10 + j
#                 if is_prime(c):
#                     cnt = 1
#                     for p in range(k+1, 10):
#                         s = 0
#                         for dd in d:
#                             s = s*10 + ( dd if dd != k else p )
#                         s = s * 10 + j
#                         if is_prime(s):
#                             cnt = cnt + 1
#                     if cnt == 8:
#                         print(c)
#                         print(d)
#                         for p in range(k+1, 10):
#                             s = 0
#                             for dd in d:
#                                 s = s*10 + ( dd if dd != k else p )
#                             s = s * 10 + j
#                             print(s)
# print('Done')                    

k = [121313,
     222323,
     323333,
     424343,
     525353,
     626363,
     727373,
     828383,
     929393]
    
for p in k:
    print(is_prime(p))