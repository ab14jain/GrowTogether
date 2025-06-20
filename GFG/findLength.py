#User function Template for python3
class Solution:
    def findLength(self, color, radius):
        
        #[2,2,5]
        #[3,3,5]
        n = len(color)
        stack = []

        for i in range(n):
            currC = color[i]
            currR = radius[i]
            
            if stack and stack[-1][0] == currC and stack[-1][1] == currR:
                
                stack.pop()                 
            else:
                stack.append([color[i], radius[i]])

        return len(stack)
        # mp = {}
        # count = 0
        # for i in range(n):
        #     if (color[i], radius[i]) in mp:
        #         mp[(color[i], radius[i])] += 1
        #     else:
        #         mp[(color[i], radius[i])] = 1

        # for key in mp:
        #     count += mp[key]%2

        # return count


s=Solution()
print(s.findLength([1, 2, 2, 1], [1, 2, 2, 1]))
print(s.findLength([2,3,5], [3,3,5]))
print(s.findLength([2,2,5], [3,3,5]))
print(s.findLength([2,2,2], [3,3,3]))