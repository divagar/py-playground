def binarySearch(nums, k):
    numsLen = len(nums) -1
    left = 0
    right = numsLen

    while left <= right:
        mid = (left+right) // 2
        print(mid)
        if(nums[mid] == k):
            return mid
        elif(nums[mid] < k):
            left = mid + 1
        else:
            right = mid - 1

x = [5, 57, 3, 73, 36, 7, 6, 1]
x = sorted(x)
k = 36
out = binarySearch(x, k)
print(f"In {x}")
print(f"out {out}")
