
f = open('pe152/tests.py')

rr = []
for line in f:
    if not line in rr:
        rr.append(line)

print(len(rr))
rr.sort()

f = open('pe152/solutions.txt', 'w+')
f.writelines(rr)