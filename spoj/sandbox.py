import time

e = 50
l1 = [e] * 200000 + [70]
l2 = l1[:]
l3 = l2[:]

print('Lists created')

start_time = time.monotonic()
while e in l1:
    l1.remove(e)
print('First method done in {} seconds, list is now {}'.format(time.monotonic() - start_time, l1))

start_time = time.monotonic()
try:
    while True:
        l2.remove(e)
except ValueError:
    pass
print('First method done in {} seconds, list is now {}'.format(time.monotonic() - start_time, l2))

start_time = time.monotonic()
l4 = l3[:]
del l3[:]
for el in l4:
    if el != e:
        l3.append(el)
print('Third method done in {} seconds, list is now {}'.format(time.monotonic() - start_time, l3))


