##9. Create a set of random numbers. Add more numbers until the set has 10 unique
##elements. Also, remove the smallest and largest element.

import random
s=set()
while len(s)<10:
    s.add(random.randint(1,100))
print(s)
s=sorted(s)
s.pop(0)
s.pop(-1)
print(s)

