# Stack - Linear datastructure, follows LIFO (Last In First Out)

class Stack():
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)
        return self.data

    def pop(self):
        if(len(self.data) != 0):
            self.data.pop()
            return self.data
        else:
            None

    def isEmpty(self):
        return len(self.data) == 0

    def peek(self):
        if(len(self.data) != 0):
            return self.data[len(self.data)-1]
        else:
            None


s = Stack()
print(s.peek())
print(s.isEmpty())
print(s.push(10))
print(s.push(20))
print(s.push(21))
print(s.pop())
print(s.isEmpty())
print(s.peek())
