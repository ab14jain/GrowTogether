class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):        
        pointer1 = B
        pointer2 = C
        while pointer2 >= pointer1:            
            temp = A[pointer1]
            A[pointer1] = A[pointer2]
            A[pointer2] = temp            
            pointer1 += 1
            pointer2 -= 1
        
        return A
    
# Time complexity: O(n)
# Space complexity: O(1)
# Input: A = [1, 2, 3, 4, 5], B = 2, C = 4
# Output: [1, 2, 5, 4, 3]

sol = Solution()
print(sol.solve([1, 2, 3, 4, 5], 2, 4))
print(sol.solve([2, 5, 6], 0, 2))