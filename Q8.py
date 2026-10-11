
import math

n = int(input("Enter n: "))
k = int(input("Enter k: "))

factors = []

for i in range(1, math.isqrt(n) + 1):
    if n % i == 0:
        factors.append(i)

        if i != n // i:
            factors.append(n // i)

factors.sort()

if k <= len(factors):
    print("K-th factor:", factors[k - 1])
else:
    print(-1)
