def maxArea(nums):
    first = 0
    last = len(nums) - 1
    max = 0

    while first <= last:
        min = nums[first] if nums[first] < nums[last] else nums[last]
        distance = last - first
        currentMax = min * distance
        max = currentMax if max < currentMax else max

        print("---")
        print("first -> ", first)
        print("last -> ", last)
        print("min -> ", min)
        print("max -> ", max)

        if nums[first] < nums[last]:
            first += 1
        else:
            last -= 1
    return max


nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(nums))
