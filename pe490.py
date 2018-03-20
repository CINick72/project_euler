
steps = [-3, -2, -1, 1, 2, 3]
global_cnt = [0]
sol = []
for i in range(0, 16):
    sol.append([])
def step(n, pos, visited: list, lv):
    if pos == n and lv == pos - 1:
        global_cnt[0] += 1
        sol[n].append(list(visited))
        # print(visited)
    else:
        visited.append(pos)
        for s in steps:
            new_pos = pos + s
            if new_pos > 0 and new_pos <= n and not new_pos in visited:
                step(n, new_pos, visited, lv + 1)
        visited.remove(pos)


def f(n):
    visited = []
    pos = 1
    global_cnt[0] = 0
    step(n, pos, visited, 0)
    print(n, global_cnt)

coeff = [2, -1, 2, 1, 1, 0, -1, -1]
s = [0, 1, 1, 1, 2, 6, 14, 28, 56]
# , 1140, 2401, 5074, 10738, 22711, 48001

N = 10 ** 9
def f1(n):
    f1n = 0
    k = 1
    n = len(s)
    for c in coeff:
        f1n = (f1n + (s[n - k] * c) % N ) % N
        k = k + 1
    return f1n

f3 = 0
for ss in s:
    f3 = f3 + ss ** 3
for i in range(9, 10 ** 14):
    f1n = f1(i)
    s.append(f1n)
    s = s[1:]
    f3 = ( f3 + ( f1n ** 3 ) % N ) % N

print(f3)