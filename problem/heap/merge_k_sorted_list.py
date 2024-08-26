class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def traverse(node, list=[]):
    if node is None:
        return list

    if node is not None:
        list.append(node.val)
        traverse(node.next, list)
    return list


def sortList(inputList):
    cList = []
    sList = []

    if(len(inputList) == 0):
        return []

    for n in inputList:
        cList += traverse(n, [])
    print(cList)

    sList = sorted(cList)
    print(sList)

    retList = Node(sList[0])
    node = retList
    for i in range(1, len(sList)):
        node.next = Node(sList[i])
        node = node.next
    return retList


# [[1,4,5],[1,3,4],[2,6]]
n1 = Node(1)
n1.next = Node(4)
n1.next.next = Node(5)

n2 = Node(1)
n2.next = Node(3)
n2.next.next = Node(4)

n3 = Node(2)
n3.next = Node(6)

inputList = [n1, n2, n3]
sortList(inputList)
