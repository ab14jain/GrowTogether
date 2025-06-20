class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        i = 1

        def count(curr):
            res = 0
            nbr = curr+1


            while curr <=n:
                res += min(nbr, n+1) - curr
                curr *= 10
                nbr *= 10

            return res
        
        while i < k:
            steps = count(curr)
            if i +steps <= k:
                curr = curr + 1
                i += steps
            else:
                curr *= 10
                i += 1
            
        return curr
    
s=Solution()
print(s.findKthNumber(13, 2))
print(s.findKthNumber(1, 1))