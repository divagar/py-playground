class MySimpleQueue:
	
	def __init__(self):
		self.size = 5
		self.myQueue = [None] * self.size
		self.front = -1
		self.back = -1

	def show(self):
		print("myQueue -> ", self.myQueue)

	def isEmpty(self):
		return self.front == -1 and self.back == -1

	def isFull(self):
		return (self.back == self.size-1)

	def enqueue(self, item):
		if(self.isFull()):
			print("queue is full.")
		elif(self.isEmpty()):
			self.front = 0
			self.back = 0
			self.myQueue[0] = item
		else:
			self.back = self.back + 1
			self.myQueue[self.back] = item
	
	def dequeue(self):
		if(self.isEmpty()):
			print("queue is empty.")
		else:
			self.myQueue[self.front] = None
			self.front = self.front + 1


q = MySimpleQueue()
q.show()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.show()

q.dequeue()
q.dequeue()
q.dequeue()
q.show()
			