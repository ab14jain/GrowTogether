class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        
        n = len(arr)
        NSL = [-1]*n
        NSR = [n]*n
        
        stack = []
        for i in range(n):            
            while stack and arr[stack[-1]] > arr[i]:            
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
            #else:
                # if i == n-1:
                #     NSR[i] = n
            
            stack.append(i)            

        min_sum = 0
        for i in range(n):
            size = (i - NSL[i])*(NSR[i] - i)
            contri = size * arr[i]
            min_sum += contri
        
        return min_sum


s=Solution()
print(s.sumSubarrayMins([3,1,2,4])) # 17
print(s.sumSubarrayMins([71,55,82,55])) # 593
print(s.sumSubarrayMins([11,81,94,43,3])) # 444
print(s.sumSubarrayMins([71,55,82,55,77,34,98,88])) # 1776
print(s.sumSubarrayMins([71,55,82,55,77,34,98,88,88,71,55,82])) # 3772
print(s.sumSubarrayMins([10,10,10,10,10])) # 150
print(s.sumSubarrayMins([72,56,78,54,54,67,67,88,99,99,99,99])) # 5051