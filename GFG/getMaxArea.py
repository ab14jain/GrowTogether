#https://www.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1

class Solution:
    def getMaxArea(self,arr):
        #code here

        n = len(arr)
        NSL = [-1]*n
        NSR = [n]*n
        stack = []
        for i in range(n):

            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                NSL[i] = stack[-1]
            
            stack.append(i)

        stack = []
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                NSR[i] = stack[-1]
            
            stack.append(i)

        max_area = float('-inf')
        for i in range(n):
            width = NSR[i]-NSL[i]-1
            area = arr[i]*width

            max_area = max(max_area, area)

        # print(NSR)
        # print(NSL)
        return max_area

s=Solution()
print(s.getMaxArea([60,20,50,40,10,50,60]))