class Solution:
    def runningSum(self, nums):
        for i in range(len(nums)):
            if i == 0:
                x = nums[i]
                continue
            nums[i] += x
            x = nums[i]
        return nums
        
x = [1,2,3,4,5]
s = Solution()
y = s.runningSum(x)
print(y)
