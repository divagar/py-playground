def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


# n = 45
# out = fib(n)
# print(out)

# 1 1 2 3 5 8 13


def nfib(n, store):
    if n in store:
        return store[n]
    if n < 2:
        return n

    store[n] = nfib(n-1, store) + nfib(n-2, store)
    return store[n]


# n = 12
# out = nfib(n, {})
# print(out)

def dpFib(n):
    out = [0] * n

    if n < 2:
        return 1

    out[0] = 1
    out[1] = 1
    for i in range(2, n):
        out[i] = out[i-1] + out[i-2]
    return out[n-1]

n = 100
out = dpFib(n)
print(out)
