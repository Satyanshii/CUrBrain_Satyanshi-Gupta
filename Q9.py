
import math

n = int(input("Enter n: "))

candidate = max(2, n + 1)

while True:
    is_prime = True

    if candidate > 2 and candidate % 2 == 0:
        is_prime = False
    else:
        for i in range(2, math.isqrt(candidate) + 1):
            if candidate % i == 0:
                is_prime = False
                break

    if is_prime:
        print("Next prime:", candidate)
        break

    candidate += 1
