from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        n = len(arr)
        arr_set = set(arr)        
        max_count = 0
        for i in range(n-1):
            for j in range(i+1, n):
                first = arr[i]
                second = arr[j]
                third = first + second
                count = 2               
                while third in arr_set:                    
                    first = second
                    second = third
                    third = first + second
                    count += 1
                    max_count = max(max_count, count)     
        
        return max_count
    
    
s=Solution()
print(s.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
print(s.lenLongestFibSubseq([1,3,7,11,12,14,18]))
print(s.lenLongestFibSubseq([1,3,6]))
            



