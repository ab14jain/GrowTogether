#https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here

        n = len(arr)
        NGR = [-1]*n

        stack = []
        for i in range(n-1, -1, -1):

            while stack and stack[-1] <= arr[i]:
                stack.pop()

            if stack:
                NGR[i] = stack[-1]
            
            stack.append(arr[i])

        return NGR
    
s=Solution()
print(s.nextLargerElement([1,3,2,4]))
print(s.nextLargerElement([6,8,0,1,3]))
print(s.nextLargerElement([6,8,8,1,3]))
print(s.nextLargerElement([10,20,30,50]))
print(s.nextLargerElement([50,40,30,10]))