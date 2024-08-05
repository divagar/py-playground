'''
Given a sorted list of numbers, remove duplicates and return the new length. You must do this in-place and without using extra memory.
'''
# using two pointer solution: use 
def removeDuplicate(nums):
    x = 0
    y = 0
    for i, n in enumerate(nums):
        x = i
        if nums[x] != nums[y]:
            y += 1
            nums[y] = n
    nums = nums[:y+1]
    return nums
        

x = [1,1,2,2,2,3,3,4]
y = removeDuplicate(x)
print(y)
