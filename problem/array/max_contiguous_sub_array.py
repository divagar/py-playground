def getContiguousSubArray(input):
    maxSubArr = []

    for i in range(len(input)):
        for j in range(i+1, len(input)):
            subArr = input[i:j]
            if sum(maxSubArr) < sum(subArr):
                maxSubArr = subArr

    return maxSubArr


def getContiguousSubArray1(input):
    dp = [0] * (len(input))
    if len(input) > 1:
        dp[0] = input[0]

    for i in range(1, len(input)):
        dp[i] = max(input[i], dp[i-1] + input[i])
        print(dp)

    return dp


input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output = getContiguousSubArray(input)
print(output)
print(sum(output))

output = getContiguousSubArray1(input)
print(output)
