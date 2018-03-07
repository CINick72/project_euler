"""
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. 
In fact, there are exactly four numbers below fifty that can be expressed in such a way:
28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4
How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""

import math
def euler(N):
    a = [True] * N
    # Берëм невычеркнутые числа от 2 до sqrt(n)
    for i in range(2, int(math.sqrt(N))):
        # Вычëркиваем числа, кратные невычеркнутому
        for j in range(i * 2, N, i):
            a[j] = False

    b = [i for i in range(2, N) if a[i]]  
    return b

primes = euler(7072)
numbers = set()
cnt = 0
for x in primes:
    for y in primes:
        if y > 369:
            continue
        for z in primes:
            if z > 85:
                continue
            c = x * x + y * y * y + z * z * z * z
            if c <= 50000000:
                numbers.add(c)

print(len(numbers))