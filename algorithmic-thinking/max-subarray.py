def maxSubArray(nums):
    max = 0
    s = 0
    e = 0
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            su = sum(nums[i:j+2])
            print(nums[i:j+2])
            print(su)
            if(su > max):
                max = su
                s = i
                e = j+2
    return max, s, e


nums = [-2,1,-3,4,-1,2,1,-5,4]
max, s, e = maxSubArray(nums)
print("max = ", max)
print("sub array = ", nums[s:e])