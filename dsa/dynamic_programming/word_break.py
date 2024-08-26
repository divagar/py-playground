def isPresent(myStr, myDict):
    for i in range(len(myStr) + 1):
        first = myStr[:i]
        print("first", first)
        if first in myDict:
            second = myStr[i:]
            print("second", second)
            if not len(second) or second in myDict or isPresent(second, myDict):
                return True
    return False


#myStr = "helloworld"
#myDict = ["hello", "world"]
myStr = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
myDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa",
          "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
out = isPresent(myStr, myDict)
print(out)
