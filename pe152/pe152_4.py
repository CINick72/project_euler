import time

sol = [i for i in range(0,36)]

sol = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,28,30,35,36,37, 38, 39, 45]

sol2 = []
for i in sol:
    sol2.append(i ** 2)
    

q = [0] * 81
p = [0] * 81

for i in range(2,46):
    p[i] = 1/i**2

q[80] = p[80]
for i in range(79, 1, -1):
    q[i] = q[i+1] + p[i]

# 2,3,4,5,7,12,15,20,28,35
# 2,3,4,6,7,9,12,15,28,30,35,36,45
# 2,3,4,6,7,9,10,20,28,35,36,45
def solve(x, y, d, idx, taken):
    taken.append(int(d ** 0.5))
    x = x * d - y
    y = y * d
    rest = x/y
    n_idx = idx
    for i in sol2[idx:]:
        n_idx += 1
        id = int(i**0.5)
        if i > d and i*x > y and q[id] >= rest and p[id] <= rest:
            solve(x, y, i, n_idx, list(taken))
        elif q[id] < rest:
            break
    t = 1/rest
    if t in sol2:
        t = int(t ** 0.5)
        if not t in taken:
            taken.append(t)
            # taken.sort()
            print(taken)

t = time.clock()
solve(1, 2, 4, 3, [])
print(time.clock() - t)
# x/y = 1/d + x*d - y / y*d, xd > y
# taken = []
# x = 1
# y = 2
# while True:
# d = 0
# for i in sol2:
# if i*x > y and not i in taken:
# d = i
# break
# if d == 0:
# t = (y/x) ** 0.5
# if t in sol2:
# print(t)
# print('solved')
# if len(taken) == len(sol):
# break
# break
# else:
# x = x * d - y
# y = y * d
# taken.append(d)
# print(d)


# print(x, y, x/y, (y/x) ** 0.5)