def maxProductSubArray(nums):
    curProduct = maxProduct = 0

    for i in range(len(nums)):
        if curProduct < 0:
            curProduct = 0
        curProduct *= nums[i]
        if curProduct > maxProduct:
            maxProduct = curProduct
        return maxProduct


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxProductSubArray(nums))