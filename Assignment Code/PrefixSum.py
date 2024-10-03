class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):

        prefSum = [A[0]]
        for i in range(1, len(A)):
            prefSum.append(A[i] + prefSum[i - 1])
        
        result = []

        for j in range(0, len(B)):
            L = B[j][0]
            R = B[j][1]

            left_sum = 0
            if L > 0:
                left_sum = prefSum[L - 1]
            result.append(prefSum[R] - left_sum)

        return result

s= Solution()
# A = [1, 2, 3, 4, 5]
# B = [[0, 3], [1, 2]]

A = [2, 2, 2]
B = [[0, 0], [1, 2]]
print(s.rangeSum(A, B)) # [10, 5]