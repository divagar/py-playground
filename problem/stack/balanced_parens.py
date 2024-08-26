def checkParens(openEle, closeEle):
    if openEle == '[' and closeEle == ']':
        return True
    elif openEle == '(' and closeEle == ')':
        return True
    elif openEle == '{' and closeEle == '}':
        return True
    else:
        return False


def isBalancedParens(input):
    inputArr = input.split(" ")
    result = []

    for ele in inputArr:
        resultLen = len(result)
        if resultLen != 0 and checkParens(result[resultLen-1], ele):
            result.pop()
        else:
            result.append(ele)
        print(result)

    if len(result) == 0:
        return True
    else:
        return False


input = "[ ( { ( ) } ) [ ] }"
output = isBalancedParens(input)
print(output)
