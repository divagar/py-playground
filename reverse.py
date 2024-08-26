def reverse(data):
    for x in range(len(data)-1, -1, -1):
        yield data[x]

rit = reverse("hello")
print(next(rit))
print(next(rit))
print(next(rit))
print(next(rit))
print(next(rit))
