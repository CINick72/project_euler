"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


import math
import time



N = 600851475143

def is_prime(numb) -> bool:
    for i in range(2, int(numb/2)):
        if numb % i == 0:
            return False
    return True

def do(N) -> int:
    k = int(N/2)
    for i in range(3, k, 2):
        if N % i == 0:
            p = N / i
            if is_prime(p):
                return p
    return None

if __file__ == "main":
    start_time = time.time()
    print(do(N))
    print("--- %s seconds ---" % (time.time() - start_time))
