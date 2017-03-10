line = input()
while line != '0 0':
    nums = line.split(' ')
    print(int(nums[0]) ** int(nums[1]))
    line = input()