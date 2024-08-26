class CircularQueue:
    def __init__(self, size=5):
        self.size = size
        self.data = [None] * self.size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if(self.isFull()):
            print("Queue is full !")
        elif(self.isEmpty()):
            self.data[0] = item
            self.front = 0
            self.rear = 0
            print("q font, rear -> ", self.front, self.rear)
            print(self.data)
        else:
            self.rear = (self.rear + 1) % self.size
            self.data[self.rear] = item
            print("q font, rear -> ", self.front, self.rear)
            print(self.data)

    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is empty !")
        elif(self.front == self.rear):
            self.data[self.front] = None
            self.front = -1
            self.rear = -1
            print("de font, rear -> ", self.front, self.rear)
            print(self.data)
        else:
            self.data[self.front] = None
            self.front = (self.front + 1) % self.size
            print("de font, rear -> ", self.front, self.rear)
            print(self.data)


cq = CircularQueue(3)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.enqueue(101)
cq.enqueue(201)
cq.enqueue(301)
cq.enqueue(401)
cq.dequeue()
cq.dequeue()
cq.enqueue(401)
cq.dequeue()
cq.dequeue()
