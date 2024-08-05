#simple implementation of linkedlist in python

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,):
        self.head = None

    def addAtTheLast(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = newNode

    def addAtTheBeginning(self, newValue):
        newNode = Node(newValue)
        newNode.next = self.head
        self.head = newNode

    def delete(self, value):
        if self.head == None:
            print("No item available to remove")
        else:
            current = self.head
            while current.next != None and current.next.value != value:
                current = current.next

            if(current.next != None):
                current.next = current.next.next

    def deleteFromBeginning(self):
        if self.head == None:
            print("No item available to remove")
        else:
            current = self.head
            if current.next == None:
                self.head = None
            else:
                self.head = current.next

    def deleteFromEnd(self):
        if self.head == None:
            print("No item available to remove")
        elif self.head.next == None:
            self.head = None
        else:
            current = self.head
            while current.next != None and current.next.next != None:
                current = current.next
            current.next = None

    def show(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

ll = LinkedList()
ll.addAtTheLast("How")
ll.addAtTheLast("are")
ll.addAtTheLast("doing ?")
ll.show()

ll.addAtTheBeginning("Divagar")
ll.addAtTheBeginning("Hi")
ll.show()

ll.delete("hhh")

ll.deleteFromEnd()
ll.deleteFromEnd()
ll.deleteFromEnd()
ll.deleteFromEnd()
ll.deleteFromEnd()
ll.show()