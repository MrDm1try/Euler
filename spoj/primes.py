import math


def list_of_primes(n):
    numbers = list(range(2, n + 1))
    i = 0
    candidate = numbers[0]

    while candidate <= math.sqrt(n):
        numbers[numbers.index(candidate) + candidate::candidate] = [0] * ((n // candidate) - 1)
        i += 1
        while numbers[i] == 0:
            i += 1
        candidate = numbers[i]
    return [x for x in numbers if x != 0]


def print_primes_on_interval(m, n):
    if m < 2:
        m = 2
    numbers = list(range(m, n + 1))
    primes = list_of_primes(int(math.sqrt(n)))

    for prime in primes:
        reminder = m % prime
        start_pos = 0 if reminder == 0 else prime - reminder
        numbers[start_pos::prime] = [0] * len(numbers[start_pos::prime])
    for x in primes:
        if x >= m:
            print(x)
    for x in numbers:
        if x != 0:
            print(x)



number_of_repetitions = int(input())
intervals = []
for i in range(number_of_repetitions):
    interval = input().split(' ')
    intervals.append((int(interval[0]), int(interval[1])))

for interval in intervals:
    print_primes_on_interval(*interval)

