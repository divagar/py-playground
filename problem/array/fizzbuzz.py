class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        out = []
        for i in range(1, A+1):
            if(i % 3 == 0 and i % 5 == 0):
                out.append('FizzBuzz')
            elif(i % 3 == 0):
                out.append('Fizz')
            elif(i % 5 == 0):
                out.append('Buzz')
            else:
                out.append(i)
        return out

s = Solution()
out = s.fizzBuzz(10)
print(out)
