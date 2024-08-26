def getMissingNumber(nums):
    expectedSum = sum(range(len(nums)+1))
    currentSum = sum(nums)
    return expectedSum - currentSum

nums = [0, 2, 3, 4]
print(getMissingNumber(nums))