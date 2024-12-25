#https://www.scaler.com/academy/mentee-dashboard/class/325318/homework/problems/1104?navref=cl_tt_nv
import bisect

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of list of integers
    # @return an integer
    def solve(self, A, B, C):
        

        # for i in range(A):
        #     C[i].sort()

        # ans = float('inf')  
        # res = []
        # for i in range(A-1):

        #     next_row = C[i+1]
        #     for j in range(B):
        #         lower = bisect.bisect_left(next_row, C[i][j])
        #         upper = bisect.bisect_right(next_row, C[i][j])
        #         ans = min(ans, min((upper - C[i][j]), (C[i][j]-lower)))
            
        
        
        # return ans

        def bsearch(low, high, n, arr):
            mid = (low + high)//2
        
            if(low <= high):
                if(arr[mid] < n):
                    return bsearch(mid +1, high, n, arr)
                return bsearch(low, mid - 1, n, arr)
        
            return low
        
        # Return the minimum absolute difference adjacent
        # elements of array
        def mindiff(arr, n, m):
        
            # arr = [0 for i in range(R)][for j in range(C)]
            # Sort each row of the matrix.
            for i in range(n):
                sorted(arr)
        
            ans = 2147483647
        
            # For each matrix element
            for i in range(n-1):
                for j in range(m):
                    # Search smallest element in the next row which
                    # is greater than or equal to the current element
                    p = bsearch(0, m-1, arr[i][j], arr[i + 1])
                    ans = min(ans, abs(arr[i + 1][p] - arr[i][j]))
        
                    # largest element which is smaller than the current
                    # element in the next row must be just before
                    # smallest element which is greater than or equal
                    # to the current element because rows are sorted.
                    if (p-1 >= 0):
                        ans = min(ans, abs(arr[i + 1][p - 1] - arr[i][j]))
            return ans


        return mindiff(C,A,B)

            #ans = min(ans, min(abs(C[i][j] - next_row[lower-1]), abs(C[i][j] - next_row[upper])))
            
            # a = bisect_right(C, C[i+1])
            # b = bisect_left(C, C[i][j])

            # for j in range(B):

            #     ans = min(ans, min(a-C[i][j], C[i][j]-b))

                # for k in range(A):
                #     for l in range(B):
                #         ans = min(ans, abs(C[i][j] - C[k][l]))

        return ans

# Time complexity: O(A^2 * B^2)
# Space complexity: O(1)

A = 2
B = 2
C = [[1, 4], [2, 3]]
s = Solution()
print(s.solve(A, B, C))
# Explanation: The minimum difference is 0. We can choose 1 from the first list and 1 from the second list.

A = 2
B = 2
C = [[1, 2], [3, 4]]
print(s.solve(A, B, C))

       


