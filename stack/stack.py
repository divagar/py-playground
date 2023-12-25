class Stack:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        return str(self.items)
    
    def size(self):
        print("size ", len(self.items))

    def isEmpty(self):
        print("is empty ? ", len(self.items) == 0)
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print("Item pushed ", item)

    def pop(self):
        if (not self.isEmpty()):
            item = self.items.pop()
            print("Item popped ", item)
            return item
        else:
            print("Stack is empty !")

    def peek(self):
        if (not self.isEmpty()):
            item = self.items[-1]
            print("Item peeked ", item)
            return item
        else:
            print("Stack is empty !")

if __name__ == "__main__":
    mystack = Stack();
    mystack.size()
    mystack.push(10)
    mystack.push(20)
    mystack.push(30)
    mystack.pop()
    mystack.peek()
    mystack.size()
    mystack.isEmpty()
    print(mystack)
