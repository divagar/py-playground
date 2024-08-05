#Design a class to efficiently find the Kth largest element in a stream of numbers. The class should have the following two things:​

#The constructor of the class should accept an integer array containing initial numbers from the stream and an integer K.

#The class should expose a function add(int num) which will store the given number and return the Kth largest number.
from heapq import *

class findKlargestNumber:
    minHeap = []

    def __init__(self, nums, k):
        for n in nums:
            self.add(n)

    def add(self, n):
        heappush(self.minHeap, n)