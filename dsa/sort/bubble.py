
def bubbleSort(x):
	for i in range(len(x)):
		for j in range(0, len(x)-i-1):
			if(x[j] > x[j+1]):
				t = x[j]
				x[j] = x[j+1]
				x[j+1] = t
	return x

x = [14, 24, 42, 1, 2, 52, 0]
print(x)
print("Bubble Sort")
bubbleSort(x)
print(x)