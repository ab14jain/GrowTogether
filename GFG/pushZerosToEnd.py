#https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1
class Solution:
	def pushZerosToEnd(self,arr):
            # code here
            # n = len(arr)
            # i = 0
            
            # while i < n:
            #     if arr[i] == 0:
            #         j = i + 1
            #         while j < n:
            #             if arr[j] != 0:
            #                 arr[i] = arr[j]
            #                 arr[j] = 0
            #                 break
            #             j += 1     
            #     i += 1

            # return arr

            # n = len(arr)
            # i = 0
            # temp_arr = [0 for _ in range(n)]
            # x = 0
            # for i in range(n):
            #     if arr[i] != 0:
            #         temp_arr[x] = arr[i]
            #         arr[i] = 0
            #         x += 1
            
            # return temp_arr

            # count = 0
    
            # for i in range(len(arr)):
            #     if arr[i] != 0:
            #         arr[i], arr[count] = arr[count], arr[i]
            #         count += 1
            
            # return arr
			
            n = len(arr)
            non_zero_count = 0

            for i in range(n):
                if arr[i] != 0:
                    arr[non_zero_count], arr[i] = arr[i], arr[non_zero_count]
                    non_zero_count += 1
            
            return arr
            
            

            


s=Solution()
print(s.pushZerosToEnd([2, 4, 1, 7, 5, 0])) #[2, 4, 1, 7, 5, 0]
print(s.pushZerosToEnd([3, 5, 0, 0, 4])) #[2, 4, 1, 7, 5, 0]
     