
def selectionSort(x):
	for i in range(len(x)):
		minIndex = i
		for j in range(i, len(x)-1):
			if(x[minIndex] > x[j+1]):
				minIndex = j+1
		t = x[i]
		x[i] = x[minIndex]
		x[minIndex] = t
		print("after ", i," iteration :", x)
				

x = [25, 24, 64, 2, 35, 1, 3, 0]
print(x)
x = selectionSort(x)
print(x)