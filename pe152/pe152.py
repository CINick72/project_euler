import time

sol = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 18, 20, 21, 24, 28, 30, 35, 36,
        39, 40, 42, 45, 52, 56, 60, 63, 64, 70, 72]

sol2 = []
for i in sol:
    sol2.append(i ** 2)

q = [0] * 81
p = [0] * 81

for i in range(2,81):
    p[i] = 1/i**2

q[80] = p[80]
for i in range(79, 1, -1):
    q[i] = q[i+1] + p[i]

solutions = []
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
            taken.sort()
            if not taken in solutions:
                solutions.append(taken)

t = time.clock()
solve(1, 2, 4, 3, [])
print(time.clock() - t)
print(len(solutions))