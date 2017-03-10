n = int(input())
for i in range(n):
    num = int(input())
    d = 5
    sum = 0
    while d <= num:
        sum += num // d
        d *= 5
    print(sum)