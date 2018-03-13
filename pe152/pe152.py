"""
There are several ways to write the number 1/2 as a sum of inverse squares using distinct integers.
For instance, the numbers {2,3,4,5,7,12,15,20,28,35} can be used:
In fact, only using integers between 2 and 45 inclusive, there are exactly three ways to do it, 
the remaining two being: {2,3,4,6,7,9,10,20,28,35,36,45} and {2,3,4,6,7,9,12,15,28,30,35,36,45}.
How many ways are there to write the number 1/2 as a sum of inverse squares using distinct integers
between 2 and 80 inclusive?
"""
import time
import math
from decimal import *

def abs(n):
    return n if n > 0 else -n

def sum(b, set1, set2):
    s1 = 0
    s2 = 0
    k = 1
    l1 = len(set1)
    l2 = len(set2)
    for i in b[::-1]:
        if l1 >= k:
            s1 = s1 + ( set1[l1 - k] if i == '1' else 0 )
        if l2 >= k:
            s2 = s2 + ( set2[l2 - k] if i == '1' else 0 )
        k = k + 1
    return (s1, s2)

def find_subset_sums(sol_var) -> [int]:
    subsets = [[]]
    for m in sol_var:
        l = len(subsets)
        for i in range(l):
            new_subset = list(subsets[i])
            new_subset.append(m)
            subsets.append(new_subset)

    subsets_sums = [0] * len(subsets)
    for i in range(len(subsets_sums)):
        s = 0
        for m in subsets[i]:
            s = s + p[m]
        subsets_sums[i] = s
    
    return (subsets, subsets_sums)

t = time.clock( )

getcontext().prec = 128

q = [0] * 81
p = [0] * 81

for i in range(2,81):
    p[i] = Decimal(1/i**2)

q[80] = p[80]
for i in range(79, 1, -1):
    q[i] = q[i+1] + p[i]


b = []
for i in range(1, 2**18):
# for i in range(1, 2**17):
    b.append(bin(i)[2:])

s1 = []
s2 = []
for bb in b[::-1]:
    s = sum(bb, p[46:64], p[64:81])
    # s = sum(bb, p[12:29], p[29:46])
    s1.append(s[0])
    s2.append(s[1])

# s1.sort(reverse=True) 
# s2.sort()

v1 = [12,15,20,28,35]
v2 = [20,28,35,36,45]
v3 = [12,15,28,30,35,36,45]

v1_sums = find_subset_sums(v1)
v2_sums = find_subset_sums(v2)
v3_sums = find_subset_sums(v3)

t = Decimal('0.00526077097505668936881784158998698330833576619625091552734375')
for i in range(len(v1_sums[1])):
    if v1_sums[1][i] == t:
        print(v1_sums[0][i])

for i in range(len(v2_sums[1])):
    if v2_sums[1][i] == t:
        print(v2_sums[0][i])

for i in range(len(v3_sums[1])):
    if v3_sums[1][i] == t:
        print(v3_sums[0][i])     

t1 = Decimal('0.0032773679134710907039952643149405275835306383669376373291015625')   
k = -1
for i in s1:
    k = k + 1
    if i == t1:
        print(k)

t2 = Decimal('0.0019834030615823289279107954907743760486482642590999603271484375')   
k = -1
for i in s2:
    k = k + 1
    if i == t2:
        print(k)

print('Done')

# v_sums = []
# v_sums.extend(v1_sums)
# v_sums.extend(v2_sums)
# v_sums.extend(v3_sums)
# col_sum = []
# for vm in v_sums:
#     if not vm in col_sum:
#         col_sum.append(vm)

# cnt1 = 0
# cnt2 = 0
# cnt3 = 0
# cnt = 0
# for s in col_sum:
#     k = 0
#     k1 = 0 
#     if s1[0] + s2[len(s2)-1] >= s:
#         while True:
#             try:
#                 st = s1[k] + s2[k1]
#                 diff = st - s
#                 if abs(diff) <= Decimal(0.00000000000001):
#                     print(s, s1[k], s2[k1])
#                     cnt = cnt + 1
#                     if s in v1_sums:
#                         cnt1 += 1
#                     if s in v2_sums:
#                         cnt2 += 1                        
#                     if s in v3_sums:
#                         cnt3 += 1                        
#                     break
#                 elif diff > 0:
#                     k = k + 1
#                 else:
#                     k1 = k1 + 1
#             except:
#                 break

# print(cnt, cnt1, cnt2, cnt3)
# print(time.clock( ) - t)


# # print(p)
# # print(q)

# cnt = [0]
# def find(s, next, l):
#     s = s + p[next]
#     if abs(1 - 2*s) < 0.000000000001:
#         cnt[0] = cnt[0] + 1
#         print(l)
#         return
#     elif s > 0.5:
#         return
#     else:
#         for i in range(next+1, 46):
#             if 0.5 - s <= q[i]:
#                 # l.append(i)
#                 find(s,i, l)
#                 # l.remove(i)
#             else:
#                 return

# l = [2]
# find(0, 2, l)
# print(cnt)


