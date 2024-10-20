#Approch
# 1. For each element in the array, we need to find the number of elements less than the current element on the left side and the number of elements greater than the current element on the right side.
# 2. The number of triplets that can be formed with the current element as the middle element is the product of the number of elements less than the current element on the left side and the number of elements greater than the current element on the right side.
# 3. We need to find the number of elements less than the current element on the left side and the number of elements greater than the current element on the right side.
# 4. We can find the number of elements less than the current element on the left side by iterating from 0 to i-1 and checking if the element at the current index is less than the element at index i.
# 5. We can find the number of elements greater than the current element on the right side by iterating from i+1 to n-1 and checking if the element at the current index is greater than the element at index i.
# 6. We can find the number of triplets that can be formed with the current element as the middle element by multiplying the number of elements less than the current element on the left side and the number of elements greater than the current element on the right side.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        n = len(A)
        triplets = 0

        for i in range(1, n-1):
            lesser = self.lesserOnes(A, i)
            greater = self.greaterOnes(A, i)
            triplets += lesser * greater

        return triplets
        
    
    def lesserOnes(self, A, i):
        count = 0
        for j in range(i):
            if A[j] < A[i]:
                count += 1
        return count
    
    def greaterOnes(self, A, i):
        count = 0
        for j in range(i+1, len(A)):
            if A[j] > A[i]:
                count += 1
        return count
    

s = Solution()
print(s.solve([1, 2, 3, 1, 2])) # 2
print(s.solve([1, 2, 3, 1, 2, 3])) # 6
print(s.solve([1, 2, 3, 1, 2, 3, 4])) # 8
print(s.solve([1, 2, 3, 1, 2, 3, 4, 5])) # 10
print(s.solve([1, 2, 3, 1, 2, 3, 4, 5, 6])) # 12