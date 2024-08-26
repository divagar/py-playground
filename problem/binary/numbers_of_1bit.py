def get1bit(n):
    count = 0
    for i in str(bin(n)):
        if(i == "1"):
            count += 1
    return count


n = '00000000000000000000000000001011'
print(get1bit(n))
