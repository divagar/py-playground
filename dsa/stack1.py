from cProfile import run


def createStack():
	myStack=[]
	return myStack

def isEmpty(stack):
	if(len(stack) == 0):
		return 0
	else:
		return 1

def push(stack, item):
	stack.append(item)

def pop(stack):
	if(isEmpty(stack)!=0):
		stack.pop()


myStack = createStack();
print("myStack -> ", myStack)

push(myStack, 10);
push(myStack, 20);
push(myStack, 30);
push(myStack, 40);
push(myStack, 50);
print("myStack -> ", myStack)

pop(myStack)
print("myStack -> ", myStack)