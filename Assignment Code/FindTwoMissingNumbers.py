class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        A_arr = [-1]*(n+2)

        for i in A:
            if(A_arr[i-1]) == -1:
                A_arr[i-1] = 1
        
        result = []
        for i in range(len(A_arr)):
            if A_arr[i] == -1:
                result.append(i+1)
        
        return result

# Driver code
s = Solution()
print(s.solve([1, 3, 5])) # [2, 4]
print(s.solve([1, 2, 3])) # [4, 5]
print(s.solve([1, 2, 3, 4, 5])) # [6, 7]
print(s.solve([1, 2, 3,4,5,6,7,8,9])) # [10, 11]