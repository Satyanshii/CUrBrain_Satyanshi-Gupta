
n = int(input("Enter n: "))

if n <= 2:
    print(0)
else:
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p < n:
        if is_prime[p]:
            for i in range(p * p, n, p):
                is_prime[i] = False
        p += 1

    print("Number of primes:", sum(is_prime))
