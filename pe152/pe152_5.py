

import time

t = time.clock()

k = 0
for i in range(2**35):
    k += 1

print(k)
print(time.clock() - t)
    
        