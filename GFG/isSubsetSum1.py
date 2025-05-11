#https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        
        def recur(e, rem):

            if rem == 0:
                return True
            
            if e < 0:
                return False
            
            if rem < 0:
                return False   

            return recur(e-1, rem-arr[e]) or recur(e-1, rem)
        
        return recur(len(arr)-1, sum)
    
s=Solution()
print(s.isSubsetSum([3,34,4,12,5,2],9))
print(s.isSubsetSum([3, 34, 4, 12, 5, 2],30))
print(s.isSubsetSum([1,2,3],6))