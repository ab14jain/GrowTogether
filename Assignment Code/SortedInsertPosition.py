#https://www.scaler.com/academy/mentee-dashboard/class/325318/assignment/problems/204?navref=cl_tt_lst_nm

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):

        def binary_search(A, B):
            left = 0
            right = len(A) - 1
            mid = (left + right) // 2

            while left <= right:
                if A[mid] == B:
                    return mid
                elif A[mid] < B:
                    left = mid + 1
                else:
                    right = mid - 1
                mid = (left + right) // 2
            
            return left
        
        return binary_search(A, B)
    
s= Solution()
print(s.searchInsert([1, 3, 5, 6], 5)) #2
print(s.searchInsert([1, 3, 5, 6], 2)) #1
print(s.searchInsert([1, 3, 5, 6], 7)) #4