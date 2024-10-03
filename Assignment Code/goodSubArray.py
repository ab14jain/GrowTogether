class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        count_good_array = 0
        n = len(A)

        for i in range(n):
            sum_a = 0

            for j in range(i, n):
                sum_a += A[j]

                len_a = j - i + 1

                if len_a % 2 == 0 and sum_a < B:
                    count_good_array += 1
                
                if len_a % 2 != 0 and sum_a > B:
                    count_good_array += 1
        
        return count_good_array

sol = Solution()
A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
B = 65
print(sol.solve(A, B)) # 4
