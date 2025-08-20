from math import ceil


class Solution:
    def minSoldiers(self, arr, k):
        # code here

        n = len(arr)
        req = ceil(n/2)
        multiple_k = 0
        min_req = [0]*n
        for i in range(n):

            if arr[i] % k != 0:
                min_req[i] = k*ceil(arr[i]/k) - arr[i]

        min_req.sort()

        for i in range(req):
            multiple_k += min_req[i]
        
        return multiple_k

s=Solution()
print(s.minSoldiers([5,6,3,2,1], 2))
print(s.minSoldiers([3,5,6,7,9,10], 4))