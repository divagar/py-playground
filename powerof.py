def powof_i(x, n):
    ret = 1
    for v in range(n):
        ret = x * ret
    return ret


def powof_r(x, n):
    if(n == 1):
        return x
    return x * powof_r(x, n-1)


def powof_r_1(x, n):
    return x if n == 1 else x * powof_r(x, n-1)


v = powof_i(2, 5)
print("v -> ", v)

v = powof_r(2, 5)
print("v -> ", v)

v = powof_r_1(2, 5)
print("v -> ", v)
