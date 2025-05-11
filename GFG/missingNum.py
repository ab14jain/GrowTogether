class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr)
        sum_t = sum(arr)
        return (((n+2)*(n+1))//2) - sum_t
    
s=Solution()
print(s.missingNum([1,2,3,5]))
print(s.missingNum([8,2,4,5,3,7,1]))
print(s.missingNum([1]))