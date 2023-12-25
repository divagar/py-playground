import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def put(self, priority, item):
        heapq.heappush(self.items, (priority, item))

    def get(self):
        return heapq.heappop(self.items)
    
    def __str__(self):
        return str(self.items)
    

pq = PriorityQueue()
print(pq)

pq.put(5, "a")
pq.put(3, "c")
pq.put(6, "d")
pq.put(1, "t")
print(pq)

print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq)