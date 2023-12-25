import stack

s = stack.Stack();
str = "ereh ragavid"
reversedStr = ""

for char in str:
    s.push(char)

print(s)

while not s.isEmpty():
    reversedStr += s.pop()

print(reversedStr)

