def isPrime(x):
	if(x == 0 or x == 1):
		return 0
	for i in range(2, x//2):
		if(x%i == 0):
			return 0
	return 1

def getPrime(x):
	if(x % 2 == 0):
		x = x + 1
	while(not isPrime(x)):
		x = x + 2
	return x

def hashFunction(key):
	pn = getPrime(10)
	return pn % key

def insertHash(key, value):
	index = hashFunction(key)
	hashMap[index] = [key, value]

def removeHash(key):
	index = hashFunction(key)
	hashMap[index] = []

hashMap = [[],] * 10

print("Hashmap Before->", hashMap)
insertHash(10, "hello")
insertHash(1, "hello world")
insertHash(2, "hoddy world")
print("Hashmap After->>", hashMap)

removeHash(4)
print("Hashmap After->>", hashMap)