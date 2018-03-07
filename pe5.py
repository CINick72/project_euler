"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time

t = time.clock( )
def pe5():
    i = 40
    while True:
        i += 20
        t = True
        for k in range(3, 20):
            t = t and (i % k == 0)
            if not t:
                break
        if t:
            return i

print(pe5())

print(time.clock( ) - t)