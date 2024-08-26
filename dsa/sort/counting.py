
def countingSort(data):
	countArr = storeCount(data)

	cCountArr = cummulativeCount(countArr)

	out = [0] * len(data)
	for i in range(len(data)):
		count = cCountArr[data[i]]
		out[count-1] = data[i]
	return out
	
def storeCount(data):
	max = findMax(data)
	countArr = [0] * (max+1)
	for i in range(len(data)):
		countArr[data[i]] += 1
	return countArr

def cummulativeCount(data):
	for i in range(1, len(data)):
		data[i] += data[i-1]
	return data

def findMax(data):
	max = None
	for i in range(len(data)-1):
		if(data[i] > data[i+1]):
			max = data[i]
	return max	

data = [35, 21, 25, 1, 5, 63, 0, 14]
print(data)
print("Counting Sort")
out = countingSort(data)
print(out)