def rob(nums):
    n = len(nums)
    ret = [0] * n

    for i, val in enumerate(nums):
        if(i == 0):
            ret[0] = nums[0]
        elif(i == 1):
            ret[1] = max(nums[0], nums[1])
        else:
            ret[i] = max((nums[i] + ret[i-2]), ret[i-1])
        print(ret)

    return ret[n-1]


a = [4, 3, 5, 6, 7, 1, 2]
rob(a)
