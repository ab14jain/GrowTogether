class Solution:
    def validgroup(self, arr, k):
        # Code here

        # arr.sort()
        # n = len(arr)
        # i = 0

        # if n%k != 0:
        #     return False
        
        # while i < n:

        #     # for j in range(i, i+k-1):
        #     #     if arr[j+1] - arr[j] == 1:
        #     #         continue
        #     #     else:
        #     #         return False
        #     # i += k

        #     if arr[i+k-1] - arr[i] != k-1:
        #         return False

        #     i += k           
        
        # return True

        # Traverse the sorted arr
        for i in range(len(arr)):            
            if arr[i] == -1:
                continue            
            count = 0            
            curr = arr[i]            
            for j in range(i, len(arr)):
                if arr[j] == curr:
                    count += 1                    
                    curr += 1
                    
                    arr[j] = -1
                if count == k:
                    break
            
            if count != k:
                return False

        
        return True
        
s=Solution()
# print(s.validgroup([3, 6, 10, 14, 5, 2, 9, 9], 2))
print(s.validgroup([10,1,1,2,10,11], 2))
# print(s.validgroup([10,1,2,11], 2))
# print(s.validgroup([7,8,9,10,11], 2))
                
            
