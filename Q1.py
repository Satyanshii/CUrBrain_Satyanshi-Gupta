def hasEvenDigits(n):
    count = 0
    n = abs(n)

    if n == 0:
        count = 1
    else:
        while n > 0:
            n = n // 10
            count += 1

    return count % 2 == 0


n = int(input("Enter an integer: "))
print(hasEvenDigits(n))