def maxSubarray(nums):
    currentSum = maxSum = nums[0]

    for i in range(len(nums)):
        if currentSum < 0:
            currentSum = 0
        currentSum += nums[i]
        if currentSum > maxSum:
            maxSum = currentSum
    return maxSum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubarray(nums))
