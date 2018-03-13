import time
from decimal import *

start = time.clock( )

getcontext().prec = 128

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        # print '\t',f
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def lcm(a,b):
    m = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)

def sum(b, set1, set2):
    s1 = 0
    s2 = 0
    k = 1
    l1 = len(set1)
    l2 = len(set2)
    lb = len(b)
    for i in b[::-1]:
        if l1 >= lb and l1 >= k:
            s1 = s1 + ( p[set1[l1 - k]] if i == '1' else 0 )
        if l2 >= lb and l2 >= k:
            s2 = s2 + ( p[set2[l2 - k]] if i == '1' else 0 )
        k = k + 1
    return (s1, s2)

q = [0] * 81
p = [0] * 81

for i in range(2, 81):
    p[i] = Decimal(1/i**2)

primes = []
for i in range(2, 81):
    if is_prime(i):
        primes.append(i)
# print(primes)

primes_in = [2, 3, 5, 7, 37]
primes_out = []
for prime in primes:
    if not prime in primes_in:
        primes_out.append(prime)

N = 80
set1 = []
for i in range(2, N+1):
    t = False
    for k in primes_in:
        if i % k == 0:
            t = True
            break
    if t: 
        for k in primes_out:
            if i % k == 0:
                t = False
                break
    if t:
        set1.append(i)

# set1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 
#         14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 
#         25, 26, 27, 28, 29, 33, 34, 35, 36, 39, 
#         40, 41, 42, 44, 46, 47, 48, 49, 51, 56, 
#         58, 63, 68, 70, 72, 77]

# print(set1)
set_length = len(set1)
print(set_length)

st_index = 3

com = (set_length - st_index + 1) // 2
print(com)

b = []
for i in range(1, 2**com):
    b.append(bin(i)[2:])

board = st_index + com
# print(board)

s1 = []
s2 = []
for bb in b[::-1]:
    s = sum(bb, set1[st_index:board], set1[board:])
    s1.append(s[0])
    s2.append(s[1])

t = Decimal(1/4 + 1/9 + 1/16)

res = []

def find():

    s1.sort(reverse=True)
    s2.sort()

    z = Decimal('0.0000000000000001')
    cnt = 0
    for s in [Decimal(0.5) - t]:
        k = 0
        k1 = 0
        if s1[0] + s2[len(s2)-1] >= s:
            while True:
                try:
                    st = s1[k] + s2[k1]
                    diff = st - s
                    if abs(diff) <= z:
                        res.append([s1[k], s2[k1], '', '', [2, 3, 4]])
                        cnt = cnt + 1
                        k = k + 1
                        # k1 = k1 + 1
                    elif diff > 0:
                        k = k + 1
                    else:
                        k1 = k1 + 1
                except:
                    break
    print(cnt)


find()

print('find=', time.clock() - start)

def reveal(b, start, end):
    ret = []
    k = 1
    l1 = end - start
    for i in b[::-1]:
        if l1 >= k:
            if i == '1':
                ret.append(set1[start + (l1 - k)])
        k = k + 1
    return ret



for bb in b[::-1]:
    s = sum(bb, set1[st_index:board], set1[board:])
    for r in res:
        if s[0] == r[0]:
            r[2] = bb
        if s[1] == r[1]:
            r[3] = bb

rr = []
for r in res:
    r[4].extend(reveal(r[2], st_index, board))
    r[4].extend(reveal(r[3], board, set_length))
    r[4].sort()
    l = 1
    for kk in r[4]:
        l = lcm(l, kk)
    s = 0
    for kk in r[4]:
        s += ( l / kk ) ** 2
    check = s / l**2
    if check == 0.5 and not r[4] in rr:
        print(r[4])
        rr.append(r[4])

print(len(rr)) 

print('end=', time.clock() - start)