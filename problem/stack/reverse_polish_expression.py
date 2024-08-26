def detectOp(op):
    if op == '+' or op == '-' or op == "*" or op == "/":
        return True
    else:
        return False


def evalOp(num1, num2, op):
    if op == '+':
        return (num1 + num2)
    elif op == '-':
        return (num1 - num2)
    elif op == '*':
        return (num1 * num2)
    elif op == '/':
        return (num1 / num2)
    else:
        print("invalid operator")

def evaluate(input):
    inputArr = input.split(" ")
    result = []

    for ex in inputArr:
        if detectOp(ex):
            num1 = int(result.pop())
            num2 = int(result.pop())
            result.append(evalOp(num1, num2, ex))
        else:
            result.append(ex)

    return result


#input = "1 2 * 13 +"
input = "1 2 3 4 + + +"
output = evaluate(input)
print(output)