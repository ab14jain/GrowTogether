class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        # time complexity O(n*m)
        # max_ones = 0
        # max_ones_index = 0
        # n = len(A)
        # for i in range(n):
        #     temp_count = 0
        #     for j in range(n):
        #         if A[i][j] == 1:
        #             temp_count += 1
            
        #     if temp_count > max_ones:
        #         max_ones = temp_count
        #         max_ones_index = i

        # return max_ones_index

        # time complexity O(n+m)
        
        max_ones_index = 0
        n = len(A)
        m = len(A[0])
        i = 0
        j = m - 1
        while i < n and j >= 0:
            if A[i][j] == 1:
                j -= 1
                max_ones_index = i
            else:
                i += 1
        
        return max_ones_index

s = Solution()
print(s.solve([[0, 0, 0, 0],
         [0, 0, 0, 1],
         [1, 1, 1, 1],
         [1, 1, 1, 1]])) # 2