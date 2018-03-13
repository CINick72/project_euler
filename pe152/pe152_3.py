
def func(n):
    return [n+1, n*(n+1)]

n = [[2]]
k = 0
for i in n:
    for c in i:
        p = func(c)
        if int(p[0] ** 0.5)**2 ==  p[0]:
            print(p[0])
        if int(p[1] ** 0.5)**2 ==  p[1]:
            print(p[0])            
        n.append(p)
    k = k + 1
    if k > 500:
        break

# print(n)