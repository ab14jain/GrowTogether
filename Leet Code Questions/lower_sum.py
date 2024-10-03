class   Solution:
    def solve(self, A):
        lower_sum = [0] * len(A)
        higher_sum = [0] * len(A)

        for i in range(1, len(A)):
            lower_sum[i] = lower_sum[i - 1] + A[i - 1]
        
        for i in range(len(A) - 2, -1, -1):
            higher_sum[i] = higher_sum[i + 1] + A[i + 1]

        print(lower_sum)
        print(higher_sum)

        for i in range(len(A)):
            if lower_sum[i] == higher_sum[i]:
                return i
        return -1

# Test
A = [-7,1,5,2,-4,3,0]
solution = Solution()
print(solution.solve(A))  # 3