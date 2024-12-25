#https://www.scaler.com/academy/mentee-dashboard/class/325300/assignment/problems/4190/?navref=cl_pb_nv_tb

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Approach : Finding all paarir using two loops
        # count = 0
        # n = len(A)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if A[i] > A[j]:
        #             count += 1
        
        # return (count % 1000000007)

        #Approach : Using Merge Sort

        # def merge_sort(arr, l, r):
        #     res = 0
            
        #     if l < r:
        #         m = (l + r) // 2
        #         res += merge_sort(arr, l, m)
        #         res += merge_sort(arr, m+1, r)
        #         res += merge(arr, l, m, r)
            
        #     return res
        
        # def merge(arr, l, m, r):
        #     count = 0
        #     i = j = 0
        #     k = l            
        #     n1 = m - l + 1
        #     n2 = r - m
        #     L = [0] * n1
        #     R = [0] * n2

        #     for i in range(n1):
        #         L[i] = arr[l + i]

        #     for j in range(n2):
        #         R[j] = arr[m+1+j]

            
        #     while (i<n1 and j<n2):
        #         if L[i] <= R[j]:
        #             arr[k] = L[i]
        #             i += 1
        #         else:
        #             arr[k] = R[j]
        #             j += 1
        #             count += (n1 - i)
                
        #         k += 1

        #     while i < n1:
        #         arr[k] = L[i]
        #         i += 1
        #         k += 1
            
        #     while j < n2:
        #         arr[k] = R[j]
        #         j += 1
        #         k += 1
            
        #     return count

        # n = len(A)
        # result = merge_sort(A, 0, n-1)
        
        # return result % 1000000007

               
        def merge_count(arr, l, m, r):
            n1 = m - l + 1
            n2 = r - m

            # Set up two lists for left and right halves
            left = arr[l:m + 1]
            right = arr[m + 1:r + 1]

            
            res = 0
            i = 0
            j = 0
            k = l
            while i < n1 and j < n2:
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                    res += (n1 - i)
                k += 1

            # Merge remaining elements
            while i < n1:
                arr[k] = left[i]
                i += 1
                k += 1
            while j < n2:
                arr[k] = right[j]
                j += 1
                k += 1

            return res

        # Function to count inversions in the array
        def count_inv(arr, l, r):
            res = 0
            if l < r:
                m = (r + l) // 2                
                res += count_inv(arr, l, m)
                res += count_inv(arr, m + 1, r)                
                res += merge_count(arr, l, m, r)
            return res

        n = len(A)
        ans = count_inv(A, 0, n - 1)
        return ans % 1000000007


    
s=Solution()
A=[45,10,15,25,50]
print(s.solve(A)) # Output: 3
A=[5, 2, 9, 3, 5, 7, 1]
print(s.solve(A)) # Output: 11
A=[1, 2, 3, 4, 5]
print(s.solve(A)) # Output: 0
A=[3, 4, 1, 2]
print(s.solve(A)) # Output: 4
