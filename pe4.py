"""
A palindromic number reads the same both ways. The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindromic(n, k) -> bool:
    tmp = n
    z = []
    k2 = int(k/2)
    for _i in range(0, k):
        z.append(tmp % 10)
        tmp = int(tmp / 10)
    return z[:k2] == list(reversed(z[k2:]))

# for i in range(99, 10, -1):
#     for j in range(99, 10, -1):
#         if is_palindromic(i * j, 4):
#             print(i * j)
#             break

def find():
    max = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            k = i * j
            if is_palindromic(k, 6):
                if k > max:
                    max = k
    return max
        
print(find())

