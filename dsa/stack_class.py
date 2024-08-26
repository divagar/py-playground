class MyStack():

	def __init__(self):
		self.myStack=[]

	def isEmpty(self):
		if(len(self.myStack) == 0):
			return 0;
		else:
			return 1;

	def push(self, item):
		self.myStack.append(item);

	def pop(self):
		if(self.isEmpty() != 0):
			self.myStack.pop()


obj = MyStack();
print("s -> ", obj.myStack)
obj.push(10);
obj.push(20);
obj.push(30);
print("s -> ", obj.myStack)
obj.pop()
print("s -> ", obj.myStack)