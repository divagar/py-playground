def rob(nums):
    print("rob -> ", nums)
    n = len(nums)
    ret = [0] * n

    for i, val in enumerate(nums):
        if(i == 0):
            ret[0] = nums[0]
        elif(i == 1):
            ret[1] = max(nums[0], nums[1])
        elif(i>=2):
            ret[i] = max((nums[i] + ret[i-2]), ret[i-1])
        print(ret)

    return ret[n-1]


def run(a):
    if len(a) == 0:
        return 0
    if len(a) == 1:
        return a[0]
    else:
        return max(rob(a[1:]), rob(a[:-1]))


a = [1, 2, 3, 1]
out = run(a)
print(out)
