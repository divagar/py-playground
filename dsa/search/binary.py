def binarySearch(data, key, low, high):
	if high >= low:
		mid = low + (high-low)//2
		if key == data[mid]:
			return mid
		elif key > data[mid]:
			return binarySearch(data, key, mid+1, high)
		elif key < data[mid]:
			return binarySearch(data, key, low, mid-1)
	else:
		return -1

data = [35, 45, 50, 53, 60, 69, 87, 90]
key = 45
print("Data ->", data)
print("Key ->", key)
ret = binarySearch(data, key, 0, len(data)-1)
if(ret == -1):
	print("Element not found !")
else:
	print("Element found in index ", ret)