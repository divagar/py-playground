class MyStack():

	def __init__(self):
		self.myStack = []
	
	def push(self, item):
		self.myStack.append(item)

	def pop(self):
		self.myStack.pop()
	
	def show(self):
		print("Data -> ", self.myStack)


s = MyStack()
s.show()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.show()

s.pop()
s.pop()
s.show()