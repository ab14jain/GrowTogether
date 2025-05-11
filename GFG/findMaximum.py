#https://www.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1

class Solution:

	def findMaximum(self, arr):
		# code here

            prev = arr[0]
            i = 1
            n = len(arr)
            
            while i < n:
                if arr[i] < prev:
                    return prev
                
                prev = arr[i]
                
                i += 1
            
            return arr[-1]
     
s=Solution()
print(s.findMaximum([1, 2, 4, 5, 7, 8, 3]))
print(s.findMaximum([10, 20, 30, 40, 50]))
print(s.findMaximum([120, 100, 80, 20, 0]))
                    