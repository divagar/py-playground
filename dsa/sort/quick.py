
def partition(data, low, high):
	# take the right most a pivot element
	pivot = data[high]

	# index of greated elm
	i = low - 1

	for j in range(low, high):
		if(data[j] <= pivot):
			i +=1
			t = data[i]
			data[i] = data[j]
			data[j] = t
	t = data[i+1]
	data[i+1] = data[high]
	data[high] = t

	return i + 1
			
	

def quickSort(data, low, high):
	if(low < high):
		# find pivot element
		pi = partition(data, low, high)

		# sort left side of pivot
		quickSort(data, low, pi-1)
	
		# sort right side of pivot
		quickSort(data, pi+1, high)
	

data = [24, 36, 11, 25, 47, 1, 36, 2, 38, 0, 65]
print(data)
print("Quick sort")
quickSort(data, 0, len(data)-1)
print(data)