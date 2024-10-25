
# Intuition
#<!-- Describe your first thoughts on how to solve this problem. -->

# intution
# 1. Traverse the top row, then the right column, then the bottom row, and finally the left column.
# 2. Repeat the above steps for the inner matrix.
# 3. Keep track of the top, bottom, left, and right boundaries of the matrix.
# 4. Keep track of the count of elements visited.
# 5. Repeat the above steps until the top boundary is less than or equal to the bottom boundary and the left boundary is less than or equal to the right boundary.



# Approach
#<!-- Describe your approach to solving the problem. -->
# 1. Initialize the top, bottom, left, and right boundaries of the matrix.
# 2. Initialize the count of elements visited. 
# 3. Initialize the answer array of size n*m.
# 4. Traverse the top row, then the right column, then the bottom row, and finally the left column.
# 5. Repeat the above steps for the inner matrix.
# 6. Keep track of the top, bottom, left, and right boundaries of the matrix.
# 7. Keep track of the count of elements visited.
# 8. Repeat the above steps until the top boundary is less than or equal to the bottom boundary and the left boundary is less than or equal to the right boundary.
# 9. Return the answer array.

# Complexity
# - Time complexity:
#<!-- Add your time complexity here, e.g. $$O(n)$$ -->
#
# 1. The time complexity is O(n*m) because we are traversing all the elements of the matrix.


# - Space complexity:
#<!-- Add your space complexity here, e.g. $$O(n)$$ -->
# we are using extra space to store the answer array of size n*m.

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        m = len(matrix[0])
        
        top = 0
        bottom = n - 1
        left = 0
        right = m - 1
        count = 0

        ans = [0]*n*m

        while top <= bottom and left <= right:
            for i in range(left, right+1):
                ans[count] = matrix[top][i]
                count += 1
            top += 1

            for i in range(top, bottom+1):
                ans[count] = matrix[i][right]
                count += 1
            right -= 1

            for i in range(right, left-1, -1):
                if count < n*m:
                    ans[count] = matrix[bottom][i]
                    count += 1
            bottom -= 1

            for i in range(bottom, top-1, -1):    
                if count < n*m:            
                    ans[count] = matrix[i][left]
                    count += 1
            left += 1
        
        return ans
    

s = Solution()
# print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(s.spiralOrder([[7],[9],[6]]))
# print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
