n = int(input())
numbers = []
for i in range(n):
    line = input().split(' ')
    s = str(int(str(int(line[0]))[::-1]) + int(str(int(line[1]))[::-1]))[::-1]
    while s[0] == '0':
        s = s[1:]
    print(s)