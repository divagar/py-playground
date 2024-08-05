'''
Given a array of int and a target int
find a pair of sum int of target
'''

def findTwoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum = nums[i] + nums[j]
            if(sum == target):
                return [nums[i], nums[j]]
    return False

def findTwoSum2(nums, target):
    store = {}
    for n in nums:
        x = target - n
        if x in store:
            return [x, n]
        store[n] = 0
    return False

nums = [4, 5, 6, 7, 8]
target = 12

out = findTwoSum(nums, target)
print(f"out {out}")

out = findTwoSum2(nums, target)
print(f"out {out}")