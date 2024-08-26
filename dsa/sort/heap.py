def heapify(data, size, h):
	largest = h
	left = 2 * h + 1
	right = 2 * h + 2

	if (left < size and data[left] > data[largest]):
		largest = left
	if (right < size and data[right] > data[largest]):
		largest = right

	if (largest != h):
		t = data[largest]
		data[largest] = data[h]
		data[h] = t
		heapify(data, size, largest)


def heapSort(data):
	size = len(data)

	#find max heap
	print("data -> ", data)
	for i in range(size//2, -1, -1):
		heapify(data, size, i)
	print("max heap data -> ", data)

	#swap
	for i in range(size-1, 0, -1):
		t = data[i]
		data[i] = data[0]
		data[0] = t
		heapify(data, size, i)

x = [14, 24, 42, 1, 2, 52, 0]
print(x)
print("Heap Sort")
heapSort(x)
print(x)
