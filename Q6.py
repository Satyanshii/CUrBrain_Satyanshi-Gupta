def digit_frequency_difference(n: int, a: int, b: int) -> int:
    count_a = 0
    count_b = 0

    if n == 0:
        if a == 0:
            count_a += 1
        if b == 0:
            count_b += 1
    else:
        while n > 0:
            digit = n % 10

            if digit == a:
                count_a += 1
            if digit == b:
                count_b += 1

            n = n // 10

    return abs(count_a - count_b)


n = int(input("Enter a non-negative integer: "))
a = int(input("Enter the first digit (0-9): "))
b = int(input("Enter the second digit (0-9): "))

print(digit_frequency_difference(n, a, b))