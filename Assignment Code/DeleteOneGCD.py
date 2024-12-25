import math


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        # gcd = 0
        # max_gcd = 0
        # n = len(A)
        # for i in range(n):
        #     gcd = math.gcd(gcd, A[i])

        # max_gcd = max(max_gcd, gcd)

        # i = 0        
        # while i < n:
        #     gcd = 0
        #     for j in range(n):
        #         if j == i:
        #             continue
        #         gcd = math.gcd(gcd, A[j])
            
        #     max_gcd = max(max_gcd, gcd)
        #     i += 1
        
        # return max_gcd

        max_gcd = 0
        n = len(A)

        prefix_gcd = [0] * n
        suffix_gcd = [0] * n

        prefix_gcd[0] = A[0]
        suffix_gcd[n-1] = A[n-1]

        for i in range(1, n):
            prefix_gcd[i] = math.gcd(prefix_gcd[i-1], A[i])
        
        for i in range(n-2, -1, -1):
            suffix_gcd[i] = math.gcd(suffix_gcd[i+1], A[i])

        
        for i in range(n):
            if i == 0:
                max_gcd = max(max_gcd, suffix_gcd[i+1])
            elif i == n-1:
                max_gcd = max(max_gcd, prefix_gcd[i-1])
            else:
                max_gcd = max(max_gcd, math.gcd(prefix_gcd[i-1], suffix_gcd[i+1]))

        return max_gcd

            


s = Solution()

print(s.solve([2, 4, 6, 8, 10])) # Output: 2
print(s.solve([3,9,6,8,3])) # Output: 3
print(s.solve([12, 15, 18])) # Output: 6