import math


def _list_primes(n):
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


def get_primes_on_interval(m, n):
    if m < 2:
        m = 2
    numbers = list(range(m, n + 1))
    primes = _list_primes(int(math.sqrt(n)))

    for prime in primes:
        reminder = m % prime
        start_pos = 0 if reminder == 0 else prime - reminder
        numbers[start_pos::prime] = [0] * len(numbers[start_pos::prime])
    return [x for x in primes if x >= m] + [x for x in numbers if x != 0]


# import threading
# import time
#
# running = True
# file = None
# file_lock = threading.Lock()
#
#
# class Thr:
#
#     def __init__(self):
#         self._running = True
#         self.file = None
#         self.file_lock = threading.Lock()
#
#     def count(self):
#         i = 0
#         while self._running:
#             self.file_lock.acquire()
#             with open(self.file, 'a') as f:
#                 f.write(str(i))
#             self.file_lock.release()
#             i += 1
#
#     def start(self):
#         t1 = threading.Thread(target=self.count)
#         t1.start()
#
#     def stop(self):
#         self._running = False
#
#     def change_file(self, filename):
#         self.file_lock.acquire()
#         self.file = filename
#         self.file_lock.release()
#
#
# r = Thr()
# r.change_file('123.txt')
# r.start()
# time.sleep(2)
# r.change_file('456.txt')
# time.sleep(2)
# r.change_file('789.txt')
# time.sleep(2)
# r.stop()


# def char_in_string(line, char):
#     #return c in l
#
#     for c in line:
#         if c == char:
#             return True
#     return False
#
# line = input("A string needed:\n")
# char = ''
# while len(char) != 1:
#     char = input("A character needed:\n")
#
# if char_in_string(line, char):
#     print("Yeah, it's inside")
# else:
#     print("Nope, it's not there")

# l = logging.getLogger(__name__)

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s \t%(levelname)s\t%(name)s\t%(message)s', filename='1.txt')
#
# console_output_handter = logging.StreamHandler(sys.stdout)
# ch.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s \t%(levelname)s\t%(name)s\t%(message)s')
# ch.setFormatter(formatter)
# l.addHandler(ch)
#
# l.info('lll')
# l.debug('ppp')

# def love():
#     x = len("love")
#     for i in range(19):
#         x = (128 * x + 314) % 127
#         yield x
#
# na = 'Fr/ku~>_d49XjL:1dHr"P\r3\x0b^N!ajrdKPpU4boG<of:iX#pvf  twvz;eiDB!z[_Mma~axx\tyr)4yF|\x0cr0_2=P:Yz *c"4_]eO6I1OieTAnBLPlksz.$NnjkcW2Ce)m{R'
# print(''.join(na[piton] for piton in love()))

# import math
#
# n = 600851475143
#
# for i in reversed(range(100*100, 999*999)):
#     if str(i) == str(i)[::-1]:
#         for j in range(100, 1000):
#             if i % j == 0 and i // j in range(100, 1000):
#                 print(i, j)
#                 break

# n = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
# r = '123456789'
#
# import operator
# import functools
#
# max = -1
# for i in range(0, len(n)-12):
#     p = functools.reduce(operator.mul, map(int, n[i:i+13]), 1)
#     max = p if p > max else max
#
# print(max)

# for a in range(1, 1000):
#     for b in range(a + 1, 1000):
#         for c in range(b + 1, 1000):
#             if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
#                 print(a, b, c, a * b * c)

# l = []
# for i in range(20):
#      l.extend([list(map(int, input().split(' ')))])
# print(l)

# l = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
#      [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
#      [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
#      [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
#      [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
#      [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
#      [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
#      [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
#      [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
#      [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
#      [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
#      [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
#      [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
#      [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
#      [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
#      [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
#      [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
#      [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
#      [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
#      [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]
#
# max = -1
# # down
# for i in range(17):
#     for j in range(20):
#         p = l[i][j] * l[i + 1][j] * l[i + 2][j] * l[i + 3][j]
#         max = p if p > max else max
#
# # right
# for i in range(20):
#     for j in range(17):
#         p = l[i][j] * l[i][j + 1] * l[i][j + 2] * l[i][j + 3]
#         max = p if p > max else max
#
# # right-down diagonals
# for i in range(17):
#     for j in range(17):
#         p = l[i][j] * l[i + 1][j + 1] * l[i + 2][j + 2] * l[i + 3][j + 3]
#         max = p if p > max else max
#
# # left-down diagonals
# for i in range(17):
#     for j in range(3, 20):
#         p = l[i][j] * l[i + 1][j - 1] * l[i + 2][j - 2] * l[i + 3][j - 3]
#         max = p if p > max else max
#
# print(max)

# import math
# import timeit
#
#
# def count_divisors(num):
#     divs = 0
#     sqrt = math.sqrt(num)
#     for i in range(1, int(sqrt) + 1):
#         if num % i == 0:
#             divs += 2 if i != sqrt else 1
#     return divs
#
# i = 1
# while count_divisors(sum(range(i))) < 500:
#     i += 1
#
# print(sum(range(i)), count_divisors(sum(range(i))), count_divisors(sum(range(i-1))))

# max = (-1, -1)
#
# for i in range(2, 1000000):
#     if i % 10000 == 0:
#         print(i)
#     l = [i]
#     while l[-1] != 1:
#         if l[-1] % 2 == 0:
#             l.append(l[-1] // 2)
#         else:
#             l.append(3*l[-1] + 1)
#     if len(l) > max[0]:
#         max = (len(l), i)
#
# print(max)

# def count_routes(n):
#     n += 1
#     l = [[''] * n for i in range(n)]
#     for x in range(n):
#         for y in range(n):
#             if x == 0 or y == 0:
#                 l[x][y] = 1
#             else:
#                 l[x][y] = l[x-1][y] + l[x][y-1]
#     return l
#
# print(count_routes(20)[-1][-1])

# print(sum([int(c) for c in str(2**1000)]))

# def spell_number(n):
#     values = {0:'', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
#               10: 'ten', 11: 'eleven', 12: 'twelwe', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
#               17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
#               60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'}
#     s = ''
#     r, n = divmod(n, 1000)
#     if r:
#         s += values[r] + values[1000]
#     r, n = divmod(n, 100)
#     if r:
#         s += values[r] + values[100]
#     if n:
#         if s:
#             s += 'and'
#         if n < 21:
#             s += values[n]
#         else:
#             s += values[(n//10)*10] + values[n%10]
#
#     return s
#
# print(spell_number(0))
# print(sum([len(spell_number(n)) for n in range(1001)]))

# with open('p3.txt', 'r') as f:
#     l = [list(map(int, line.split())) for line in f.read().split('\n')]
#
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         right = l[i-1][j] if i and j < len(l[i-1]) else 0
#         left = l[i-1][j-1] if i else 0
#         l[i][j] += max(left, right)
#
# for line in l:
#     print(line)
# print(max(l[-1]))

# from datetime import datetime
#
# sum = 0
#
# for year in range(1901, 2001):
#     for month in range(1, 13):
#         if datetime(year, month, 1).weekday() == 6:
#             sum += 1
#
# print(sum)

# import math
#
# print(sum([int(c) for c in str(math.factorial(100))]))

# import math
#
# def count_divisors(num):
#     divs = 0
#     sqrt = math.sqrt(num)
#     for i in range(1, int(sqrt) + 1):
#         if num % i == 0:
#             divs += i + (num // i) if i != sqrt and i > 1 else i
#     return divs
#
# div_list = [count_divisors(i) for i in range(1, 10000)]
# d = dict(zip(range(1, 10000), div_list))
# sum = 0
#
#
# for i in range(1, 10000):
#     if d.get(d[i], -1) == i and i != d[i]:
#         sum += i
#
# print(sum)

# import string
#
# with open('names.txt') as f:
#     l = f.read()[1:-1].split('","')
#
# abc = string.ascii_uppercase
# l.sort()
#
# print(l.index('COLIN'))
#
# res = 0
# for i in range(len(l)):
#     res += (i+1) * sum([abc.index(c)+1 for c in l[i]])
#
# print(res)

# import math
#
#
# def sum_divisors(num):
#     divs = [1]
#     sqrt = math.sqrt(num)
#     for i in range(2, int(sqrt) + 1):
#         if num % i == 0:
#             divs.append(i)
#             if i != sqrt:
#                 divs.append(num // i)
#     return sum(divs)
#
# l = [i for i in range(1, 28124) if sum_divisors(i) > i]
#
# sums = set()
#
# for i in l:
#     for j in l:
#         sums.add(i+j)
#
# print(len(sums))
#
# print(sum([l for l in range(1, 28124) if l not in sums]))

# from itertools import permutations
#
# print(''.join(list(permutations('0123456789'))[999999]))

# def get_fib_by_length(l):
#     a = 1
#     b = 1
#     i = 3
#     while len(str(a+b)) < l:
#         a, b = b, a+b
#         i += 1
#     return i
#
# print(get_fib_by_length(1000))

# def len_of_period(n):
#     ups = []
#     up = 1
#     while True:
#         if up % n == 0:
#             return -1
#         if up in ups:
#             return len(ups[ups.index(up):])
#         ups.append(up)
#         d = up // n
#         up = (up - d*n) * 10
#
#
#
# m = []
# for i in range(2, 1000):
#     print(i)
#     m.append((len_of_period(i), i))
#
# m.sort(key=lambda x: x[0])
# m.reverse()
# print(m[:20])
#
# print(len_of_period(9))



# import math
#
# list_of_primes = []
# for num in range(2, 1000000):
#     sqrt = math.sqrt(num)
#     for i in range(2, int(sqrt) + 1):
#         if num % i == 0:
#             break
#     else:
#         list_of_primes.append(num)
#
# print('Calculated list of primes')
#
#
# def number_of_primes_in_a_row(a, b):
#     i = 0
#     while (i ** 2 + a * i + b) in list_of_primes:
#         i += 1
#     return i
#
#
# max = -1
# for a in range(-999, 1000):
#     print(a)
#     for b in range(-1000, 1001):
#         m = number_of_primes_in_a_row(a, b)
#         if m > max:
#             max = m
#             print('a: {}, b: {}, max: {}, a * b: {}'.format(a, b, max, a * b))


# def get_sum(n):
#     s = 1
#     for i in range(3, n+1, 2):
#         s += sum(range((i-2)**2, (i**2) + 1, i-1)[1:])
#     return s
#
#
# print(get_sum(1001))

# s = set()
# for a in range(2, 101):
#     for b in range(2, 101):
#         s.add(a**b)
#
# print(len(s))

# def can_be(n, i):
#     return sum([int(c) ** i for c in str(n)]) == n
#
# print(sum([i for i in range(10, 1000000) if can_be(i, 5)]))

# i = 0
# for one in range(201):
#     for two in range(101):
#         for five in range(41):
#             for ten in range(21):
#                 for twenty in range(11):
#                     for fifty in range(5):
#                         for hundred in range(3):
#                             for two_hundred in range(2):
#                                 if one + 2*two + 5*five + 10*ten + 20*twenty + 50*fifty + 100*hundred + 200*two_hundred == 200:
#                                     i += 1
#
# print(i)

# from itertools import permutations
#
# l = list(permutations('123456789'))
#
#
# s = set()
# for p in l:
#     for i in range(1, 8):
#         for j in range(i+1, 9):
#             if int(''.join(p[:i])) * int(''.join(p[i:j])) == int(''.join(p[j:])):
#                 s.add(int(''.join(p[j:])))
#
# print(sum(s))

# def h2s(hours):
#     fradrag = 5659
#
#     netto = hours*179
#
#     return netto*0.92 - (netto*0.92 - fradrag)*0.38 + (6015*0.62 if netto < 12000 else 0)
#
# max_su = h2s(67)
# i = 68
# while h2s(i) < max_su:
#     i += 1
# print(i, h2s(i))

# fu = 1
# fd = 1
#
# for down in range(10, 100):
#     for up in range(10, down):
#         u = set([c for c in str(up)])
#         d = set([c for c in str(down)])
#         common = d & u
#         if len(common) == 1 and common != {'0'}:
#             common = common.pop()
#             u = [c for c in str(up)]
#             u.remove(common)
#             u = int(''.join(u))
#             d = [c for c in str(down)]
#             d.remove(common)
#             d = int(''.join(d))
#             if d != 0 and up/down == u/d:
#                 fu *= up
#                 fd *= down
#                 print('{}/{}  {}/{}'.format(up, down, u, d))
#
# print()
# print('{}/{}'.format(fu, fd))

# import math
#
# s = 0
# for i in range(3, 1000000):
#     if sum([math.factorial(int(c)) for c in str(i)]) == i:
#         s += i
#
# print(s)

# import math
#
#
# list_of_primes = []
# for num in range(2, 1000000):
#     sqrt = math.sqrt(num)
#     for i in range(2, int(sqrt) + 1):
#         if num % i == 0:
#             break
#     else:
#         list_of_primes.append(num)
#
# print('Calculated list of primes')
#
# def prime(n):
#     return n in list_of_primes
#
# def rotations(n):
#     l = []
#     n = str(n)[-1] + str(n)[:-1]
#     for i in range(len(n)-1):
#         l.append(int(n))
#         n = n[-1] + n[:-1]
#     return l

# num = 0
# for i in list_of_primes:
#     if all(prime(r) for r in rotations(i)):
#         print(i)
#         num += 1

# sum = 0
# for i in range(1000000):
#     if str(i) == str(i)[::-1] and "{0:b}".format(i) == "{0:b}".format(i)[::-1]:
#         sum += i
#
# print(sum)

# import math
#
# list_of_primes = []
# for num in range(2, 1000000):
#     sqrt = math.sqrt(num)
#     for i in range(2, int(sqrt) + 1):
#         if num % i == 0:
#             break
#     else:
#         list_of_primes.append(num)
#
# print('Calculated list of primes')
#
# def works(n):
#     l2r = str(n)
#     r2l = str(n)
#     while l2r:
#         if int(l2r) not in list_of_primes or int(r2l) not in list_of_primes:
#             return False
#         l2r = l2r[1:]
#         r2l = r2l[:-1]
#     return True
#
# sum = 0
# for i in range(10, 1000000):
#     if works(i):
#         print(i)
#         sum += i
#
# print(sum)

# def pandigital(n):
#     return '0' not in n and len(n) == len(set(n))
#
#
# def get_value(number):
#     i = 2
#     res = str(number)
#     while True:
#         if len(res) > 9 or not pandigital(res):
#             return -1
#         if len(res) == 9:
#             return int(res)
#         res += str(number * i)
#         i += 1
#
# print(max(get_value(i) for i in range(100000)))

# def num(p):
#     n = 0
#     for a in range(1, p // 2):
#         for b in range(1, p // 2):
#             for c in range(1, p // 2):
#                 if a + b + c == p and a ** 2 + b ** 2 == c ** 2:
#                     n += 1
#     return n // 2
#
# print(num(120))
#
# l = [p for p in [(i, num(i)) for i in range(1000)] if p[1] != 0]
# print(max(l, key=lambda z:z[1]))

# s = ''.join(str(i) for i in range(1000000))
#
# print(int(s[1])*int(s[10])*int(s[100])*int(s[1000])*int(s[10000])*int(s[100000])*int(s[1000000]))

# import math
# from itertools import permutations
#
#
# def is_prime(num):
#     sqrt = math.sqrt(num)
#     for i in range(2, int(sqrt) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# l = [int(''.join(p)) for p in list(permutations('1234567'))[::-1]]
#
# for i in l:
#     if is_prime(i):
#         print(i)
#         break

# words = ["A", "ABILITY", "ABLE", "ABOUT", "ABOVE", "ABSENCE", "ABSOLUTELY", "ACADEMIC", "ACCEPT", "ACCESS", "ACCIDENT",
#          "ACCOMPANY", "ACCORDING", "ACCOUNT", "ACHIEVE", "ACHIEVEMENT", "ACID", "ACQUIRE", "ACROSS", "ACT", "ACTION",
#          "ACTIVE", "ACTIVITY", "ACTUAL", "ACTUALLY", "ADD", "ADDITION", "ADDITIONAL", "ADDRESS", "ADMINISTRATION",
#          "ADMIT", "ADOPT", "ADULT", "ADVANCE", "ADVANTAGE", "ADVICE", "ADVISE", "AFFAIR", "AFFECT", "AFFORD", "AFRAID",
#          "AFTER", "AFTERNOON", "AFTERWARDS", "AGAIN", "AGAINST", "AGE", "AGENCY", "AGENT", "AGO", "AGREE", "AGREEMENT",
#          "AHEAD", "AID", "AIM", "AIR", "AIRCRAFT", "ALL", "ALLOW", "ALMOST", "ALONE", "ALONG", "ALREADY", "ALRIGHT",
#          "ALSO", "ALTERNATIVE", "ALTHOUGH", "ALWAYS", "AMONG", "AMONGST", "AMOUNT", "AN", "ANALYSIS", "ANCIENT", "AND",
#          "ANIMAL", "ANNOUNCE", "ANNUAL", "ANOTHER", "ANSWER", "ANY", "ANYBODY", "ANYONE", "ANYTHING", "ANYWAY", "APART",
#          "APPARENT", "APPARENTLY", "APPEAL", "APPEAR", "APPEARANCE", "APPLICATION", "APPLY", "APPOINT", "APPOINTMENT",
#          "APPROACH", "APPROPRIATE", "APPROVE", "AREA", "ARGUE", "ARGUMENT", "ARISE", "ARM", "ARMY", "AROUND", "ARRANGE",
#          "ARRANGEMENT", "ARRIVE", "ART", "ARTICLE", "ARTIST", "AS", "ASK", "ASPECT", "ASSEMBLY", "ASSESS", "ASSESSMENT",
#          "ASSET", "ASSOCIATE", "ASSOCIATION", "ASSUME", "ASSUMPTION", "AT", "ATMOSPHERE", "ATTACH", "ATTACK", "ATTEMPT",
#          "ATTEND", "ATTENTION", "ATTITUDE", "ATTRACT", "ATTRACTIVE", "AUDIENCE", "AUTHOR", "AUTHORITY", "AVAILABLE",
#          "AVERAGE", "AVOID", "AWARD", "AWARE", "AWAY", "AYE", "BABY", "BACK", "BACKGROUND", "BAD", "BAG", "BALANCE",
#          "BALL", "BAND", "BANK", "BAR", "BASE", "BASIC", "BASIS", "BATTLE", "BE", "BEAR", "BEAT", "BEAUTIFUL",
#          "BECAUSE", "BECOME", "BED", "BEDROOM", "BEFORE", "BEGIN", "BEGINNING", "BEHAVIOUR", "BEHIND", "BELIEF",
#          "BELIEVE", "BELONG", "BELOW", "BENEATH", "BENEFIT", "BESIDE", "BEST", "BETTER", "BETWEEN", "BEYOND", "BIG",
#          "BILL", "BIND", "BIRD", "BIRTH", "BIT", "BLACK", "BLOCK", "BLOOD", "BLOODY", "BLOW", "BLUE", "BOARD", "BOAT",
#          "BODY", "BONE", "BOOK", "BORDER", "BOTH", "BOTTLE", "BOTTOM", "BOX", "BOY", "BRAIN", "BRANCH", "BREAK",
#          "BREATH", "BRIDGE", "BRIEF", "BRIGHT", "BRING", "BROAD", "BROTHER", "BUDGET", "BUILD", "BUILDING", "BURN",
#          "BUS", "BUSINESS", "BUSY", "BUT", "BUY", "BY", "CABINET", "CALL", "CAMPAIGN", "CAN", "CANDIDATE", "CAPABLE",
#          "CAPACITY", "CAPITAL", "CAR", "CARD", "CARE", "CAREER", "CAREFUL", "CAREFULLY", "CARRY", "CASE", "CASH", "CAT",
#          "CATCH", "CATEGORY", "CAUSE", "CELL", "CENTRAL", "CENTRE", "CENTURY", "CERTAIN", "CERTAINLY", "CHAIN", "CHAIR",
#          "CHAIRMAN", "CHALLENGE", "CHANCE", "CHANGE", "CHANNEL", "CHAPTER", "CHARACTER", "CHARACTERISTIC", "CHARGE",
#          "CHEAP", "CHECK", "CHEMICAL", "CHIEF", "CHILD", "CHOICE", "CHOOSE", "CHURCH", "CIRCLE", "CIRCUMSTANCE",
#          "CITIZEN", "CITY", "CIVIL", "CLAIM", "CLASS", "CLEAN", "CLEAR", "CLEARLY", "CLIENT", "CLIMB", "CLOSE",
#          "CLOSELY", "CLOTHES", "CLUB", "COAL", "CODE", "COFFEE", "COLD", "COLLEAGUE", "COLLECT", "COLLECTION",
#          "COLLEGE", "COLOUR", "COMBINATION", "COMBINE", "COME", "COMMENT", "COMMERCIAL", "COMMISSION", "COMMIT",
#          "COMMITMENT", "COMMITTEE", "COMMON", "COMMUNICATION", "COMMUNITY", "COMPANY", "COMPARE", "COMPARISON",
#          "COMPETITION", "COMPLETE", "COMPLETELY", "COMPLEX", "COMPONENT", "COMPUTER", "CONCENTRATE", "CONCENTRATION",
#          "CONCEPT", "CONCERN", "CONCERNED", "CONCLUDE", "CONCLUSION", "CONDITION", "CONDUCT", "CONFERENCE",
#          "CONFIDENCE", "CONFIRM", "CONFLICT", "CONGRESS", "CONNECT", "CONNECTION", "CONSEQUENCE", "CONSERVATIVE",
#          "CONSIDER", "CONSIDERABLE", "CONSIDERATION", "CONSIST", "CONSTANT", "CONSTRUCTION", "CONSUMER", "CONTACT",
#          "CONTAIN", "CONTENT", "CONTEXT", "CONTINUE", "CONTRACT", "CONTRAST", "CONTRIBUTE", "CONTRIBUTION", "CONTROL",
#          "CONVENTION", "CONVERSATION", "COPY", "CORNER", "CORPORATE", "CORRECT", "COS", "COST", "COULD", "COUNCIL",
#          "COUNT", "COUNTRY", "COUNTY", "COUPLE", "COURSE", "COURT", "COVER", "CREATE", "CREATION", "CREDIT", "CRIME",
#          "CRIMINAL", "CRISIS", "CRITERION", "CRITICAL", "CRITICISM", "CROSS", "CROWD", "CRY", "CULTURAL", "CULTURE",
#          "CUP", "CURRENT", "CURRENTLY", "CURRICULUM", "CUSTOMER", "CUT", "DAMAGE", "DANGER", "DANGEROUS", "DARK",
#          "DATA", "DATE", "DAUGHTER", "DAY", "DEAD", "DEAL", "DEATH", "DEBATE", "DEBT", "DECADE", "DECIDE", "DECISION",
#          "DECLARE", "DEEP", "DEFENCE", "DEFENDANT", "DEFINE", "DEFINITION", "DEGREE", "DELIVER", "DEMAND", "DEMOCRATIC",
#          "DEMONSTRATE", "DENY", "DEPARTMENT", "DEPEND", "DEPUTY", "DERIVE", "DESCRIBE", "DESCRIPTION", "DESIGN",
#          "DESIRE", "DESK", "DESPITE", "DESTROY", "DETAIL", "DETAILED", "DETERMINE", "DEVELOP", "DEVELOPMENT", "DEVICE",
#          "DIE", "DIFFERENCE", "DIFFERENT", "DIFFICULT", "DIFFICULTY", "DINNER", "DIRECT", "DIRECTION", "DIRECTLY",
#          "DIRECTOR", "DISAPPEAR", "DISCIPLINE", "DISCOVER", "DISCUSS", "DISCUSSION", "DISEASE", "DISPLAY", "DISTANCE",
#          "DISTINCTION", "DISTRIBUTION", "DISTRICT", "DIVIDE", "DIVISION", "DO", "DOCTOR", "DOCUMENT", "DOG", "DOMESTIC",
#          "DOOR", "DOUBLE", "DOUBT", "DOWN", "DRAW", "DRAWING", "DREAM", "DRESS", "DRINK", "DRIVE", "DRIVER", "DROP",
#          "DRUG", "DRY", "DUE", "DURING", "DUTY", "EACH", "EAR", "EARLY", "EARN", "EARTH", "EASILY", "EAST", "EASY",
#          "EAT", "ECONOMIC", "ECONOMY", "EDGE", "EDITOR", "EDUCATION", "EDUCATIONAL", "EFFECT", "EFFECTIVE",
#          "EFFECTIVELY", "EFFORT", "EGG", "EITHER", "ELDERLY", "ELECTION", "ELEMENT", "ELSE", "ELSEWHERE", "EMERGE",
#          "EMPHASIS", "EMPLOY", "EMPLOYEE", "EMPLOYER", "EMPLOYMENT", "EMPTY", "ENABLE", "ENCOURAGE", "END", "ENEMY",
#          "ENERGY", "ENGINE", "ENGINEERING", "ENJOY", "ENOUGH", "ENSURE", "ENTER", "ENTERPRISE", "ENTIRE", "ENTIRELY",
#          "ENTITLE", "ENTRY", "ENVIRONMENT", "ENVIRONMENTAL", "EQUAL", "EQUALLY", "EQUIPMENT", "ERROR", "ESCAPE",
#          "ESPECIALLY", "ESSENTIAL", "ESTABLISH", "ESTABLISHMENT", "ESTATE", "ESTIMATE", "EVEN", "EVENING", "EVENT",
#          "EVENTUALLY", "EVER", "EVERY", "EVERYBODY", "EVERYONE", "EVERYTHING", "EVIDENCE", "EXACTLY", "EXAMINATION",
#          "EXAMINE", "EXAMPLE", "EXCELLENT", "EXCEPT", "EXCHANGE", "EXECUTIVE", "EXERCISE", "EXHIBITION", "EXIST",
#          "EXISTENCE", "EXISTING", "EXPECT", "EXPECTATION", "EXPENDITURE", "EXPENSE", "EXPENSIVE", "EXPERIENCE",
#          "EXPERIMENT", "EXPERT", "EXPLAIN", "EXPLANATION", "EXPLORE", "EXPRESS", "EXPRESSION", "EXTEND", "EXTENT",
#          "EXTERNAL", "EXTRA", "EXTREMELY", "EYE", "FACE", "FACILITY", "FACT", "FACTOR", "FACTORY", "FAIL", "FAILURE",
#          "FAIR", "FAIRLY", "FAITH", "FALL", "FAMILIAR", "FAMILY", "FAMOUS", "FAR", "FARM", "FARMER", "FASHION", "FAST",
#          "FATHER", "FAVOUR", "FEAR", "FEATURE", "FEE", "FEEL", "FEELING", "FEMALE", "FEW", "FIELD", "FIGHT", "FIGURE",
#          "FILE", "FILL", "FILM", "FINAL", "FINALLY", "FINANCE", "FINANCIAL", "FIND", "FINDING", "FINE", "FINGER",
#          "FINISH", "FIRE", "FIRM", "FIRST", "FISH", "FIT", "FIX", "FLAT", "FLIGHT", "FLOOR", "FLOW", "FLOWER", "FLY",
#          "FOCUS", "FOLLOW", "FOLLOWING", "FOOD", "FOOT", "FOOTBALL", "FOR", "FORCE", "FOREIGN", "FOREST", "FORGET",
#          "FORM", "FORMAL", "FORMER", "FORWARD", "FOUNDATION", "FREE", "FREEDOM", "FREQUENTLY", "FRESH", "FRIEND",
#          "FROM", "FRONT", "FRUIT", "FUEL", "FULL", "FULLY", "FUNCTION", "FUND", "FUNNY", "FURTHER", "FUTURE", "GAIN",
#          "GAME", "GARDEN", "GAS", "GATE", "GATHER", "GENERAL", "GENERALLY", "GENERATE", "GENERATION", "GENTLEMAN",
#          "GET", "GIRL", "GIVE", "GLASS", "GO", "GOAL", "GOD", "GOLD", "GOOD", "GOVERNMENT", "GRANT", "GREAT", "GREEN",
#          "GREY", "GROUND", "GROUP", "GROW", "GROWING", "GROWTH", "GUEST", "GUIDE", "GUN", "HAIR", "HALF", "HALL",
#          "HAND", "HANDLE", "HANG", "HAPPEN", "HAPPY", "HARD", "HARDLY", "HATE", "HAVE", "HE", "HEAD", "HEALTH", "HEAR",
#          "HEART", "HEAT", "HEAVY", "HELL", "HELP", "HENCE", "HER", "HERE", "HERSELF", "HIDE", "HIGH", "HIGHLY", "HILL",
#          "HIM", "HIMSELF", "HIS", "HISTORICAL", "HISTORY", "HIT", "HOLD", "HOLE", "HOLIDAY", "HOME", "HOPE", "HORSE",
#          "HOSPITAL", "HOT", "HOTEL", "HOUR", "HOUSE", "HOUSEHOLD", "HOUSING", "HOW", "HOWEVER", "HUGE", "HUMAN", "HURT",
#          "HUSBAND", "I", "IDEA", "IDENTIFY", "IF", "IGNORE", "ILLUSTRATE", "IMAGE", "IMAGINE", "IMMEDIATE",
#          "IMMEDIATELY", "IMPACT", "IMPLICATION", "IMPLY", "IMPORTANCE", "IMPORTANT", "IMPOSE", "IMPOSSIBLE",
#          "IMPRESSION", "IMPROVE", "IMPROVEMENT", "IN", "INCIDENT", "INCLUDE", "INCLUDING", "INCOME", "INCREASE",
#          "INCREASED", "INCREASINGLY", "INDEED", "INDEPENDENT", "INDEX", "INDICATE", "INDIVIDUAL", "INDUSTRIAL",
#          "INDUSTRY", "INFLUENCE", "INFORM", "INFORMATION", "INITIAL", "INITIATIVE", "INJURY", "INSIDE", "INSIST",
#          "INSTANCE", "INSTEAD", "INSTITUTE", "INSTITUTION", "INSTRUCTION", "INSTRUMENT", "INSURANCE", "INTEND",
#          "INTENTION", "INTEREST", "INTERESTED", "INTERESTING", "INTERNAL", "INTERNATIONAL", "INTERPRETATION",
#          "INTERVIEW", "INTO", "INTRODUCE", "INTRODUCTION", "INVESTIGATE", "INVESTIGATION", "INVESTMENT", "INVITE",
#          "INVOLVE", "IRON", "IS", "ISLAND", "ISSUE", "IT", "ITEM", "ITS", "ITSELF", "JOB", "JOIN", "JOINT", "JOURNEY",
#          "JUDGE", "JUMP", "JUST", "JUSTICE", "KEEP", "KEY", "KID", "KILL", "KIND", "KING", "KITCHEN", "KNEE", "KNOW",
#          "KNOWLEDGE", "LABOUR", "LACK", "LADY", "LAND", "LANGUAGE", "LARGE", "LARGELY", "LAST", "LATE", "LATER",
#          "LATTER", "LAUGH", "LAUNCH", "LAW", "LAWYER", "LAY", "LEAD", "LEADER", "LEADERSHIP", "LEADING", "LEAF",
#          "LEAGUE", "LEAN", "LEARN", "LEAST", "LEAVE", "LEFT", "LEG", "LEGAL", "LEGISLATION", "LENGTH", "LESS", "LET",
#          "LETTER", "LEVEL", "LIABILITY", "LIBERAL", "LIBRARY", "LIE", "LIFE", "LIFT", "LIGHT", "LIKE", "LIKELY",
#          "LIMIT", "LIMITED", "LINE", "LINK", "LIP", "LIST", "LISTEN", "LITERATURE", "LITTLE", "LIVE", "LIVING", "LOAN",
#          "LOCAL", "LOCATION", "LONG", "LOOK", "LORD", "LOSE", "LOSS", "LOT", "LOVE", "LOVELY", "LOW", "LUNCH",
#          "MACHINE", "MAGAZINE", "MAIN", "MAINLY", "MAINTAIN", "MAJOR", "MAJORITY", "MAKE", "MALE", "MAN", "MANAGE",
#          "MANAGEMENT", "MANAGER", "MANNER", "MANY", "MAP", "MARK", "MARKET", "MARRIAGE", "MARRIED", "MARRY", "MASS",
#          "MASTER", "MATCH", "MATERIAL", "MATTER", "MAY", "MAYBE", "ME", "MEAL", "MEAN", "MEANING", "MEANS", "MEANWHILE",
#          "MEASURE", "MECHANISM", "MEDIA", "MEDICAL", "MEET", "MEETING", "MEMBER", "MEMBERSHIP", "MEMORY", "MENTAL",
#          "MENTION", "MERELY", "MESSAGE", "METAL", "METHOD", "MIDDLE", "MIGHT", "MILE", "MILITARY", "MILK", "MIND",
#          "MINE", "MINISTER", "MINISTRY", "MINUTE", "MISS", "MISTAKE", "MODEL", "MODERN", "MODULE", "MOMENT", "MONEY",
#          "MONTH", "MORE", "MORNING", "MOST", "MOTHER", "MOTION", "MOTOR", "MOUNTAIN", "MOUTH", "MOVE", "MOVEMENT",
#          "MUCH", "MURDER", "MUSEUM", "MUSIC", "MUST", "MY", "MYSELF", "NAME", "NARROW", "NATION", "NATIONAL", "NATURAL",
#          "NATURE", "NEAR", "NEARLY", "NECESSARILY", "NECESSARY", "NECK", "NEED", "NEGOTIATION", "NEIGHBOUR", "NEITHER",
#          "NETWORK", "NEVER", "NEVERTHELESS", "NEW", "NEWS", "NEWSPAPER", "NEXT", "NICE", "NIGHT", "NO", "NOBODY", "NOD",
#          "NOISE", "NONE", "NOR", "NORMAL", "NORMALLY", "NORTH", "NORTHERN", "NOSE", "NOT", "NOTE", "NOTHING", "NOTICE",
#          "NOTION", "NOW", "NUCLEAR", "NUMBER", "NURSE", "OBJECT", "OBJECTIVE", "OBSERVATION", "OBSERVE", "OBTAIN",
#          "OBVIOUS", "OBVIOUSLY", "OCCASION", "OCCUR", "ODD", "OF", "OFF", "OFFENCE", "OFFER", "OFFICE", "OFFICER",
#          "OFFICIAL", "OFTEN", "OIL", "OKAY", "OLD", "ON", "ONCE", "ONE", "ONLY", "ONTO", "OPEN", "OPERATE", "OPERATION",
#          "OPINION", "OPPORTUNITY", "OPPOSITION", "OPTION", "OR", "ORDER", "ORDINARY", "ORGANISATION", "ORGANISE",
#          "ORGANIZATION", "ORIGIN", "ORIGINAL", "OTHER", "OTHERWISE", "OUGHT", "OUR", "OURSELVES", "OUT", "OUTCOME",
#          "OUTPUT", "OUTSIDE", "OVER", "OVERALL", "OWN", "OWNER", "PACKAGE", "PAGE", "PAIN", "PAINT", "PAINTING", "PAIR",
#          "PANEL", "PAPER", "PARENT", "PARK", "PARLIAMENT", "PART", "PARTICULAR", "PARTICULARLY", "PARTLY", "PARTNER",
#          "PARTY", "PASS", "PASSAGE", "PAST", "PATH", "PATIENT", "PATTERN", "PAY", "PAYMENT", "PEACE", "PENSION",
#          "PEOPLE", "PER", "PERCENT", "PERFECT", "PERFORM", "PERFORMANCE", "PERHAPS", "PERIOD", "PERMANENT", "PERSON",
#          "PERSONAL", "PERSUADE", "PHASE", "PHONE", "PHOTOGRAPH", "PHYSICAL", "PICK", "PICTURE", "PIECE", "PLACE",
#          "PLAN", "PLANNING", "PLANT", "PLASTIC", "PLATE", "PLAY", "PLAYER", "PLEASE", "PLEASURE", "PLENTY", "PLUS",
#          "POCKET", "POINT", "POLICE", "POLICY", "POLITICAL", "POLITICS", "POOL", "POOR", "POPULAR", "POPULATION",
#          "POSITION", "POSITIVE", "POSSIBILITY", "POSSIBLE", "POSSIBLY", "POST", "POTENTIAL", "POUND", "POWER",
#          "POWERFUL", "PRACTICAL", "PRACTICE", "PREFER", "PREPARE", "PRESENCE", "PRESENT", "PRESIDENT", "PRESS",
#          "PRESSURE", "PRETTY", "PREVENT", "PREVIOUS", "PREVIOUSLY", "PRICE", "PRIMARY", "PRIME", "PRINCIPLE",
#          "PRIORITY", "PRISON", "PRISONER", "PRIVATE", "PROBABLY", "PROBLEM", "PROCEDURE", "PROCESS", "PRODUCE",
#          "PRODUCT", "PRODUCTION", "PROFESSIONAL", "PROFIT", "PROGRAM", "PROGRAMME", "PROGRESS", "PROJECT", "PROMISE",
#          "PROMOTE", "PROPER", "PROPERLY", "PROPERTY", "PROPORTION", "PROPOSE", "PROPOSAL", "PROSPECT", "PROTECT",
#          "PROTECTION", "PROVE", "PROVIDE", "PROVIDED", "PROVISION", "PUB", "PUBLIC", "PUBLICATION", "PUBLISH", "PULL",
#          "PUPIL", "PURPOSE", "PUSH", "PUT", "QUALITY", "QUARTER", "QUESTION", "QUICK", "QUICKLY", "QUIET", "QUITE",
#          "RACE", "RADIO", "RAILWAY", "RAIN", "RAISE", "RANGE", "RAPIDLY", "RARE", "RATE", "RATHER", "REACH", "REACTION",
#          "READ", "READER", "READING", "READY", "REAL", "REALISE", "REALITY", "REALIZE", "REALLY", "REASON",
#          "REASONABLE", "RECALL", "RECEIVE", "RECENT", "RECENTLY", "RECOGNISE", "RECOGNITION", "RECOGNIZE", "RECOMMEND",
#          "RECORD", "RECOVER", "RED", "REDUCE", "REDUCTION", "REFER", "REFERENCE", "REFLECT", "REFORM", "REFUSE",
#          "REGARD", "REGION", "REGIONAL", "REGULAR", "REGULATION", "REJECT", "RELATE", "RELATION", "RELATIONSHIP",
#          "RELATIVE", "RELATIVELY", "RELEASE", "RELEVANT", "RELIEF", "RELIGION", "RELIGIOUS", "RELY", "REMAIN",
#          "REMEMBER", "REMIND", "REMOVE", "REPEAT", "REPLACE", "REPLY", "REPORT", "REPRESENT", "REPRESENTATION",
#          "REPRESENTATIVE", "REQUEST", "REQUIRE", "REQUIREMENT", "RESEARCH", "RESOURCE", "RESPECT", "RESPOND",
#          "RESPONSE", "RESPONSIBILITY", "RESPONSIBLE", "REST", "RESTAURANT", "RESULT", "RETAIN", "RETURN", "REVEAL",
#          "REVENUE", "REVIEW", "REVOLUTION", "RICH", "RIDE", "RIGHT", "RING", "RISE", "RISK", "RIVER", "ROAD", "ROCK",
#          "ROLE", "ROLL", "ROOF", "ROOM", "ROUND", "ROUTE", "ROW", "ROYAL", "RULE", "RUN", "RURAL", "SAFE", "SAFETY",
#          "SALE", "SAME", "SAMPLE", "SATISFY", "SAVE", "SAY", "SCALE", "SCENE", "SCHEME", "SCHOOL", "SCIENCE",
#          "SCIENTIFIC", "SCIENTIST", "SCORE", "SCREEN", "SEA", "SEARCH", "SEASON", "SEAT", "SECOND", "SECONDARY",
#          "SECRETARY", "SECTION", "SECTOR", "SECURE", "SECURITY", "SEE", "SEEK", "SEEM", "SELECT", "SELECTION", "SELL",
#          "SEND", "SENIOR", "SENSE", "SENTENCE", "SEPARATE", "SEQUENCE", "SERIES", "SERIOUS", "SERIOUSLY", "SERVANT",
#          "SERVE", "SERVICE", "SESSION", "SET", "SETTLE", "SETTLEMENT", "SEVERAL", "SEVERE", "SEX", "SEXUAL", "SHAKE",
#          "SHALL", "SHAPE", "SHARE", "SHE", "SHEET", "SHIP", "SHOE", "SHOOT", "SHOP", "SHORT", "SHOT", "SHOULD",
#          "SHOULDER", "SHOUT", "SHOW", "SHUT", "SIDE", "SIGHT", "SIGN", "SIGNAL", "SIGNIFICANCE", "SIGNIFICANT",
#          "SILENCE", "SIMILAR", "SIMPLE", "SIMPLY", "SINCE", "SING", "SINGLE", "SIR", "SISTER", "SIT", "SITE",
#          "SITUATION", "SIZE", "SKILL", "SKIN", "SKY", "SLEEP", "SLIGHTLY", "SLIP", "SLOW", "SLOWLY", "SMALL", "SMILE",
#          "SO", "SOCIAL", "SOCIETY", "SOFT", "SOFTWARE", "SOIL", "SOLDIER", "SOLICITOR", "SOLUTION", "SOME", "SOMEBODY",
#          "SOMEONE", "SOMETHING", "SOMETIMES", "SOMEWHAT", "SOMEWHERE", "SON", "SONG", "SOON", "SORRY", "SORT", "SOUND",
#          "SOURCE", "SOUTH", "SOUTHERN", "SPACE", "SPEAK", "SPEAKER", "SPECIAL", "SPECIES", "SPECIFIC", "SPEECH",
#          "SPEED", "SPEND", "SPIRIT", "SPORT", "SPOT", "SPREAD", "SPRING", "STAFF", "STAGE", "STAND", "STANDARD", "STAR",
#          "START", "STATE", "STATEMENT", "STATION", "STATUS", "STAY", "STEAL", "STEP", "STICK", "STILL", "STOCK",
#          "STONE", "STOP", "STORE", "STORY", "STRAIGHT", "STRANGE", "STRATEGY", "STREET", "STRENGTH", "STRIKE", "STRONG",
#          "STRONGLY", "STRUCTURE", "STUDENT", "STUDIO", "STUDY", "STUFF", "STYLE", "SUBJECT", "SUBSTANTIAL", "SUCCEED",
#          "SUCCESS", "SUCCESSFUL", "SUCH", "SUDDENLY", "SUFFER", "SUFFICIENT", "SUGGEST", "SUGGESTION", "SUITABLE",
#          "SUM", "SUMMER", "SUN", "SUPPLY", "SUPPORT", "SUPPOSE", "SURE", "SURELY", "SURFACE", "SURPRISE", "SURROUND",
#          "SURVEY", "SURVIVE", "SWITCH", "SYSTEM", "TABLE", "TAKE", "TALK", "TALL", "TAPE", "TARGET", "TASK", "TAX",
#          "TEA", "TEACH", "TEACHER", "TEACHING", "TEAM", "TEAR", "TECHNICAL", "TECHNIQUE", "TECHNOLOGY", "TELEPHONE",
#          "TELEVISION", "TELL", "TEMPERATURE", "TEND", "TERM", "TERMS", "TERRIBLE", "TEST", "TEXT", "THAN", "THANK",
#          "THANKS", "THAT", "THE", "THEATRE", "THEIR", "THEM", "THEME", "THEMSELVES", "THEN", "THEORY", "THERE",
#          "THEREFORE", "THESE", "THEY", "THIN", "THING", "THINK", "THIS", "THOSE", "THOUGH", "THOUGHT", "THREAT",
#          "THREATEN", "THROUGH", "THROUGHOUT", "THROW", "THUS", "TICKET", "TIME", "TINY", "TITLE", "TO", "TODAY",
#          "TOGETHER", "TOMORROW", "TONE", "TONIGHT", "TOO", "TOOL", "TOOTH", "TOP", "TOTAL", "TOTALLY", "TOUCH", "TOUR",
#          "TOWARDS", "TOWN", "TRACK", "TRADE", "TRADITION", "TRADITIONAL", "TRAFFIC", "TRAIN", "TRAINING", "TRANSFER",
#          "TRANSPORT", "TRAVEL", "TREAT", "TREATMENT", "TREATY", "TREE", "TREND", "TRIAL", "TRIP", "TROOP", "TROUBLE",
#          "TRUE", "TRUST", "TRUTH", "TRY", "TURN", "TWICE", "TYPE", "TYPICAL", "UNABLE", "UNDER", "UNDERSTAND",
#          "UNDERSTANDING", "UNDERTAKE", "UNEMPLOYMENT", "UNFORTUNATELY", "UNION", "UNIT", "UNITED", "UNIVERSITY",
#          "UNLESS", "UNLIKELY", "UNTIL", "UP", "UPON", "UPPER", "URBAN", "US", "USE", "USED", "USEFUL", "USER", "USUAL",
#          "USUALLY", "VALUE", "VARIATION", "VARIETY", "VARIOUS", "VARY", "VAST", "VEHICLE", "VERSION", "VERY", "VIA",
#          "VICTIM", "VICTORY", "VIDEO", "VIEW", "VILLAGE", "VIOLENCE", "VISION", "VISIT", "VISITOR", "VITAL", "VOICE",
#          "VOLUME", "VOTE", "WAGE", "WAIT", "WALK", "WALL", "WANT", "WAR", "WARM", "WARN", "WASH", "WATCH", "WATER",
#          "WAVE", "WAY", "WE", "WEAK", "WEAPON", "WEAR", "WEATHER", "WEEK", "WEEKEND", "WEIGHT", "WELCOME", "WELFARE",
#          "WELL", "WEST", "WESTERN", "WHAT", "WHATEVER", "WHEN", "WHERE", "WHEREAS", "WHETHER", "WHICH", "WHILE",
#          "WHILST", "WHITE", "WHO", "WHOLE", "WHOM", "WHOSE", "WHY", "WIDE", "WIDELY", "WIFE", "WILD", "WILL", "WIN",
#          "WIND", "WINDOW", "WINE", "WING", "WINNER", "WINTER", "WISH", "WITH", "WITHDRAW", "WITHIN", "WITHOUT", "WOMAN",
#          "WONDER", "WONDERFUL", "WOOD", "WORD", "WORK", "WORKER", "WORKING", "WORKS", "WORLD", "WORRY", "WORTH",
#          "WOULD", "WRITE", "WRITER", "WRITING", "WRONG", "YARD", "YEAH", "YEAR", "YES", "YESTERDAY", "YET", "YOU",
#          "YOUNG", "YOUR", "YOURSELF", "YOUTH"]
#
# import string
#
# triangles = [i*(i+1)//2 for i in range(1, 1000)]
#
# def is_triangle_word(word):
#    return sum(string.ascii_uppercase.index(w)+1 for w in word) in triangles
#
# print(len(list(filter(is_triangle_word, words))))

# import math
#
# th = 1000000
#
# list_of_primes = set()
# for num in range(2, th):
#    sqrt = math.sqrt(num)
#    for i in range(2, int(sqrt) + 1):
#        if num % i == 0:
#            break
#    else:
#        list_of_primes.add(num)
#
# print('Calculated list of primes')
#
# def list_divisors(num):
#    divs = set()
#    sqrt = math.sqrt(num)
#    for i in range(2, int(sqrt) + 1):
#        if num % i == 0:
#            divs.add(i)
#            divs.add(num // i)
#    return divs
#
# def solve(n):
#    i = 4
#    while i < th:
#        divs = list_divisors(i)
#        if len(divs & list_of_primes) == n:
#            for j in range(i+1, i+n):
#                if not len(list_divisors(j) & list_of_primes) == n:
#                    break
#            else:
#                return i
#        i += 1
#
# print(solve(4))

# print(str(sum(i**i for i in range(1, 1001)))[-10:])

# import math
# from itertools import combinations
#
# list_of_primes = []
# for num in range(1000, 10000):
#   sqrt = math.sqrt(num)
#   for i in range(2, int(sqrt) + 1):
#       if num % i == 0:
#           break
#   else:
#       list_of_primes.append(num)

# print(list(filter(lambda x : set(str(x[0])) == set(str(x[1])) and set(str(x[0])) == set(str(x[2])) and x[2] - x[1] == x[1] - x[0], combinations(list_of_primes, 3))))


# list_of_primes = get_primes_on_interval(1, 1000000)
# print('Calculated list of primes, length = {}'.format(len(list_of_primes)))
#
#
# def check(i, j):
#    c = 0
#    num = list_of_primes[i]
#    while num > 0:
#        num -= list_of_primes[j]
#        c += 1
#        j -= 1
#    if num == 0:
#        return (list_of_primes[i], c)
#
#
# l = []
# for i in reversed(range(1, len(list_of_primes))):
#    if i % 100 == 0:
#        print(i)
#    for j in reversed(range(1, i)):
#        n = check(i, j)
#        if n:
#            l.append(n)
#
# print(sorted(l, key=lambda x: x[1])[::-1])


# s = 0
# set1 = {1}
# set89 = {89}
# for i in range(2, 10000000):
#    my_set = set()
#    n = i
#    while True:
#        my_set.add(n)
#        if n in set1:
#            set1.update(my_set)
#            break
#        if n in set89:
#            set89.update(my_set)
#            s += 1
#            break
#        n = sum(int(c)**2 for c in str(n))
# print(s)

# from fractions import Fraction
# seq = [2] + [el for lst in [(1, 2*i, 1) for i in range(1, 35)] for el in lst]
#
# def calculate(l):
#    if len(l) == 1:
#        return l[0]
#    return l[0] + Fraction(1, calculate(l[1:]))

# n = Fraction(str(calculate(seq[:100]))).numerator
#
# print(n, sum(int(c) for c in str(n)))

# import roman
# import string
#
# nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#
# def fromRoman(s):
#    i = 0
#    num = 0
#    while i < len(s):
#        if i == len(s) - 1:
#            num += nums[s[i]]
#        elif nums[s[i]] < nums[s[i+1]]:
#            num += nums[s[i+1]] - nums[s[i]]
#            i += 1
#        else:
#            num += nums[s[i]]
#        i += 1
#    return num
#
# sum = 0
# with open('names.txt') as f:
#    for l in f.readlines():
#        l = l.rstrip()
#        sum += len(l) - len(roman.toRoman(fromRoman(l)))
#
# print(sum)

# import itertools
# import functools
#
# primes = get_primes_on_interval(0, 1000000)
#
#
# def max_family(number):
#     def repl(number, digits, n):
#         i = int(''.join([str(number)[i] if i not in digits else str(n) for i in range(len(str(number)))]))
#         if len(str(i)) == len(str(number)) and i in primes:
#             return i
#         return 0
#
#     return [[repl(number, digits, i) for i in range(10)] for j in range(1, len(str(number))) for digits in itertools.combinations(range(len(str(number))), j)]
#
#
# for i in primes[11320:]:
#     m = max_family(i)
#     print(i)
#     b = False
#     for mm in m:
#         mmm = list(filter(lambda x: x, mm))
#         if len(mmm) >= 8:
#             b = True
#             ans = min(mmm)
#     if b:
#         print('----->', ans)
#         break
