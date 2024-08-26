from locale import currency


def incrementArr(input):
    carry = 1
    size = len(input)
    result = input

    for x in range(size-1, -1, -1):
        current = input[x] + carry
        if current > 9:
            result[x] = 0
            carry = 1
        else:
            result[x] = current
            carry = 0

    if carry:
        result = [1] + result

    return result


input = [9, 9, 9, 9]
output = incrementArr(input)
print(output)
