#https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/1

class Solution:
    def subarrayXor(self, arr, k):
        # code here

        n = len(arr)    
        prefix_xor = {}
        curr_xor = 0
        result = 0
        for i in range(n):            
            curr_xor ^= arr[i]            
            if curr_xor == k:
                result += 1

            if (curr_xor ^ k) in prefix_xor:
                result += prefix_xor[curr_xor ^ k]

            if curr_xor in prefix_xor:
                prefix_xor[curr_xor] += 1            
            else:
                prefix_xor[curr_xor] = 1

        return result
    
s=Solution()
print(s.subarrayXor([4, 2, 2, 6, 4], 6))
print(s.subarrayXor([5, 6, 7, 8, 9], 5))
print(s.subarrayXor([1, 1, 1, 1], 0))
print(s.subarrayXor([1, 0, 0, 0, 1, 0, 1], 2))
print(s.subarrayXor([1, 1, 1, 1, 1], 2))