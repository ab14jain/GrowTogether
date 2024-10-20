
#Approach
# 1. Calculate the left sum and right sum of the array
# 2. If left_sum[i] == right_sum[i], return i
# 3. If no such index exists, return -1

class Solution:
    def pivotIndex(self, c: list[int]) -> int:
        n = len(c)
        left_sum = [0]*n
        right_sum = [0]*n

        left_sum[0] = c[0]
        right_sum[n-1] = c[n-1]
        for i in range(1, n):
            left_sum[i] = left_sum[i-1] + c[i]

        for i in range(n-2, -1, -1):
            right_sum[i] = right_sum[i+1] + c[i]               
        

        for i in range(len(c)):
            if left_sum[i] == right_sum[i]:
                return i
        
        
        return -1

s = Solution()
print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
print(s.pivotIndex([1, 2, 3]))
