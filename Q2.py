def reverse_and_double(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    reverse = reverse * sign
    return 2 * reverse


n = int(input("Enter an integer: "))
print(reverse_and_double(n))