
def insertionSort(x):
	for i in range(1, len(x)):
		key = x[i]
		j = i-1
		while j >= 0 and key < x[j]:
			x[j+1] = x[j]
			j = j-1
		x[j+1] = key
		print("after ", i, " iteration:", x)
				

x = [24, 14, 53, 12 , 5, 15, 463, 0 , 25, 1]
print(x)
insertionSort(x)
print(x)