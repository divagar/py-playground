
def productOfArray(nums):
    out = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i is not j:
                product *= nums[j]
        out.append(product)
    return out


nums = [1, 5, 2, 3, 7, 6]
print(productOfArray(nums))


def productOfArray1(nums):
    out = []
    product = 1

    for i in range(1, len(nums)):
        product *= nums[i]
    out.append(product)

    for i in range(1, len(nums)):
        out.append(out[0]//nums[i])
    return out


nums = [1, 5, 2, 3, 7, 6]
print(productOfArray1(nums))


def productOfArray2(nums):
    print(nums)
    out = [1] * len(nums)
    left = [1] * len(nums)
    right = [1] * len(nums)

    for i in range(1, len(nums)):
        left[i] = left[i-1] * nums[i-1]
        right[-i-1] = right[-i] * nums[-i]

    for i in range(len(nums)):
        out[i] = left[i] * right[i]

    return out


nums = [1, 5, 2, 3, 7, 6]
print(productOfArray2(nums))
