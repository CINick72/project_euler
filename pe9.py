"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc
"""

done = False
for a in range(500):
    for b in range(500):
        c = 2 * a * b - 2 * a * 1000 - 2 * b * 1000 + 1000 * 1000
        if c == 0:
            done = True
            break
    if done:
        break

c = 1000 - a - b
print(a)
print(b)
print(c)

print(a * a + b * b - c * c)
print(a * b * c)