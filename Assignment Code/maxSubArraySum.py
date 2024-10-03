class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):

        if A == 1:
            if C[0] <= B:
                return C[0]
        max_sum = 0
        for i in range(A):
            temp_sum = 0
            for j in range(i,A):
                # print(C[i:j+1])
                # print(sum(C[i:j+1]))
                #temp_sum = sum(C[i:j+1])
                temp_sum += C[j]
                if temp_sum <= B:
                    max_sum = max(temp_sum, max_sum)
                    
        return max_sum


s= Solution()
A = 5
B = 10
C = [2, 1, 3, 4, 1]
print(s.maxSubarray(A,B,C)) # 10