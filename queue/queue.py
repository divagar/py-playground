from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is empty !")
        else:
            return self.items.popleft()
    
    def peek(self):
        if(self.isEmpty()):
            print("Queue is empty !")
        else:
            return self.items[0]
    
    def __str__(self):
        return str(self.items)
    

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q)
print(q.size())
print(q.peek())
q.dequeue()
print(q)
q.dequeue()
q.dequeue()
q.dequeue()