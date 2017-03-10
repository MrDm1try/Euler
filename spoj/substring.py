import sys

for line in sys.stdin:
    sub = input()
    s = input()
    i = 0
    s1, s2, s = s.partition(sub)

    while s:
        i += len(s1)
        print(i)
        i += len(sub)
        s1, s2, s = s.partition(sub)

    if (i > 0):
        print()