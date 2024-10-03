class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        lenA = len(A)
        B = B % lenA

        if B == 0:
            return A
        else:
            reverseArr = self.reverseArray(A, 0, lenA - 1)
            reverseArr = self.reverseArray(reverseArr, 0, B - 1)
            reverseArr = self.reverseArray(reverseArr, B, lenA - 1)
            return reverseArr

    
    def reverseArray(self, A, B, C):
        pointer1 = B
        pointer2 = C

        while pointer1 <= pointer2:
            temp = A[pointer1]
            A[pointer1] = A[pointer2]
            A[pointer2] = temp
            pointer1 += 1
            pointer2 -= 1
        
        return A
    

sol = Solution()
print(sol.solve([1, 2, 3, 4, 5], 2))
