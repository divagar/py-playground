def product(nums, acc):
    if len(nums) == 0:
        return acc
    return acc + product(nums[-1], acc)


x = [1, 2, 3, 4, 5]
y = product(x, acc=0)
print(x)
print(y)