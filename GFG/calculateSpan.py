#https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1
class Solution:
    def calculateSpan(self, arr):
        #write code here

        n = len(arr)
        NSL = [1]*n

        stack = []
        
        for i in range(n):
           
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
                
            if stack:
                NSL[i] = i - stack[-1]
            else:
                NSL[i] = i + 1

            stack.append(i)
            

        return NSL
    

s=Solution()
print(s.calculateSpan([100, 80, 60, 70, 60, 75, 85]))
print(s.calculateSpan([10, 4, 5, 90, 120, 80]))