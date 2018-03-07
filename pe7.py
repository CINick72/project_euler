"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""


def is_prime(numb) -> bool:
    for i in range(2, int(numb/2)):
        if numb % i == 0:
            return False
    return True

cnt = 1
i = 3
while True:
    if is_prime(i):
        cnt += 1
    if cnt == 10001:
        print(i)
        break
    i += 2

# erat = list([x, False] for x in range(3, int(N / 2), 2))
# base = -1
# while True:
#     found = False
#     for i in erat[base+1:]:
#         base += 1
#         if not i[1]:
#             found = True
#             break
#     if found:
#         for i in erat[base+1:]:
#             if not i[1] and i[0] % erat[base][0] == 0:
#                 i[1] = True
#     else:
#         break
# prime = list(filter(lambda x: not x[1],  erat))