"""
Euler discovered the remarkable quadratic formula:
n^2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41
is clearly divisible by 41.
The incredible formula n^2−79n+1601
was discovered, which produces 80 primes for the consecutive values 0≤n≤79
. The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
    n^2+an+b
, where |a|<1000 and |b|≤1000
where |n|
is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a
and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n,
 starting with n=0.
"""


import time

primes = []
def is_prime(numb) -> bool:
    if numb < 0:
        numb = numb * -1
    if not numb in primes:
        for i in range(2, int(numb/2)):
            if numb % i == 0:
                return False
        primes.append(numb)
        return True
    else:
        return True

t = time.clock()

bs = []
for b in range(-1000, 1001):
    if is_prime(b):
        bs.append(b)

maxn = 0
maxa = 0
maxb = 0
for a in range(-999, 1000, 2):
    for b in bs:
        n = 0
        while True:
            p = n * n + a * n + b
            if not is_prime(p):
                if n > maxn:
                    maxn = n
                    maxa = a
                    maxb = b
                break
            else:
                n = n + 1

print(time.clock() - t)

print(maxn)
print(maxa)
print(maxb)

print(maxa * maxb)