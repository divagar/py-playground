def getSumPair(data, targetSum):
    left = 0
    right = len(data) - 1

    for i in range(len(data)):
        if(data[left] + data[right] > targetSum):
            right += 1
        elif (data[left] + data[right] < targetSum):
            left += 1
        else:
            return (left, right)

data = [2, 3, 4, 5, 6, 1, 5, 4, 5]
print(data)
targetSum = 11
out = getSumPair(data, targetSum)
print(out)
