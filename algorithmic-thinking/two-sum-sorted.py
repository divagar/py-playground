'''
Given an array of integers sorted in ascending order, 
find two numbers that add up to a given target.
Return the indices of the two numbers in ascending order. 
You can assume elements in the array are unique and there is only one solution.
Do this in O(n) time and with constant auxiliary space.
'''

def twoSumSorted(nums, k):
    numsLen = len(nums)-1
    s = 0
    e = numsLen
    for i in range(numsLen, -1 , -1):
        print("e =", e)
        sum = nums[e] + nums[s]
        print("sum = ", sum)
        if(sum > k):
            e -= 1
            continue
        elif(sum == k):
            return [s, e]
        else:
            s +=1
    return []
        
        

x = [2, 3, 4, 5, 8, 11, 18]
k = 8
y = twoSumSorted(x, k)
print(y)
