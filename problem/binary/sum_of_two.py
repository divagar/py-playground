def sum(a, b):
    mask = 0xFFFFFFFF
    maxInt = 0x7FFFFFFF
    while b != 0:
        sum = a ^ b
        carry = (a & b) << 1
        a = sum & mask
        b = carry & mask
    if(a < maxInt):
        return a
    else:
        print(a)
        print(a ^ mask)
        result = a ^ mask
        return ~result


print("a = 2, b = 3, sum = ", sum(2, 3))
print("a = 5, b = 10, sum = ", sum(5, 10))
print("a = -1, b = 1, sum = ", sum(-1, 1))
print("a = -12, b = -8, sum = ", sum(-12, -8))
