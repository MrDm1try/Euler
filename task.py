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


# def num_to_digits(n):
#     return sorted([c for c in str(n)])
#
#
# i = 1
# p = num_to_digits(i)
# while p != num_to_digits(i*2)\
#         or p != num_to_digits(i*3)\
#         or p != num_to_digits(i*4)\
#         or p != num_to_digits(i*5)\
#         or p != num_to_digits(i*6):
#     i += 1
#     p = num_to_digits(i)
#
# print(i)

# def nCr(n,r):
#     f = math.factorial
#     return f(n) // f(r) // f(n-r)
#
# i = 0
# for n in range(1, 101):
#     for r in range(1, n):
#         if nCr(n, r) > 1000000:
#             i += 1
#
# print(i)


# class Card:
#     def __init__(self, card):
#         card_num = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
#         self.value = card_num[card[0]] if card[0] in card_num else int(card[0])
#         self.suit = card[1]
#
#     def __repr__(self):
#         values = {2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eught', 9: 'Nine', 10: 'Ten',
#                   11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
#         suits = {'H': 'Hearts', 'S': 'Spades', 'D': 'Diamonds', 'C': 'Clubs'}
#         return '{} of {}'.format(values[self.value], suits[self.suit])
#
#     def __lt__(self, other):
#         return self.value < other.value
#
#     def __gt__(self, other):
#         return self.value > other.value
#
#
# class Hand:
#     def __init__(self, ls):
#         self.cards = sorted([Card(c) for c in ls], reverse=True)
#
#     def _flush(self):
#         return self.cards[0].suit == self.cards[1].suit == self.cards[2].suit == \
#                self.cards[3].suit == self.cards[4].suit
#
#     def _straight(self):
#         return self.cards[0].value == self.cards[1].value + 1 == self.cards[2].value + 2 == \
#                self.cards[3].value + 3 == self.cards[4].value + 4
#
#     def get_hand(self):
#         # check straight/royal flush
#         if self._straight() and self._flush():
#             return [8, self.cards[0].value]
#
#         # check four of a kind
#         if self.cards[0].value == self.cards[1].value == self.cards[2].value == self.cards[3].value:
#             return [7, self.cards[0].value]
#         if self.cards[1].value == self.cards[2].value == self.cards[3].value == self.cards[4].value:
#             return [7, self.cards[1].value]
#
#         # check full house
#         if self.cards[0].value == self.cards[1].value == self.cards[2].value and \
#                         self.cards[3].value == self.cards[4].value:
#             return [6, self.cards[0].value]
#         if self.cards[0].value == self.cards[1].value and \
#                                 self.cards[2].value == self.cards[3].value == self.cards[4].value:
#             return [6, self.cards[2].value]
#
#         # check flush
#         if self._flush():
#             return [5] + [c.value for c in self.cards]
#
#         # check straight
#         if self._straight():
#             return [4, self.cards[0].value]
#
#         # check three of a kind
#         if self.cards[0].value == self.cards[1].value == self.cards[2].value:
#             return [3, self.cards[0].value]
#         if self.cards[1].value == self.cards[2].value == self.cards[3].value:
#             return [3, self.cards[1].value]
#         if self.cards[2].value == self.cards[3].value == self.cards[4].value:
#             return [3, self.cards[2].value]
#
#         # check two pairs
#         if self.cards[0].value == self.cards[1].value and self.cards[2].value == self.cards[3].value:
#             return [2, self.cards[0].value, self.cards[2].value, self.cards[4].value]
#         if self.cards[0].value == self.cards[1].value and self.cards[3].value == self.cards[4].value:
#             return [2, self.cards[0].value, self.cards[3].value, self.cards[2].value]
#         if self.cards[1].value == self.cards[2].value and self.cards[3].value == self.cards[4].value:
#             return [2, self.cards[1].value, self.cards[3].value, self.cards[0].value]
#
#         # check one pair
#         if self.cards[0].value == self.cards[1].value:
#             return [1, self.cards[0].value, self.cards[2].value, self.cards[3].value, self.cards[4].value]
#         if self.cards[1].value == self.cards[2].value:
#             return [1, self.cards[1].value, self.cards[0].value, self.cards[3].value, self.cards[4].value]
#         if self.cards[2].value == self.cards[3].value:
#             return [1, self.cards[2].value, self.cards[0].value, self.cards[1].value, self.cards[4].value]
#         if self.cards[3].value == self.cards[4].value:
#             return [1, self.cards[3].value, self.cards[0].value, self.cards[1].value, self.cards[2].value]
#
#         # kicker
#         return [0] + [c.value for c in self.cards]
#
#
# i1 = 0
# i2 = 0
# with open('poker.txt', 'r') as f:
#     for l in f.readlines():
#         deal = l.split()
#         h1 = Hand(deal[:5]).get_hand()
#         h2 = Hand(deal[5:]).get_hand()
#         res = 0
#         while True:
#             if h1[res] == h2[res]:
#                 res += 1
#             elif h1[res] > h2[res]:
#                 i1 += 1
#                 break
#             else:
#                 i2 += 1
#                 break
# print(i1, i2, i1 + i2)


# def reverse(num):
#     return int(''.join([c for c in reversed(str(num))]))
#
#
# def is_palindrome(num):
#     return num == reverse(num)
#
#
# def is_Lychrel(num):
#     for i in range(50):
#         num += reverse(num)
#         if is_palindrome(num):
#             return False
#     return True
#
#
# print(len([0 for i in range(1, 10000) if is_Lychrel(i)]))

# def dig_sum(num):
#     return sum(int(c) for c in str(num))
#
# print(max(dig_sum(a**n) for a in range(1, 100) for n in range(1, 100)))



# def h2s(hours):
#     fradrag = 5659
#     netto = hours*179
#     return netto*0.92 - (netto*0.92 - fradrag)*0.38 + (6015*0.62 if netto < 12000 else 0)
#
# max_su = h2s(67)
# print(max_su)
# i = 68
# while h2s(i) < max_su:
#     i += 1
# print(i, h2s(i))


# from fractions import Fraction
#
#
# def create_fractions(n):
#     l = []
#     f = Fraction(1, 2)
#     for i in range(n):
#         l.append(1 + f)
#         f = Fraction(1, 2 + f)
#     return l
#
#
# print(len(list(filter(lambda f: len(str(f.numerator)) > len(str(f.denominator)), create_fractions(1000)))))


class Spiral():
    def __init__(self, n):
        self.primes = get_primes_on_interval(0, 10000000)
        print('Got primes')
        self.layers = 1
        self.side_length = 1
        self.matrix = [[1]]
        self.x = self.y = 0
        for _ in range(n - 1):
            self.add_layer()

    def add_layer(self):
        for i, line in enumerate(self.matrix):
            self.matrix[i] = [0] + line + [0]
        self.matrix = [[0] * len(self.matrix[0])] + self.matrix + [[0] * len(self.matrix[0])]
        self.layers += 1
        self.side_length += 2
        self.x += 1
        self.y += 1
        n = self.matrix[self.x][self.y] + 1
        self.y += 1
        for _ in range(self.side_length - 1):
            self.matrix[self.x][self.y] = n
            n += 1
            self.x -= 1
        self.x += 1
        self.y -= 1
        for _ in range(self.side_length - 1):
            self.matrix[self.x][self.y] = n
            n += 1
            self.y -= 1
        self.y += 1
        self.x += 1
        for _ in range(self.side_length - 1):
            self.matrix[self.x][self.y] = n
            n += 1
            self.x += 1
        self.x -= 1
        self.y += 1
        for _ in range(self.side_length - 1):
            self.matrix[self.x][self.y] = n
            n += 1
            self.y += 1
        self.y -= 1

    def get_ratio(self):
        if self.matrix[-1][-1] > self.primes[-1]:
            raise RuntimeError('Not enough primes')
        s = set()
        for i in range(self.side_length):
            s.add(self.matrix[i][i])
            s.add(self.matrix[i][self.side_length - 1 - i])
        return (len(s.intersection(self.primes)) / len(s)) * 100

    def __str__(self):
        s = ""
        for line in self.matrix:
            s += '\t'.join(map(str, line)) + "\n"
        return s


# s = Spiral(750)
# ratio = s.get_ratio()
# while ratio >= 9.5:
#     s.add_layer()
#     ratio = s.get_ratio()
# print(ratio, s.side_length)
# s = Spiral(4)
# ratio = s.get_ratio()
# print(ratio, s.layers)

# def is_prime(num):
#     if num <= 1:
#         return False
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     if num % 3 == 0:
#         return False
#
#     c = 5
#     while c**2 <= num:
#         if n % c == 0 or n % (c + 2) == 0:
#             return False
#         c += 6
#     return True
#
#
# n = 9
# no_of_primes = 3
# step = 2
# while no_of_primes / ((step * 2) + 1) > 0.10:
#     step += 2
#     for _ in range(3):
#         n += step
#         if is_prime(n):
#             no_of_primes += 1
#     n += step
#
# print(step + 1)

# mess = [79, 59, 12, 2, 79, 35, 8, 28, 20, 2, 3, 68, 8, 9, 68, 45, 0, 12, 9, 67, 68, 4, 7, 5, 23, 27, 1, 21, 79, 85, 78,
#         79, 85, 71, 38, 10, 71, 27, 12, 2, 79, 6, 2, 8, 13, 9, 1, 13, 9, 8, 68, 19, 7, 1, 71, 56, 11, 21, 11, 68, 6, 3,
#         22, 2, 14, 0, 30, 79, 1, 31, 6, 23, 19, 10, 0, 73, 79, 44, 2, 79, 19, 6, 28, 68, 16, 6, 16, 15, 79, 35, 8, 11,
#         72, 71, 14, 10, 3, 79, 12, 2, 79, 19, 6, 28, 68, 32, 0, 0, 73, 79, 86, 71, 39, 1, 71, 24, 5, 20, 79, 13, 9, 79,
#         16, 15, 10, 68, 5, 10, 3, 14, 1, 10, 14, 1, 3, 71, 24, 13, 19, 7, 68, 32, 0, 0, 73, 79, 87, 71, 39, 1, 71, 12,
#         22, 2, 14, 16, 2, 11, 68, 2, 25, 1, 21, 22, 16, 15, 6, 10, 0, 79, 16, 15, 10, 22, 2, 79, 13, 20, 65, 68, 41, 0,
#         16, 15, 6, 10, 0, 79, 1, 31, 6, 23, 19, 28, 68, 19, 7, 5, 19, 79, 12, 2, 79, 0, 14, 11, 10, 64, 27, 68, 10, 14,
#         15, 2, 65, 68, 83, 79, 40, 14, 9, 1, 71, 6, 16, 20, 10, 8, 1, 79, 19, 6, 28, 68, 14, 1, 68, 15, 6, 9, 75, 79, 5,
#         9, 11, 68, 19, 7, 13, 20, 79, 8, 14, 9, 1, 71, 8, 13, 17, 10, 23, 71, 3, 13, 0, 7, 16, 71, 27, 11, 71, 10, 18,
#         2, 29, 29, 8, 1, 1, 73, 79, 81, 71, 59, 12, 2, 79, 8, 14, 8, 12, 19, 79, 23, 15, 6, 10, 2, 28, 68, 19, 7, 22, 8,
#         26, 3, 15, 79, 16, 15, 10, 68, 3, 14, 22, 12, 1, 1, 20, 28, 72, 71, 14, 10, 3, 79, 16, 15, 10, 68, 3, 14, 22,
#         12, 1, 1, 20, 28, 68, 4, 14, 10, 71, 1, 1, 17, 10, 22, 71, 10, 28, 19, 6, 10, 0, 26, 13, 20, 7, 68, 14, 27, 74,
#         71, 89, 68, 32, 0, 0, 71, 28, 1, 9, 27, 68, 45, 0, 12, 9, 79, 16, 15, 10, 68, 37, 14, 20, 19, 6, 23, 19, 79, 83,
#         71, 27, 11, 71, 27, 1, 11, 3, 68, 2, 25, 1, 21, 22, 11, 9, 10, 68, 6, 13, 11, 18, 27, 68, 19, 7, 1, 71, 3, 13,
#         0, 7, 16, 71, 28, 11, 71, 27, 12, 6, 27, 68, 2, 25, 1, 21, 22, 11, 9, 10, 68, 10, 6, 3, 15, 27, 68, 5, 10, 8,
#         14, 10, 18, 2, 79, 6, 2, 12, 5, 18, 28, 1, 71, 0, 2, 71, 7, 13, 20, 79, 16, 2, 28, 16, 14, 2, 11, 9, 22, 74, 71,
#         87, 68, 45, 0, 12, 9, 79, 12, 14, 2, 23, 2, 3, 2, 71, 24, 5, 20, 79, 10, 8, 27, 68, 19, 7, 1, 71, 3, 13, 0, 7,
#         16, 92, 79, 12, 2, 79, 19, 6, 28, 68, 8, 1, 8, 30, 79, 5, 71, 24, 13, 19, 1, 1, 20, 28, 68, 19, 0, 68, 19, 7, 1,
#         71, 3, 13, 0, 7, 16, 73, 79, 93, 71, 59, 12, 2, 79, 11, 9, 10, 68, 16, 7, 11, 71, 6, 23, 71, 27, 12, 2, 79, 16,
#         21, 26, 1, 71, 3, 13, 0, 7, 16, 75, 79, 19, 15, 0, 68, 0, 6, 18, 2, 28, 68, 11, 6, 3, 15, 27, 68, 19, 0, 68, 2,
#         25, 1, 21, 22, 11, 9, 10, 72, 71, 24, 5, 20, 79, 3, 8, 6, 10, 0, 79, 16, 8, 79, 7, 8, 2, 1, 71, 6, 10, 19, 0,
#         68, 19, 7, 1, 71, 24, 11, 21, 3, 0, 73, 79, 85, 87, 79, 38, 18, 27, 68, 6, 3, 16, 15, 0, 17, 0, 7, 68, 19, 7, 1,
#         71, 24, 11, 21, 3, 0, 71, 24, 5, 20, 79, 9, 6, 11, 1, 71, 27, 12, 21, 0, 17, 0, 7, 68, 15, 6, 9, 75, 79, 16, 15,
#         10, 68, 16, 0, 22, 11, 11, 68, 3, 6, 0, 9, 72, 16, 71, 29, 1, 4, 0, 3, 9, 6, 30, 2, 79, 12, 14, 2, 68, 16, 7, 1,
#         9, 79, 12, 2, 79, 7, 6, 2, 1, 73, 79, 85, 86, 79, 33, 17, 10, 10, 71, 6, 10, 71, 7, 13, 20, 79, 11, 16, 1, 68,
#         11, 14, 10, 3, 79, 5, 9, 11, 68, 6, 2, 11, 9, 8, 68, 15, 6, 23, 71, 0, 19, 9, 79, 20, 2, 0, 20, 11, 10, 72, 71,
#         7, 1, 71, 24, 5, 20, 79, 10, 8, 27, 68, 6, 12, 7, 2, 31, 16, 2, 11, 74, 71, 94, 86, 71, 45, 17, 19, 79, 16, 8,
#         79, 5, 11, 3, 68, 16, 7, 11, 71, 13, 1, 11, 6, 1, 17, 10, 0, 71, 7, 13, 10, 79, 5, 9, 11, 68, 6, 12, 7, 2, 31,
#         16, 2, 11, 68, 15, 6, 9, 75, 79, 12, 2, 79, 3, 6, 25, 1, 71, 27, 12, 2, 79, 22, 14, 8, 12, 19, 79, 16, 8, 79, 6,
#         2, 12, 11, 10, 10, 68, 4, 7, 13, 11, 11, 22, 2, 1, 68, 8, 9, 68, 32, 0, 0, 73, 79, 85, 84, 79, 48, 15, 10, 29,
#         71, 14, 22, 2, 79, 22, 2, 13, 11, 21, 1, 69, 71, 59, 12, 14, 28, 68, 14, 28, 68, 9, 0, 16, 71, 14, 68, 23, 7,
#         29, 20, 6, 7, 6, 3, 68, 5, 6, 22, 19, 7, 68, 21, 10, 23, 18, 3, 16, 14, 1, 3, 71, 9, 22, 8, 2, 68, 15, 26, 9, 6,
#         1, 68, 23, 14, 23, 20, 6, 11, 9, 79, 11, 21, 79, 20, 11, 14, 10, 75, 79, 16, 15, 6, 23, 71, 29, 1, 5, 6, 22, 19,
#         7, 68, 4, 0, 9, 2, 28, 68, 1, 29, 11, 10, 79, 35, 8, 11, 74, 86, 91, 68, 52, 0, 68, 19, 7, 1, 71, 56, 11, 21,
#         11, 68, 5, 10, 7, 6, 2, 1, 71, 7, 17, 10, 14, 10, 71, 14, 10, 3, 79, 8, 14, 25, 1, 3, 79, 12, 2, 29, 1, 71, 0,
#         10, 71, 10, 5, 21, 27, 12, 71, 14, 9, 8, 1, 3, 71, 26, 23, 73, 79, 44, 2, 79, 19, 6, 28, 68, 1, 26, 8, 11, 79,
#         11, 1, 79, 17, 9, 9, 5, 14, 3, 13, 9, 8, 68, 11, 0, 18, 2, 79, 5, 9, 11, 68, 1, 14, 13, 19, 7, 2, 18, 3, 10, 2,
#         28, 23, 73, 79, 37, 9, 11, 68, 16, 10, 68, 15, 14, 18, 2, 79, 23, 2, 10, 10, 71, 7, 13, 20, 79, 3, 11, 0, 22,
#         30, 67, 68, 19, 7, 1, 71, 8, 8, 8, 29, 29, 71, 0, 2, 71, 27, 12, 2, 79, 11, 9, 3, 29, 71, 60, 11, 9, 79, 11, 1,
#         79, 16, 15, 10, 68, 33, 14, 16, 15, 10, 22, 73]
#
# mess[::3] = list(map(lambda c: chr(c ^ 103), mess[::3]))
# mess[1::3] = list(map(lambda c: chr(c ^ 111), mess[1::3]))
# mess[2::3] = list(map(lambda c: chr(c ^ 100), mess[2::3]))
# print(mess)
# print(sum([ord(c) for c in mess]))


# from itertools import combinations, permutations
# from collections import OrderedDict
# import operator
# import pickle
# import yaml


# def _get_match(small, big):
#     print(small, big)
#     if big.startswith(small):
#         offset = big.replace(small, "", 1)
#         if offset in primes_str and offset + small in primes_str:
#             return offset
#     elif big.endswith(small):
#         offset = big.replace(small, "", 1)
#         if offset in primes_str and small + offset in primes_str:
#             return offset
#
#
# set_size = 4
#
#
# def _print():
#     for item in deps_read.items():
#         print(item[0], ":", sep='', end=' ')
#         print(item[1])
#
#
# primes = get_primes_on_interval(3, 1000000)
# print('Got primes')
# primes_str = list(map(str, primes))
# print('Got str primes')
# #
# # with open('primes.yaml', 'wb') as f:
# #     pickle.dump(primes_str, f)
#
# # with open('primes.yaml', 'rb') as ff:
# #     primes_str = pickle.load(ff)
# # print("UNPICKLED")
#
# deps = OrderedDict()
# for small in primes_str[:primes_str.index('677')]:
#     outcome = set(_get_match(small, big) for big in primes_str[primes_str.index(small):])
#     outcome.add(small)
#     outcome.remove(None)
#     if len(outcome) >= set_size - 1:
#         deps[small] = outcome
#
# # prime_leaving_occurences = list(filter(
# #     lambda x: (x.startswith(prime) or x.endswith(prime)) and x.replace(prime, "", 1) in primes_str,
# #     primes_str))
#
# with open('deps_long.yaml', 'w') as f:
#     f.write(yaml.dump(deps))
#
# with open('deps_long.yaml', 'r') as ff:
#     deps_read = yaml.load(ff)
#
# # print(sorted(set(map(lambda x: x.replace(item[0], "", 1), item[1])), key=int))
#
# # print(len(deps_read))
# # q = dict()
# # for l in deps_read.values():
# #     for num in l:
# #         if num not in q:
# #             q[num] = 0
# #         q[num] += 1
# #
# # for k in q:
# #     if q[k] < set_size and k in deps_read:
# #         del deps_read[k]
# # print(len(deps_read))
# #
# # deps_read = OrderedDict(sorted(deps_read.items(), key=lambda x: q[x[0]]))
# #
# # for item in deps_read.items():
# #     print(q[item[0]], ' ', item[0], ":", sep='', end=' ')
# #     print(item[1])
# #
# # print()
# # print()
# # print()
# #
# for key, value in deps_read.items():
#     value_copy = set(value)
#     for v in value_copy:
#         if v not in deps_read:
#             deps_read[key].remove(v)
#
#
# def _get_intersection(ids):
#     d = deps_read[ids[0]]
#     for s in ids[1:]:
#         d = d.intersection(deps_read[s])
#     return d
#
#
# def _remove_num(n):
#     deps_read[n] = set()
#     for key, value in deps_read.items():
#         if n in value:
#             deps_read[key].remove(n)
#
#
# keys_found = []
# for key, value in deps_read.items():
#     should_delete = True
#     for c in combinations(value, set_size):
#         if set(c).issubset(_get_intersection(c)):
#             should_delete = False
#     if should_delete:
#         _remove_num(key)
#     else:
#         keys_found.append(key)
#
# print(sum(min((tuple(sorted(map(int, deps_read[key]))) for key in keys_found), key=min)))
#
#
# for key, value in deps_read.items():
#     print(key, end=': ')
#     d = set()
#     for k in value:
#         if not d:
#             d = deps_read[k]
#         d = d.intersection(deps_read[k])
#     print(d)
#
#
# for candidate in combinations(deps_read.items(), set_size):
#     nums = {candidate[0][0]}
#     outcomes = set(candidate[0][1])
#     for c in candidate[1:]:
#         nums.add(c[0])
#         outcomes = outcomes.intersection(c[1])
#     # if outcomes:
#     #     print(nums)
#     #     print(outcomes)
#     #     print()
#     if nums.issubset(outcomes):
#         print(sum(map(int, nums)), nums)

from collections import OrderedDict
from itertools import combinations

set_size = 5
max_prime = 1000000
max_looking_for = int(math.sqrt(max_prime))

primes = get_primes_on_interval(3, max_prime)
print(primes)
print(len(primes))
# primes_str = list(map(str, primes))
# print('Got primes')
#
# deps = {}
# s = 10000
# for p in primes_str:
#     if int(p) > s:
#         print(p)
#         s += 10000
#     for sep in range(1, len(p)):
#         left = p[:sep]
#         if left in primes_str:
#             right = p[sep:]
#             if right in primes_str:
#                 if right + left in primes_str:
#                     v1 = int(left)
#                     v2 = int(right)
#                     if v1 <= max_looking_for and v2 <= max_looking_for:
#                         if v1 not in deps:
#                             deps[v1] = {v1}
#                         if v2 not in deps:
#                             deps[v2] = {v2}
#                         deps[v1].add(v2)
#                         deps[v2].add(v1)

# deps = OrderedDict(sorted(deps.items()))
# print('{')
# for key in deps:
#     print(key, deps[key], sep=': ', end=', \n')
# print('}')

deps = {
    3: {3, 7, 137, 11, 271, 17, 541, 31, 673, 929, 37, 557, 947, 823, 59, 701, 191, 449, 67, 73, 331, 719, 467, 733,
        607, 739, 229, 613, 359, 617, 109, 499, 373},
    7: {3, 7, 523, 19, 283, 541, 673, 547, 937, 433, 691, 823, 829, 61, 853, 97, 229, 487, 109, 883, 757, 127},
    11: {353, 3, 743, 839, 11, 587, 941, 239, 113, 23, 503, 953, 251, 701, 863},
    13: {577, 709, 997, 103, 331, 523, 13, 367, 241, 337, 19, 61, 829, 127},
    17: {257, 449, 3, 389, 491, 971, 239, 431, 17, 881, 83, 383},
    19: {577, 97, 163, 709, 997, 7, 937, 13, 79, 433, 19, 181, 727, 571, 31, 991},
    23: {89, 509, 773, 677, 743, 11, 47, 23, 761, 827, 311},
    29: {71, 167, 137, 683, 569, 401, 881, 179, 599, 761, 347, 29, 383},
    31: {3, 139, 907, 19, 181, 151, 859, 31, 991},
    37: {3, 67, 37, 967, 199, 607, 79, 463, 277, 313, 991},
    41: {257, 227, 41, 911, 719, 593, 887, 863},
    43: {97, 613, 103, 43, 271, 499, 691, 223},
    47: {419, 293, 521, 269, 47, 947, 149, 23, 251},
    53: {353, 419, 197, 269, 653, 113, 401, 53},
    59: {929, 3, 419, 197, 167, 971, 59},
    61: {487, 7, 331, 13, 751, 151, 409, 61},
    67: {547, 67, 3, 37, 139, 619, 751, 757, 601, 157},
    71: {257, 389, 71, 263, 233, 971, 719, 29, 947, 821, 887, 443, 317},
    73: {547, 3, 643, 73, 277, 757, 823, 571, 607},
    79: {193, 613, 37, 967, 397, 79, 367, 241, 19, 631},
    83: {449, 227, 773, 911, 719, 17, 83, 563, 311, 443, 701},
    89: {293, 137, 521, 107, 809, 431, 977, 23, 821, 983, 89, 443},
    97: {97, 967, 7, 43, 241, 19, 787, 373, 883, 919, 157, 379, 829},
    101: {641, 101, 197, 359, 107, 719, 467, 149, 383},
    103: {997, 421, 103, 43, 13, 307},
    107: {89, 449, 101, 107, 857},
    109: {673, 3, 7, 199, 139, 109, 883, 661, 919, 313, 859},
    113: {131, 227, 647, 167, 233, 11, 113, 53, 149, 983, 761, 383},
    127: {163, 7, 331, 13, 271, 241, 373, 157, 601, 127, 733, 607},
    131: {449, 641, 131, 839, 743, 617, 941, 113, 797, 479},
    137: {353, 3, 197, 743, 359, 137, 491, 587, 239, 659, 947, 89, 29, 191},
    139: {547, 67, 709, 967, 457, 139, 619, 109, 907, 367, 787, 661, 31},
    149: {101, 491, 971, 173, 47, 113, 563, 149, 953, 251},
    151: {769, 163, 937, 397, 433, 499, 631, 151, 31, 61, 607},
    157: {97, 67, 229, 181, 277, 157, 571, 733, 127},
    163: {193, 163, 613, 997, 811, 367, 19, 307, 883, 151, 409, 127},
    167: {641, 677, 167, 521, 59, 491, 269, 911, 113, 443, 29},
    173: {293, 743, 173, 431, 659, 149, 347, 191},
    179: {743, 269, 719, 593, 179, 953, 317, 29, 383},
    181: {193, 421, 199, 619, 397, 751, 19, 499, 181, 757, 787, 283, 31, 157, 607},
    191: {3, 227, 281, 137, 173, 461, 977, 599, 953, 251, 191},
    193: {577, 193, 163, 811, 79, 751, 433, 883, 181, 373, 601, 283, 541},
    197: {641, 197, 101, 137, 59, 971, 947, 53, 311, 569, 347},
    199: {673, 739, 37, 199, 811, 109, 877, 751, 211, 181, 373, 379},
    211: {199, 271, 211, 499, 373, 727, 313, 283, 349, 571},
    223: {547, 229, 43, 337, 277, 919, 829, 223},
    227: {227, 41, 719, 593, 113, 83, 281, 827, 191},
    229: {547, 3, 613, 229, 7, 937, 433, 499, 373, 631, 157, 223},
    233: {71, 233, 617, 911, 239, 113, 881, 251, 983, 347},
    239: {641, 929, 263, 137, 233, 11, 461, 239, 17, 977, 947, 347, 509},
    241: {97, 739, 421, 313, 727, 811, 13, 79, 271, 241, 691, 883, 823, 601, 127},
    251: {233, 11, 971, 941, 491, 47, 431, 251, 149, 761, 347, 191},
    257: {257, 293, 263, 71, 41, 17},
    263: {257, 293, 647, 263, 71, 941, 239, 821, 761, 443},
    269: {389, 167, 617, 461, 269, 47, 431, 179, 53, 887, 317},
    271: {3, 43, 271, 241, 211, 409, 127},
    277: {37, 73, 331, 751, 499, 787, 277, 859, 157, 223},
    281: {509, 227, 419, 281, 971, 557, 653, 719, 857, 797, 191},
    283: {193, 487, 7, 397, 463, 211, 181, 601, 283, 541},
    293: {257, 293, 263, 617, 173, 47, 467, 311, 89, 827},
    307: {577, 163, 103, 523, 367, 307, 631, 733},
    311: {197, 677, 293, 359, 653, 881, 83, 821, 23, 827, 311},
    313: {37, 619, 109, 241, 211, 727, 313, 991},
    317: {353, 419, 503, 773, 71, 269, 179, 983, 317},
    331: {577, 3, 739, 937, 331, 907, 13, 883, 61, 277, 349, 127},
    337: {223, 13, 397, 337, 691, 919, 349, 607},
    347: {197, 233, 173, 239, 401, 347, 443, 983, 251, 29},
    349: {709, 967, 331, 337, 211, 499, 373, 919, 409, 349, 829},
    353: {353, 359, 317, 137, 11, 53, 443, 797},
    359: {353, 509, 3, 101, 359, 137, 911, 311, 563, 599, 701},
    367: {163, 613, 457, 139, 13, 79, 367, 751, 307},
    373: {97, 193, 3, 229, 199, 937, 211, 373, 661, 823, 859, 349, 127},
    379: {97, 997, 199, 811, 397, 877, 751, 379},
    383: {419, 101, 941, 17, 113, 179, 29, 821, 797, 383},
    389: {389, 71, 971, 269, 17, 947, 761, 797},
    397: {673, 547, 907, 397, 79, 283, 337, 181, 151, 379},
    401: {743, 809, 593, 401, 53, 887, 347, 29},
    409: {163, 709, 271, 61, 691, 409, 349, 733},
    419: {449, 929, 419, 317, 59, 47, 563, 53, 599, 281, 443, 701, 383},
    421: {643, 709, 421, 103, 241, 433, 181, 661, 607},
    431: {89, 929, 269, 173, 431, 17, 947, 983, 857, 251, 479},
    433: {193, 229, 421, 7, 433, 19, 787, 883, 151, 571, 859},
    439: {613, 787, 853, 661, 439, 601, 541},
    443: {89, 353, 419, 263, 71, 167, 83, 761, 443, 983, 953, 347, 701},
    449: {449, 3, 131, 419, 107, 557, 941, 17, 83, 563, 821},
    457: {673, 643, 457, 139, 367, 757, 829},
    461: {677, 479, 461, 269, 239, 653, 983, 569, 191},
    463: {643, 37, 613, 523, 463, 283, 829},
    467: {641, 3, 101, 293, 617, 587, 941, 467},
    479: {131, 971, 461, 431, 593, 881, 821, 599, 569, 701, 479},
    487: {769, 487, 7, 757, 727, 601, 283, 61},
    491: {773, 167, 137, 491, 653, 17, 593, 149, 983, 251},
    499: {673, 3, 229, 43, 499, 211, 181, 277, 151, 691, 349},
    503: {647, 11, 653, 911, 563, 503, 317},
    509: {509, 647, 359, 239, 947, 23, 281, 797, 863},
    521: {641, 167, 809, 521, 557, 47, 659, 89},
    523: {577, 7, 523, 13, 463, 307, 541},
    541: {193, 439, 3, 7, 523, 283, 661, 727, 571, 541, 991},
    547: {577, 769, 67, 547, 229, 643, 7, 709, 73, 139, 397, 787, 661, 853, 823, 223},
    557: {449, 3, 521, 557, 281},
    563: {449, 419, 359, 809, 587, 971, 83, 563, 149, 503},
    569: {773, 197, 809, 461, 29, 659, 887, 569, 797, 479},
    571: {73, 433, 19, 211, 853, 157, 571, 541},
    577: {577, 193, 547, 613, 937, 331, 523, 13, 19, 307, 757},
    587: {677, 137, 617, 587, 11, 467, 563},
    593: {227, 647, 41, 479, 491, 593, 401, 179, 977, 863},
    599: {191, 419, 359, 941, 719, 599, 29, 479},
    601: {193, 439, 67, 487, 241, 823, 601, 283, 127},
    607: {3, 37, 421, 967, 73, 619, 337, 181, 151, 991, 127, 607},
    613: {577, 673, 3, 163, 613, 229, 43, 79, 367, 463, 883, 661, 439, 829},
    617: {3, 131, 293, 647, 617, 233, 587, 269, 887, 467, 983},
    619: {67, 619, 811, 139, 181, 313, 607},
    631: {739, 229, 751, 79, 307, 631, 151},
    641: {641, 929, 131, 101, 197, 167, 521, 239, 881, 467, 821, 863},
    643: {547, 643, 421, 73, 457, 463, 751, 991},
    647: {647, 263, 617, 593, 113, 821, 503, 953, 509},
    653: {491, 941, 461, 653, 659, 53, 503, 281, 311},
    659: {137, 521, 173, 653, 659, 947, 983, 569},
    661: {769, 547, 613, 421, 139, 109, 877, 883, 373, 661, 439, 541},
    673: {673, 769, 3, 613, 199, 7, 457, 109, 397, 499},
    677: {677, 167, 587, 461, 23, 827, 311},
    683: {719, 683, 29, 911},
    691: {709, 7, 727, 43, 907, 337, 241, 691, 499, 919, 409},
    701: {3, 419, 359, 11, 83, 443, 701, 479},
    709: {547, 709, 421, 967, 139, 13, 19, 691, 823, 409, 349},
    719: {3, 227, 773, 101, 71, 41, 683, 719, 911, 83, 179, 947, 599, 281},
    727: {997, 487, 727, 241, 19, 211, 691, 823, 313, 541},
    733: {3, 733, 883, 307, 157, 409, 127, 829, 991},
    739: {3, 739, 967, 199, 331, 751, 241, 853, 631},
    743: {131, 743, 137, 11, 173, 401, 881, 179, 947, 23},
    751: {193, 67, 643, 997, 739, 199, 751, 367, 787, 181, 277, 631, 379, 61},
    757: {577, 67, 487, 7, 73, 457, 811, 181, 757, 829},
    761: {389, 263, 251, 113, 977, 23, 761, 443, 29},
    769: {769, 673, 547, 997, 487, 661, 919, 151},
    773: {773, 491, 719, 83, 23, 569, 953, 317},
    787: {97, 439, 547, 139, 751, 433, 787, 277, 181, 823},
    797: {353, 131, 389, 281, 797, 569, 509, 383},
    809: {89, 929, 839, 809, 521, 401, 563, 821, 983, 569, 827},
    811: {193, 163, 997, 199, 811, 619, 241, 757, 919, 379, 991},
    821: {89, 449, 641, 647, 71, 263, 809, 971, 383, 821, 311, 857, 827, 479},
    823: {547, 3, 709, 967, 7, 73, 877, 823, 241, 787, 373, 727, 601},
    827: {227, 293, 677, 809, 821, 23, 857, 827, 311},
    829: {97, 613, 7, 457, 829, 13, 463, 757, 349, 733, 223},
    839: {131, 839, 809, 11, 911, 887},
    853: {547, 739, 7, 853, 439, 571},
    857: {281, 107, 431, 821, 857, 827},
    859: {109, 433, 373, 277, 919, 859, 31},
    863: {641, 41, 11, 593, 983, 509, 863},
    877: {997, 199, 937, 877, 883, 661, 823, 379},
    881: {641, 743, 233, 17, 881, 29, 983, 953, 311, 479},
    883: {97, 193, 163, 613, 7, 331, 109, 877, 241, 433, 883, 661, 733, 991},
    887: {839, 71, 41, 617, 269, 401, 887, 569},
    907: {331, 907, 139, 397, 691, 31},
    911: {359, 167, 41, 233, 683, 839, 911, 719, 83, 947, 503},
    919: {97, 769, 937, 811, 109, 337, 691, 919, 859, 349, 223},
    929: {929, 641, 3, 419, 809, 941, 239, 431, 983, 953, 59},
    937: {577, 229, 7, 937, 331, 877, 19, 373, 919, 151},
    941: {449, 929, 131, 263, 11, 941, 653, 467, 599, 251, 383},
    947: {3, 197, 389, 743, 71, 137, 47, 239, 431, 719, 947, 659, 911, 509},
    953: {929, 773, 647, 11, 881, 179, 149, 953, 443, 191},
    967: {97, 739, 709, 37, 967, 139, 79, 823, 349, 607},
    971: {197, 389, 71, 59, 971, 17, 977, 563, 149, 821, 281, 251, 479},
    977: {89, 971, 239, 593, 977, 761, 191},
    983: {929, 233, 617, 491, 809, 461, 431, 113, 881, 659, 347, 983, 89, 443, 317, 863},
    991: {541, 643, 37, 811, 19, 883, 313, 991, 31, 733, 607},
    997: {769, 163, 997, 103, 811, 13, 877, 751, 19, 727, 379},
}

sums = []
keys = deps.keys()
for candidate in combinations(keys, set_size):
    out = deps[candidate[0]].intersection(deps[candidate[1]])
    for key in candidate[2:]:
        out = out.intersection(deps[key])
    if len(out) == set_size:
        s = sum(out)
        print(candidate, out, s)
        sums.append(s)

print()
print("Min sum: {}".format(min(sums)))
