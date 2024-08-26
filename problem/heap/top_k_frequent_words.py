import heapq

def findFrequentWords(words, k):
    out = []
    ret = []
    dict = {}
    for i in range(len(words)):
        if words[i] in dict:
            dict[words[i]] += 1
        else:
            dict[words[i]] = 1
    print(dict)

    for key,val in dict.items():
        heapq.heappush(out, (val,key))
    print(out)

    size = k
    while size > 0 :
        ret.append(heapq.heappop(out)[1])
        size -= 1

    return ret


words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k=4
print(findFrequentWords(words, k))
