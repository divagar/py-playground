def findAvgOfSubArr(data, subArraySize):
    startWindow = 0
    subTotal = 0
    result = []

    for endWindow in range(len(data)):
        subTotal += data[endWindow]
        if endWindow >= subArraySize - 1:
            result.append(subTotal / subArraySize)
            subTotal -= data[startWindow]
            startWindow += 1
    return result


data = [1, 4, 5, 1, 5, 8, 9, 2, 3]
subArraySize = 5
out = findAvgOfSubArr(data, subArraySize)
print(out)
