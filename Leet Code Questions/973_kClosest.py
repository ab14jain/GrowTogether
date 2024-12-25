from functools import cmp_to_key


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # def distant_sort(a,b):  
        #     d1 = ((a[0])**2 + (a[1])**2)**.5
        #     d2 = ((b[0])**2 + (b[1])**2)**.5

        #     if d1 < d2:
        #         return -1
        #     elif d1 > d2:
        #         return 1
        #     else:
        #         return 0
        
        # points.sort(key=cmp_to_key(distant_sort))

        # result = points[0:k]

        # return result

        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]
    

s=Solution()
print(s.kClosest([[1,3],[-2,2]],1)) # [[-2,2]]
print(s.kClosest([[3,3],[5,-1],[-2,4]],2)) # [[3,3],[-2,4]]
print(s.kClosest([[1,3],[-2,2],[2,-2]],2)) # [[-2,2],[2,-2]]