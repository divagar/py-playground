class HashTable:
    def __init__(self, count):
        self.items = [None] * count


    def hashFunction(self, item):
        return item % len(self.items)
    
    def add(self, item):
        #compute hash function
        hf = self.hashFunction(item)
        if(hf >= len(self.items)):
            print("Compute hash function is out of index")
        elif (self.items[hf] != None):
            print("Collision detected while computing hash for item", item)
        else:
            self.items[hf] = item

    def show(self):
        print(self.items)


ht = HashTable(10)
ht.show()
ht.add(22)
ht.add(33)
ht.add(10)
ht.add(83)
ht.show()


