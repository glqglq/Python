first = ['one','two','three','four','five','six','seven','eight','nine']

#second = ['ten','']

nums = list(raw_input('Enter a num:'))
for i in range(len(nums)):
    if i != 0:
        print '-',
    nums[i] = int(nums[i])
    print first[nums[i] - 1],