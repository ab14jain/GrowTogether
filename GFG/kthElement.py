#https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1
class Solution:

    def kthElement(self, a, b, k):
        
        #using kth element of two sorted arrays
        n = len(a)
        m = len(b)
        i = 0
        j = 0

        while i < n and j < m:
            if a[i] < b[j]:
                if i + j == k - 1:
                    return a[i]
                i += 1
            else:
                if i + j == k - 1:
                    return b[j]
                j += 1
        
        while i < n:
            if i + j == k - 1:
                return a[i]
            i += 1
        
        while j < m:
            if i + j == k - 1:
                return b[j]
            j += 1
        
        return -1
            
s = Solution()
print(s.kthElement([2, 3, 6, 7, 9], [1, 4, 8, 10], 5)) # 6
