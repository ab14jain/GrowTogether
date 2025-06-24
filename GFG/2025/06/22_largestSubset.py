class Solution:
    def largestSubset(self, arr):
        #code here

        # def isValid(subset):
        #     n = len(subset)
        #     for i in range(n):
        #         for j in range(i+1, n):
        #             if subset[i] % subset[j] != 0 and subset[j] % subset[i] != 0:
        #                 return False
            
        #     return True

        # def isLexGreater(a, b):            
        #     for i in range(len(a)):
        #         if a[i] != b[i]:
        #             return a[i] > b[i]
        #     return False              

    
        # def dfs(arr, curr, index, res):

        #     if index >= len(arr):

        #         if isValid(curr):
        #             if len(curr) > len(res[0]):
        #                 res[0] = curr.copy()
        #             elif len(curr) == len(res[0]) and isLexGreater(curr, res[0]):
        #                 res[0] = curr.copy()
                    
        #         return

        #     curr.append(arr[index])
        #     include = dfs(arr,curr,index+1,res)
            
        #     curr.pop()
        #     exclude = dfs(arr,curr,index+1,res)

        # arr.sort()
        # res = [[]]
        # dfs(arr,[],0,res)
        # return res[0]

        # def lds(res, curr, i, prev, arr):
        #     # Base case: check if we've reached the
        #     # end of the array
        #     if i >= len(arr):
        #         # Update res if the current subset is 
        #         # larger or if it's the same size but lexicographically greater
        #         if len(curr) > len(res) or (len(curr) == len(res) and curr > res):
        #             res[:] = curr[:]
        #         return

        #     # Include current element if divisible by
        #     # previous element
        #     if not curr or arr[i] % prev == 0:
        #         curr.append(arr[i])

        #         # Recur with the current number included
        #         lds(res, curr, i + 1, arr[i], arr)

        #         # Backtrack to explore other possibilities
        #         curr.pop()

        #     # Exclude current element and move to the next
        #     # Recur without including the current number
        #     lds(res, curr, i + 1, prev, arr)

        # arr.sort()
        # res = []
        # curr = []

        # # Start the recursive search
        # lds(res, curr, 0, 1, arr)
        # return res

        def lds(arr, memo, parent, i):
            # If this subproblem has already been solved, return the result
            if memo[i] != -1:
                return memo[i]
        
            maxLength = 1
            bestParent = -1
        
            # Try to include arr[i] in the subset by checking all j < i
            for j in range(i):
                # Adjusted for descending order
                if arr[j] % arr[i] == 0:  
                    length = lds(arr, memo, parent, j) + 1
                    if length > maxLength:
                        maxLength = length
                        bestParent = j
        
            # Store the result for memoization and backtracking
            memo[i] = maxLength
            parent[i] = bestParent
            return maxLength

        n = len(arr)
    
        # Sort in descending order
        arr.sort(reverse=True)
        
        # Memoization array
        memo = [-1] * n      
        # Backtracking parent array
        parent = [-1] * n    
    
        maxSize = 0
        lastIndex = 0
    
        # Try to find the largest subset size for each index
        for i in range(n):
            size = lds(arr, memo, parent, i)
            if size > maxSize:
                maxSize = size
                lastIndex = i
    
        # Backtrack to construct the result
        res = []
        while lastIndex != -1:
            res.append(arr[lastIndex])
            lastIndex = parent[lastIndex]
    
        # Already in descending order due to backtracking
        return res

        
        

s=Solution()
print(s.largestSubset([1, 16, 7, 8, 4]))
print(s.largestSubset([1, 16, 7, 8, 4, 14, 21, 28]))
print(s.largestSubset([2,4,3,8]))
