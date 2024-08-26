class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self, key):
        print("   ( Insert at start )   ")
        if self.head is None:
            self.head = Node(key)
        else:
            n = self.head
            self.head = Node(key)
            n.prev = self.head
            self.head.next = n

    def insertAtEnd(self, key):
        print("   ( Insert at end )   ")
        if self.head is None:
            self.head = Node(key)
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            n = Node(key)
            n.prev = t
            t.next = n

    def insertAt(self, pos, key):
        print("   ( Insert at position )   ")
        if self.head is None:
            self.insertAtStart(key)
        elif (pos == 0):
            self.insertAtStart(key)
        else:
            index = 0
            c = self.head
            while c is not None:
                if index == pos:
                    p = c.prev
                    n = Node(key)
                    n.next = p.next
                    p.next = n
                    n.prev = p.prev
                    break
                else:
                    c = c.next
                    index += 1

    def delete(self, key):
        print("   ( Delete key )   ")
        if self.head is None:
            return
        else:
            c = self.head
            while c is not None:
                if c.data == key:
                    p = c.prev
                    n = c.next
                    p.next = n
                    n.prev = p
                    break
                else:
                    c = c.next

    def traversalRight(self):
        print("\n   ( Traversal Right )   ")
        t = self.head
        while t is not None:
            print(t.data)
            t = t.next

    def traversalLeft(self):
        print("\n   ( Traversal Left )   ")
        t = self.head
        while t.next is not None:
            t = t.next

        while t is not None:
            print(t.data)
            t = t.prev


ll = LinkedList()
ll.insertAtStart(10)
ll.insertAtEnd(11)
ll.insertAtEnd(12)
ll.insertAtEnd(13)
ll.insertAtEnd(14)
ll.insertAtEnd(15)
ll.insertAtStart(0)
ll.insertAt(2, 22)
ll.delete(13)

ll.traversalRight()
ll.traversalLeft()
