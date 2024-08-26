class MedianFinder(object):

    def __init__(self):
        self.nums = []

    def addNum(self, num):
        self.nums.append(num)

    def isEven(self):
        if(len(self.nums) % 2 == 0):
            return True
        else:
            return False

    def totalElements(self):
        total = 0
        for i in range(len(self.nums)):
            total += self.nums[i]
        return total

    def findMidElement(self):
        return (len(self.nums)//2)

    def findMedian(self):
        if len(self.nums) == 0:
            return 0

        median = 0
        if(self.isEven()):
            total = self.totalElements()
            print("total -> ", total)
            print("nums -> ", self.nums)
            median = total / len(self.nums)
        else:
            midpoint = self.findMidElement()
            median = self.nums[midpoint]
        return median


medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian())

