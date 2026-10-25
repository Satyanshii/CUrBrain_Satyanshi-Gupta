
base = int(input("Enter base: "))
power = int(input("Enter power: "))
MOD = int(input("Enter MOD: "))

result = 1 % MOD
i = 0

while i < power:
    result = (result * base) % MOD
    i += 1

print("Result:", result)
