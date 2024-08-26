def search(nums, key):
    for i in range(len(nums)):
        if key == nums[i]:
            return i
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
key = 0
print(search(nums, key))


def bSearch(nums, key):
    first = 0
    last = len(nums) - 1

    while first <= last:
        mid = first + (last - first) // 2

        if key == nums[mid]:
            return mid

        if nums[first] <= nums[mid]:
            if key > nums[mid] or key < nums[first]:
                first = mid + 1
            else:
                last = mid - 1
        else:
            if key < nums[mid]  or key > nums[last]:
                last = mid - 1
            else:
                first = mid + 1
    return -1
        

nums = [4, 5, 6, 7, 0, 1, 2]
key = 0
print(bSearch(nums, key))
