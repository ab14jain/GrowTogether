class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

        i = 0
        j = 0
        sum = 0
        n = len(A)
        while j < n and i < n:
            if A[i] == B:
                return [A[i]]      
            else:
                sum += A[j]
                if sum == B:
                    return A[i:j+1]
                elif sum > B:
                    sum -= A[i]
                    sum -= A[j]
                    i += 1
                else:
                    j += 1
        return [-1]
    
s=Solution()
A = [1,1000000000]
B = 1000000000
print(s.solve(A, B)) # Output: [2, 3]
# A = [1, 2, 3, 4, 5]
# B = 5
# print(s.solve(A, B)) # Output: [2, 3]
# A = [5, 10, 20, 100, 105]
# B = 110
# print(s.solve(A, B)) # Output: [-1]
# A = [1, 2, 3, 4, 5]
# B = 9
# print(s.solve(A, B)) # Output: [2, 4]
# A = [1, 2, 3, 4, 5]
# B = 10
# print(s.solve(A, B)) # Output: [1, 4]
# A = [1, 2, 3, 4, 5]
# B = 15
# print(s.solve(A, B)) # Output: [0, 4]