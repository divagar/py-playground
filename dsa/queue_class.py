class MyQueue():
	def __init__(self):
		self.myQueue=[];
		self.front=-1;
		self.back=-1
		self.size=5

	def isEmpty(self):
		if(self.front == -1):
			return True;
		else:
			return False;

	def isFull(self):
		if(len(self.myQueue) == self.size):
			return True;
		else:
			return False;

	def enqueue(self, item):
		if(not self.isFull()):
			self.myQueue.append(item);
			self.front = self.front + 1;

	def dequeue(self):
		if(not self.isEmpty()):
			del self.myQueue[self.front]
			self.front = self.front - 1;


q = MyQueue();
print("q -> ", q.myQueue);

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)
print("q -> ", q.myQueue);

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print("q -> ", q.myQueue);

