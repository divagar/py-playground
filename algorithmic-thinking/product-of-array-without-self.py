def productOfArr(nums):
    out = []
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if(i != j):
                prod *= nums[j]
        out.append(prod)
    return out

import math
def productOfArr2(nums):
    out = []
    for i in range(len(nums)):
        left = nums[:i]
        right = nums[i+1:]
        total = left + right
        prod = math.prod(total)
        out.append(prod)
    return out


x = [-1,1,0,-3,3]
out = productOfArr(x)
print(f"out {out}")
