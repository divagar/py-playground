def climb(n):
    ret = [0] * (n+1)

    if n == 0:
        return 1
        
    if(n > 0):
        ret[0] = 1
    if(n > 1):
        ret[1] = 1
    print("ret 1 >", ret)
    for i in range(2, n+1):
        ret[i] = ret[i-2] + ret[i-1]
    print("ret 2 >", ret)
    return ret[n]


print("Climb ->", climb(1))
