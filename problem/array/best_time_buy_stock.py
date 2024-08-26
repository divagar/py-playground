def maxProfit(prices):

    left = 0
    right = 1
    maxProfit = 0

    while(right < len(prices)):
        profit = prices[right] - prices[left]

        if(profit > maxProfit):
            maxProfit = profit

        if(prices[left] > prices[right]):
            left = right
        right += 1

    if(maxProfit > 0):
        return maxProfit
    else:
        return 0


x = [7, 6, 4, 3, 1]
p = maxProfit(x)
print(p)

# def findMinMax(prices):
#     min = 0
#     max = 0

#     if len(prices) == 0:
#         return (0, 0)

#     if len(prices) == 1:
#         min = prices[0]
#         max = prices[0]
#         return (min, max)

#     if len(prices) == 2 and prices[0] < prices[1]:
#         min = prices[0]
#         max = prices[1]
#         return max - min
#     elif len(prices) == 2 and prices[0] > prices[1]:
#         min = prices[1]
#         max = prices[0]
#         return (0, 0)

#     if prices[0] < prices[1]:
#         min = prices[0]
#         max = 0
#     else:
#         min = prices[1]
#         max = 0

#     for i in range(1, len(prices)):
#         if prices[i] < min:
#             min = prices[i]
#             max = 0
#         elif prices[i] > max:
#             max = prices[i]

#     return (min, max)


# x = [1,4,2]
# min, max = findMinMax(x)
# print("min -> ", min)
# print("max -> ", max)
# print(max-min)
