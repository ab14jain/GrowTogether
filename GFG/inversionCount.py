#https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1


class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        def countInv(arr, l, r):
            
            mid = (l + r) // 2
            count = 0
            if l < r:
                
                count += countInv(arr, l, mid)
                count += countInv(arr, mid+1, r)
                
                count += mergeAndCount(arr,l,mid,r)
            
            return count
        
        def mergeAndCount(arr, l, m, r):
            
            n1 = m - l + 1
            n2 = r - m
            
            left = arr[l:m+1]
            right = arr[m+1:r+1]

            i = 0
            j = 0
            k = l
            res = 0
        
        
            while i < n1 and j < n2:
                
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    
                    arr[k] = right[j]
                    res += n1 - i
                    j += 1
                k += 1
                
            while i < n1:
                arr[k] = left[i]
                i += 1
                k += 1
            
            while j < n2:
                arr[k] = right[j]
                j += 1
                k += 1
            
            return res
                
        
        n = len(arr)
        return countInv(arr, 0, n-1)  
    
    #     return self.countInv(arr, 0, len(arr) - 1)
    
    # def countInv(self, arr, l, r):
    #     # Your Code Here
    #     low = l
    #     high = r

    #     mid = (low + high) // 2

    #     inv_count = 0

    #     if low < high:
    #         inv_count += self.countInv(arr, l, mid)
    #         inv_count += self.countInv(arr, mid + 1, r)

    #         inv_count += self.mergeSort(arr, low, mid, high)
        
    #     return inv_count

    # def mergeSort(self, arr, low, mid, high):

    #     n1 = mid - low + 1
    #     n2 = high - mid

    #     left = arr[low:mid + 1]
    #     right = arr[mid + 1:high + 1]


    #     i = 0
    #     j = 0
    #     res = 0
    #     k = low

    #     # 3 5 1 10 9 2 6 8
    #     # 3 5 1 10          9 2 6 8
    #     # 3 5       1 10          9 2       6 8
    #     # 3     5       1   10          9   2       6   8
    #     # 3 5       1 10          9 2       6 8
    #     # 1 3 5 10     2 6 8 9

    #     while i < n1 and j < n2:

    #         if left[i] <= right[j]:
    #             arr[k] = left[i]
    #             i += 1
                
    #         else:
    #             arr[k] = right[j]
    #             j += 1
    #             res += n1 - i
    #         k += 1
        
    #     while i < n1:
    #         arr[k] = left[i]
    #         i += 1
    #         k += 1
        
    #     while j < n2:
    #         arr[k] = right[j]
    #         j += 1
    #         k += 1
        
    #     return res


s=Solution()
print(s.inversionCount([3,5,1,10,9,2,6,8])) # 5
# print(s.inversionCount([1, 20, 6, 4, 5])) # 5
# print(s.inversionCount([2, 4, 1, 3, 5])) # 3
# print(s.inversionCount([2, 3, 4, 5, 6])) # 0
    
    