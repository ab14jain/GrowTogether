class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:        
        n = len(arr)

        for i in range(n-m):
            pat = "".join(map(str,arr[i:m+i]))
            pCount = "".join(map(str,arr)).count(pat)
            # print(pat, pCount)
            if pCount >= k:
                return True
        
        return False
    

s= Solution()
print(s.containsPattern([1,2,4,4,4,4], 1, 3)) # True
print(s.containsPattern([1,2,1,2,1,1,1,3], 2, 2)) # True
print(s.containsPattern([1,2,1,2,1,3], 2, 3)) # False
print(s.containsPattern([1,2,3,1,2], 2, 2)) # False
print(s.containsPattern([2,2,2,2], 2, 3)) # False
