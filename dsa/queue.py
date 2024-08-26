# Queue - Linear data structure, follows FIFO (First In First Out)

class Queue:
    def __init__(self):
        self.data=[]

    def isEmpty(self):
        return len(self.data) == 0

    def peek(self):
        if (not self.isEmpty()):
            return self.data[0]

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if(not self.isEmpty()):
            self.data.pop(0)

q = Queue();
print("isEmpty -> ", q.isEmpty())
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q.data)
print("isEmpty -> ", q.isEmpty())
print("peek -> ", q.peek())
q.dequeue()
q.dequeue()
print(q.data)