class Solution:
    def maximumWealth(self, accounts):
        out = []
        for x in accounts:
            acc = 0
            for y in x:
                acc += y
            out.append(acc)
        sortedOut = sorted(out)
        return sortedOut[-1]
        
x = [[1,2],[3,4],[5,6],[3,1]]
s = Solution()
y = s.maximumWealth(x)
print(y)
