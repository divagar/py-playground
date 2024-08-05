class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def addToTheEnd(self, value):
        print("Going to insert ", value)
        print("Going to insert ", self.head)
        newNode = Node(value)
        if(self.head == None):
            self.head = newNode
            return
        
        current = self.head
        while current != None and current.next != None:
            current = current.next
        current.next = newNode

    def show(self):
        current = self.head
        if(self.head.next == None):
            print(self.head.value)
        while current != None and current.next != None:
            print(current.value)
            current = current.next


class Hashtable:
    def __init__(self, count):
        self.items = [None] * count

    def hashFunction(self, item):
        return item % len(self.items)
    
    def add(self, item):
        hf = self.hashFunction(item)
        
        if hf >= len(self.items):
            print("Computed hash function out of bound")
            return
        
        if self.items[hf] != None:
            print("collision detected")
            ll = self.items[hf]
            ll.addToTheEnd(item)
            self.items[hf] = ll
            return
        
        #insert item to hash map
        ll = Linkedlist()
        ll.addToTheEnd(item)
        self.items[hf] = ll

    def handleCollision(self, index):
        None

    def show(self):
        for i, item in enumerate(self.items):
            if(item != None):
                ll = item
                print("\nIndex ", i)
                ll.show()

hashTable = Hashtable(15)
hashTable.add(10)
hashTable.add(16)
hashTable.add(20)
hashTable.add(30)
hashTable.add(60)
hashTable.show()
