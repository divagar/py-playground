'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
def stockPrice(prices):
    min = None
    max = None

    for i in range(len(prices)):
        if min == None or prices[i] < prices[min]:
            min = i
        if max == None or prices[i] > prices[max]:
            max = i
    return prices[max] - prices[min]

def stockPrice2(prices):
    buy = None
    currentBuy = None
    profit = None
    currentProfit = None

    for i in range(len(prices)):
        print("prices[i] ", prices[i])
        if buy is None:
            buy = prices[i]
            currentBuy = prices[i]
        
        if profit is None:
            profit = (max(prices[i:]) - buy)
        
        if(prices[i] > buy):
            continue
        else:
            currentBuy =  prices[i]
        
        if profit < (max(prices[i:]) - currentBuy):
            profit = (max(prices[i:]) - currentBuy)
            buy = currentBuy

        print("buy ", buy)
        print("profit ", profit)
    return profit

prices = [2, 4, 1]
out = stockPrice(prices)
print(f"out {out}")
