class Solution:
    # @param A : list of integers
    # @return an integer

    # Approach
    # 1. Find the sum of all elements in the array
    # 2. Traverse the array from left to right and keep calculating the sum of elements
    # 3. Traverse the array from right to left and keep calculating the sum of elements
    # 4. If the sum of elements from left to right is equal to the sum of elements from right to left, then return the index
    # 5. Else return -1

    def solve(self, A):
        n = len(A)
        if n == 1:
            return 1
        
        lower_sum  = [0]*len(A)
        higher_sum = [0]*len(A)
        
        # sum from left to right ----------> 
        lower_sum[0] = A[0] 
        for i in range(1, n):
            lower_sum[i] = lower_sum[i - 1] + A[i]
        
        # sum from right to left <----------
        higher_sum[n - 1] = A[n - 1]
        for i in range(n - 2, -1, -1):
            higher_sum[i] = higher_sum[i + 1] + A[i]

        print(lower_sum)
        print(higher_sum)

        for i in range(0, len(A)):
            if lower_sum[i] == higher_sum[i]:
                return i

        return -1

        # n = len(A)
        # left_sum = [0]*n
        # right_sum = [0]*n

        # left_sum[0] = A[0]
        # right_sum[n-1] = A[n-1]
        # for i in range(1, n-1):
        #     left_sum[i] = left_sum[i-1] + A[i]
        #     right_sum[n-i-1] = right_sum[n-i] + A[n-i-1]

        # print(left_sum)
        # print(right_sum)
        
        # for i in range(0, len(A)):
        #     if left_sum[i] == right_sum[i]:
        #         return i
        
        
        # return -1


s= Solution()
A = [-7, 1, 5, 2, -4, 3, 0]
#A = [1, 2, 3]
#A = [1,2,3,7,1,2,3]
print(s.solve(A)) # [3]