def replaceEvenDigits(n: int) -> list:
    digits = []

    while n > 0:
        digit = n % 10

        if digit % 2 == 0:
            digits.append(0)
        else:
            digits.append(digit)

        n = n // 10

    digits.reverse()
    return digits


n = int(input("Enter a positive integer: "))
print(replaceEvenDigits(n))