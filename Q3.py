
def palindrome_or_sum(n: int) -> int:
    if n < 0:
        reverse = 0
        temp = abs(n)

        while temp > 0:
            digit = temp % 10
            reverse = reverse * 10 + digit
            temp //= 10

        reverse = -reverse
        return n + reverse

    original = n
    temp = n
    reverse = 0

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10

    if original == reverse:
        return original
    else:
        return original + reverse


n = int(input("Enter an integer: "))
print(palindrome_or_sum(n))