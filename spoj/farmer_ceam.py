plots = {'1':2}
number = 2
for i in range(2, 1000001):
    number += i
    plots[str(i)] = number

line = input()
while line != '0 0 0 0':
    nums = line.split(' ')
    money_left = int(nums[0]) - plots[nums[1]] * int(nums[2])
    if money_left >= int(nums[3]):
        print('Farmer Cream will have {} Bsf to spend.'.format(money_left))
    else:
        print('The firm is trying to bankrupt Farmer Cream by {} Bsf.'.format(int(nums[3]) - money_left))
    line = input()