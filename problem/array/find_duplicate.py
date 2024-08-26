
def findDuplicate(nums):
    dict = {}
    for i in range(len(nums)):
        if nums[i] in dict:
            return True
        dict[nums[i]] = i
    return False

nums = [35, 352, 25, 25, 15, 6, 636, 66, 2, 1, 6, 662]
print(findDuplicate(nums))