#https://www.scaler.com/academy/mentee-dashboard/class/325324/assignment/problems/4129?navref=cl_tt_nv
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        n = len(A)
        low = 1

        for i in range(1, n):
            low = min(low, A[i] - A[i-1])

        high = A[n-1] - A[0]
        ans = 0
        while low <= high:
            mid = low + (high - low)//2
            cows = 1
            curr = A[0]

            for i in range(1, n):
                if A[i] - curr >= mid:
                    cows += 1
                    curr = A[i]

            if cows < B:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1

        return ans

# Time complexity: O(nlogn)
# Space complexity: O(1)

s=Solution()
print(s.solve([5,17,100,11], 2)) # 3
print(s.solve([1, 2, 3, 4, 5], 3)) # 2
# print(s.solve([1, 2, 3, 4, 5], 2)) # 2