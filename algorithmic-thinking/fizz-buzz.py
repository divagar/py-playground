class Solution:
    def computeFizzBuzz(self, i):
        if(not i%3 and not i%5):
            return "FizzBuzz"
        elif(not i%5):
            return "Buzz"
        elif(not i%3):
            return "Fizz"
        else:
            return i
        
    def fizzBuzz(self, n):
        out = []
        for i in n:
            out.append(self.computeFizzBuzz(i))
        return out


x = [1,2,3,4,5,6,7,8,9,10,15]
s = Solution()
y = s.fizzBuzz(x)
print(y)
