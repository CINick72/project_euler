"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""


import time
import math

N = 2000000
# Выписать подряд все целые числа от 2 до n (2, 3, 4, …, n).
a = [True] * N
# Берëм невычеркнутые числа от 2 до sqrt(n)
for i in range(2, int(math.sqrt(N))):
	# Вычëркиваем числа, кратные невычеркнутому
	for j in range(i * 2, N, i):
		a[j] = False

b = [i for i in range(2, N) if a[i]]     

s = 0
for i in b:
    s += i

print(s)