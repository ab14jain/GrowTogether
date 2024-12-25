#https://www.scaler.com/academy/mentee-dashboard/class/325318/assignment/problems/199?navref=cl_tt_nv

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):

        def left_binary_search(A, B):
            left = 0
            right = len(A) - 1
            mid = (left + right) // 2

            while left <= right:
                if A[mid] == B:
                    right = mid - 1
                elif A[mid] < B:
                    left = mid + 1
                else:
                    right = mid - 1
                mid = (left + right) // 2
            
            return left
        
        def right_binary_search(A, B):
            left = 0
            right = len(A) - 1
            mid = (left + right) // 2

            while left <= right:
                if A[mid] == B:
                    left = mid + 1
                elif A[mid] < B:
                    left = mid + 1
                else:
                    right = mid - 1
                mid = (left + right) // 2

            return right
        
        left = left_binary_search(A, B)
        right = right_binary_search(A, B)

        if left > right:
            return [-1, -1]
        return [left, right]
    
s= Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 8)) #[3, 4]
print(s.searchRange([5, 17, 100, 111],3))