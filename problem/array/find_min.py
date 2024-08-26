
def findMin(nums):
    min = nums[0]
    for i in range(1, len(nums)):
        if min > nums[i]:
            min = nums[i]
    return min

nums = [4, 5, 6, 7, 1, 2, 3]
print(findMin(nums))


def findMin_1(nums):
    start = 0
    end = len(nums) - 1

    if(nums[0] < nums[end] or len(nums) == 1):
        return nums[0]

    while start <= end:
        mid = start + (end-start) // 2

        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        if nums[mid] < nums[mid-1]:
            return nums[mid]

        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


nums = [4, 5, 6, 7, 1, 2, 3]
print(findMin_1(nums))
