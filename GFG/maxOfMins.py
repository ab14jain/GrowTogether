class Solution:
    def maxOfMins(self, arr):
       # code here
        # Brute Force
        # Time Complexity: O(n^3)

        # n = len(arr)
        # ans = []
        # for i in range(n):
        #     temp = []
        #     min_val = float('inf')
        #     for j in range(n-i):                
        #         min_val = min(arr[j:j+i+1])
        #         temp.append(min_val)            
        #     ans.append(max(temp))

        # return ans

       
        n = len(arr)
        max_of_mins_ans = [0] * n
        stack = []        
        k_size_arr = [0] * n
        
        for i in range(n):  
            while stack and arr[stack[-1]] >= arr[i]:
                top = stack.pop()
                windowSize = i if not stack else i - stack[-1] - 1
                k_size_arr[top] = windowSize
            stack.append(i)
       
        while stack:
            top = stack.pop()
            windowSize = n if not stack else n - stack[-1] - 1
            k_size_arr[top] = windowSize

       
        for i in range(n):
            windowSize = k_size_arr[i] - 1  
            max_of_mins_ans[windowSize] = max(max_of_mins_ans[windowSize], arr[i])

        
        for i in range(n - 2, -1, -1):
            max_of_mins_ans[i] = max(max_of_mins_ans[i], max_of_mins_ans[i + 1])

        return max_of_mins_ans

s=Solution()
print(s.maxOfMins([10, 20, 30, 50, 10, 70, 30]))
print(s.maxOfMins([10, 20, 30]))