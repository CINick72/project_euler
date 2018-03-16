
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

for i in range(1, 15):
    f(i)

for i in range(15,1,-1):
    for j in range(2, i):
        cnt = 0
        for s in sol[j]:
            for s1 in sol[i]: #type: list
                if s1[:j-1] == s:
                    cnt += 1
        print(i, j, cnt)

# s = [0, 0, 1, 1, 2, 6, 14, 28, 56, 118, 254, 541, 1140, 2401, 5074, 10738, 22711, 48001]

# ss = [0] * 18
# ss[1] = 1
# ss[2] = 1
# ss[3] = 1
# for i in range(4, 18):
#     for j in range(1, i):
#         ss[i] += s[i - j]*s[j]

# print(ss)

# for i in range(4, 18):
#     print(i, s[i] - ss[i])