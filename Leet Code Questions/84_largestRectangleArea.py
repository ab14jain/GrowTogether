class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        n = len(heights)
        NSL = [-1]*n
        NSR = [n]*n
        mod = 1000000007
        stack = []
        for i in range(n):            
            while stack and heights[stack[-1]] > heights[i]:            
                stack.pop()            
            if stack:
                NSL[i] = stack[-1]
            stack.append(i)   

        stack = []
        for i in range(n-1,-1,-1):            
            while stack and heights[stack[-1]] >= heights[i]:            
                stack.pop()

            if stack:
                NSR[i] = stack[-1]
            
            stack.append(i)            

        area_max = 0
        for i in range(n):            
            area_max = max(area_max, (NSR[i] - NSL[i] - 1) * heights[i])
            
        
        return area_max
    
s=Solution()
print(s.largestRectangleArea([2,1,5,6,2,3])) # 10
print(s.largestRectangleArea([2,4])) # 4
print(s.largestRectangleArea([2,1,2])) # 3
print(s.largestRectangleArea([1,2,2])) # 4
print(s.largestRectangleArea([2,1,5,6,2,3,2,3,4,6,5,6,6])) # 4

        