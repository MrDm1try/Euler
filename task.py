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

import logging
import sys

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