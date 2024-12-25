#https://www.geeksforgeeks.org/problems/next-permutation5226/1

#Intution:
#1. Find the pivot element from the end of the array such that arr[pivot] < arr[pivot+1]
#2. If pivot is -1, then the array is in descending order, so sort the array and return
#3. Find the element from the end of the array such that arr[i] > arr[pivot]
#4. Swap arr[i] and arr[pivot]
#5. Reverse the array from pivot+1 to end of the array
#6. Return the array

#The time complexity is O(n) and space complexity is O(1)
class Solution:
    def nextPermutation(self, arr):
        # code here

        # [2, 4, 1, 7, 5, 0]
               # ^
        n = len(arr)
        pivot = -1
        for i in range(n-2, -1, -1):
            if arr[i] < arr[i+1]:
                pivot = i
                break
        
        if pivot == -1:
            arr.sort()
            return arr
        
        for i in range(n-1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break

        l = pivot + 1
        r = n - 1

        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        
        return arr       
    

s=Solution()
print(s.nextPermutation([2, 4, 1, 7, 5, 0])) #[2, 4, 5, 0, 1, 7]
print(s.nextPermutation([3, 4, 2, 5, 1])) #[3, 4, 5, 1, 2]
print(s.nextPermutation([1,2,3])) #[1,3,2]
print(s.nextPermutation([3,2,1])) #[1,2,3]
print(s.nextPermutation([1,1,5])) #[1,5,1]
print(s.nextPermutation([1,3,2])) #[2,1,3]
print(s.nextPermutation([1,3])) #[3,1]
print(s.nextPermutation([1])) #[1]