nums = [2, 7, 11, 15]
target = 9
out = []
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if((nums[i] + nums[j]) == target):
            out.append(i)
            out.append(j)
print(out)

def checkTwoSum(nums, target):
    dict = {}
    out = []
    
    for i in range(len(nums)):
        dict[nums[i]] = i
    print("dict -> ", dict)

checkTwoSum(nums, target)


def twoSum(nums, target):
    dic = {}
    arr = []
    for i in range(len(nums)):
        temp = target- nums[i]
      
        if temp in dic:
            print(i, temp)
            arr.append(dic[temp])
            arr.append(i)
           
            return arr
        dic[nums[i]] = i
print(twoSum([1, 7, 11, 15, 4, 5], target))