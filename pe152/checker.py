
def lcm(a,b):
    m = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)

def check(r):
    l = 1
    for kk in r:
        l = lcm(l, kk)
    s = 0
    for kk in r:
        s += ( l / kk ) ** 2
    check = s / l**2
    print(check)

check([2, 3, 4, 6, 8, 9, 12, 15, 18, 20, 24, 30, 40, 72])