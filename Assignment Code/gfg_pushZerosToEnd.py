#https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1

class Solution:
	def pushZerosToEnd(self,arr):
            # code here
            n = len(arr)
            i = 0
            
            while i < n:
                if arr[i] == 0:
                    j = i + 1
                    while j < n:
                        if arr[j] != 0:
                            arr[i] = arr[j]
                            arr[j] = 0
                            break
                        j += 1     
                i += 1

            return arr
s=Solution()
# print(s.pushZerosToEnd([1, 2, 0, 4, 3, 0, 5, 0])) # [1, 2, 4, 3, 5, 0, 0, 0]
print(s.pushZerosToEnd([1, 2, 0, 0, 0, 3, 6])) # [1, 2, 3, 6, 0, 0, 0]
# print(s.pushZerosToEnd([0, 0, 0, 0, 0])) # [0, 0, 0, 0, 0]
# print(s.pushZerosToEnd([1, 2, 3, 4, 5])) # [1, 2, 3, 4, 5]