def heapify(data, size, h):
	#print("data ->", data)
	#print("size ->", size)
	#print("h ->", h)

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

def insert(data, x):
	size = len(data)
	if(size == 0):
		data.append(x)
	else:
		data.append(x)
		for i in range(size//2-1, -1, -1):
			heapify(data, size, i)

def remove(data, x):
	size = len(data)
	i = 0
	for i in range(0, size):
		if x == data[i]:
			break

	if(i != 0):
		t = data[i]
		data[i] = data[size-1]
		data[size-1] = t
		data.remove(x)
	
	for j in range(len(data)//2-1, -1, -1):
		heapify(data, len(data), j)

data = [24, 5, 15, 10, 33, 19, 4]
print("Data -> ", data)
print("Heapify...")
heapify(data, len(data), len(data)//2-1)
print("Data -> ", data)

print("------")
data = []
insert(data, 24)
insert(data, 2)
insert(data, 63)
insert(data, 89)
insert(data, 90)
insert(data, 13)
print("Data -> ", data)

print("------")
remove(data, 89)
print("Data -> ", data)
