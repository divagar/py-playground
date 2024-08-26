class Node:
    def __init__(self, data):
        self.item = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self, key):
        n = Node(key)
        n.next = self.head
        self.head = n

    def insertAtEnd(self, key):
        if self.head is None:
            self.head = Node(key)
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = Node(key)

    def traversal(self):
        n = self.head
        while n is not None:
            print(n.item)
            n = n.next

    def search(self, key):
        n = self.head
        while n is not None:
            if n.item == key:
                return True
            n = n.next
        return False

    def delete(self, pos):
        index = 0
        p = self.head
        c = self.head
        n = self.head

        if self.head is None:
            return
        if pos == 0:
            self.head = self.head.next
            return self.head

        while c is not None:
            print("c", c.item)
            if index == pos:
                p.next = c.next
                return p
            p = c
            c = c.next
            index += 1

myLinkedList = LinkedList()
myLinkedList.insertAtEnd(11)
myLinkedList.insertAtEnd(22)
myLinkedList.insertAtEnd(33)
myLinkedList.insertAtEnd(44)

print("( Traversal )")
myLinkedList.traversal()

print("( search )")
s = myLinkedList.search(33)
if(s):
    print("Search element is found")
else:
    print("Search element not found")

print("( Insert at start )")
myLinkedList.insertAtStart(1)

print("( Traversal )")
myLinkedList.traversal()

print("( Insert at end )")
myLinkedList.insertAtEnd(55)

print("( Traversal )")
myLinkedList.traversal()

print("( Delete )")
myLinkedList.delete(5)

print("( Traversal )")
myLinkedList.traversal()
