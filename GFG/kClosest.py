from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Your code here

        arr = []
        for p in points:
            x = p[0]
            y = p[1]
            arr.append([[x,y],[x*x+y*y]])
        
        arr.sort(key=lambda x:x[1])

        res = []

        for i in range(k):
            res.append(arr[i][0])
        return res
    
s=Solution()
print(s.kClosest([[1, 3], [-2, 2], [5, 8], [0, 1]], 2))