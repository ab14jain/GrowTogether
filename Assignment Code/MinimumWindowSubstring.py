from collections import Counter


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):

        A_map = {}
        B_map = Counter(B)
        l = 0
        r = 0 
        min_len = float('inf')
        m = len(A)
        ans = ""

        def comp_map(superset, subset):
            for key in subset:
                value = subset[key]
                if key not in superset or superset[key] < value:
                    return False
            
            return True

        while r < m and l <= r:           

            if A[r] in A_map:
                A_map[A[r]] += 1
            else:
                A_map[A[r]] = 1

            while comp_map(A_map, B_map):                
                if min_len > r-l+1:
                    min_len = r-l+1
                    ans = A[l:r+1]
                A_map[A[l]] -= 1    
                l += 1 

            r += 1

        return ans
    
s=Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
