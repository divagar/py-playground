def anagrams(x):
    out = []

    if len(x) == 0:
        print(x, [x])
        return [x]

    for word in anagrams(x[1:]):
        print("word->",word)
        print("x->", x)
        for p in range(len(word) + 1):
            out.append(word[:p] + x[0] + word[p:])
    return out

x = "a"
out = anagrams(x)
print(out)