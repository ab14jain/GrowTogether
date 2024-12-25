#https://www.scaler.com/academy/mentee-dashboard/class/325300/assignment/problems/21272?navref=cl_tt_nv
import sys
sys.setrecursionlimit(10**9)
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            return merge(left, right)
        
        def merge(l, r):
            temp = []
            i = j = 0

            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    temp.append(l[i])
                    i += 1
                else:
                    temp.append(r[j])
                    j += 1
            
            while i < len(l):
                temp.append(l[i])
                i += 1
            
            while j < len(r):
                temp.append(r[j])
                j += 1

            return temp
        
        return merge_sort(A)

s=Solution()
A=[5, 2, 9, 3, 5, 7, 1]
print(s.solve(A)) # Output: [1, 2, 3, 5, 5, 7, 9]
A=[1, 2, 3, 4, 5]
print(s.solve(A)) # Output: [1, 2, 3, 4, 5]
A=[5, 4, 3, 2, 1]
print(s.solve(A)) # Output: [1, 2, 3, 4, 5]
A=[9,1]
print(s.solve(A)) # Output: [1, 2, 3, 4, 5]