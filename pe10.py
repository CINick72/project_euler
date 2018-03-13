"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
import time
import math

t = time.clock()

N = 2000000
a = [True] * N 
for i in range(2, 1414):
	if a[i]:
		for j in range(i * 2, N, i):
			a[j] = False

s = 0
for i in range(2, N):
	if a[i]:
		s += i
# b = [i for i in range(2, N) if a[i]]     

# s = 0
# for i in b:
#     s += i

print(s)

print(time.clock() - t)