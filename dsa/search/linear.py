def linearSearch(data, key):
	for i in range(len(data)):
		if data[i] == key:
			return i
	return -1

data = [35, 355, 2, 16, 68, 27, 88, 20]
key = 68
print("Data ->", data)
print("Key ->", key)
ret = linearSearch(data, key)
if(ret == -1):
	print("Element not found !")
else:
	print("Element found in index ", ret)