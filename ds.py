# List - ordered sequence of items
print("-- List --")
myList = ['apple', 'blackberry', 'orange']
print(myList, type(myList))
myList.append("grapes")
myList[1] = "blueberry"
print(myList)
print(myList[0:])
print(len(myList))

# Tuple - ordered sequence of items, but immutable once created
print("-- Tuple --")
myTuple = ("apple", "orange", "grapes")
print(myTuple, type(myTuple))
print(myTuple[0:])
print(len(myTuple))


# Set - unordered unique items
print("-- Set --")
mySet = {"apple", "orange", "grapes", "apple"}
print(mySet, type(mySet))
print(len(mySet))

# Dictionary - unordered collection of key value pair
print("-- Dictionary --")
myDict = {1: "apple", 2: "orange", 3: "grapes", 4: "blueberry"}
myDict[6] = "blackberry"
print(myDict, type(myDict))
print(len(myDict))
print(myDict[3])
