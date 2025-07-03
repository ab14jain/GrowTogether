class Solution:
    def totalElements(self, arr):
        # Code here

        n = len(arr)

        dist = set()
        i = 0
        ans = 0
        run_ans = 0
        j = 0
        while i < n:
            
            while i< n and len(dist) <= 2:
                dist.add(arr[i])
                run_ans += 1
                i += 1
                
            
            
            ans = max(ans, run_ans)

            while j < i and len(dist) > 1:
                dist.remove(arr[j])
                j += 1
                run_ans -= 1

        return ans
    
s=Solution()
print(s.totalElements([2,1,2]))
print(s.totalElements([3,1,2,2,2,2]))



