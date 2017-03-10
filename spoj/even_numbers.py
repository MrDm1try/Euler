def revert(num):
    res = 0
    while num:
        res <<= 1
        res |= num & 1
        num >>= 1
    return res

n = int(input())
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num if num % 2 == 1 else revert(num))

for i in numbers:
    print(i)