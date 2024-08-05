#Given an integer num, return the number of steps to reduce it to zero.
#In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

# class Solution:
#     def isEven(self, num):
#         if(not num%2):
#             return True
#         else:
#             return False
    
#     def numberOfSteps(self, num):
#         step = 0
#         while num != 0:
#             if(self.isEven(num)):
#                 num = num / 2
#             else:
#                 num = num -1
#             step += 1
#         return step
        

# x = 123
# s = Solution()
# y = s.numberOfSteps(x)
# print(y)

class Solution:
    
    def numberOfSteps(self, num):
        step = 0
        bitMask = 1
        while num != 0:
            if(num & bitMask):
                num -= 1
            else:
                num /= 2
            step += 1
        return step
        

x = 123
s = Solution()
y = s.numberOfSteps(x)
print(y)

