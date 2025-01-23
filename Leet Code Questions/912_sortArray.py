import random


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        # Quick Sort
        # def pivot_index(A, s, e):

        #     random_index = random.randint(s, e)
        #     A[random_index], A[s] = A[s], A[random_index]

        #     pivot = A[s]
        #     l = s+1
        #     r = e

        #     while l <= r:
        #         if A[l] <= pivot:
        #             l += 1
        #         elif A[r] >= pivot:
        #             r -= 1
        #         else:
        #             A[l], A[r] = A[r], A[l]
        #             l += 1
        #             r -= 1
            
        #     A[s], A[r] = A[r], A[s]
        #     return r
        

        # def quick_sort(arr, s, e):

        #     if s >= e:
        #         return
            
        #     idx = pivot_index(arr, s, e)
        #     quick_sort(arr, s, idx-1)
        #     quick_sort(arr, idx+1, e)

        
        # quick_sort(nums, 0, len(nums)-1)
        # return nums 

        # Merge Sort

        def merge_sort(arr, l, r):
            if l == r:
                return arr
            
            mid = (l+r)//2
            merge_sort(arr, l, mid)
            merge_sort(arr, mid+1, r)
            return merge(arr, l, mid, r)

        def merge(arr, l, mid, r):

            n1= mid - l + 1
            n2 = r - (mid + 1) + 1

            B = [0]*n1
            C = [0]*n2
            k = 0  
            for i in range(l,mid+1):
                B[k] = arr[i]
                k += 1

            k = 0
            for i in range(mid+1, r+1):
                C[k] = arr[i]
                k += 1

            i = 0
            j = 0
            k = l      

            while i < n1 and j < n2:
                if B[i] <= C[j]:
                    arr[k] = B[i]
                    i += 1
                else:
                    arr[k] = C[j]
                    j += 1
                k += 1
                
                
            while i < n1:
                arr[k] = B[i]
                i += 1
                k += 1
            
            while j < n2:
                arr[k] = C[j]
                j += 1
                k += 1
            
            return arr
           

        return merge_sort(nums, 0, len(nums)-1)
        
    
s=Solution()
print(s.sortArray([5])) # [1,2,3,5]
print(s.sortArray([5,2,3,1])) # [1,2,3,5]
print(s.sortArray([5,1,1,2,0,0])) # [0,0,1,1,2,5]