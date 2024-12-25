#https://www.geeksforgeeks.org/problems/overlapping-intervals--170633/1

class Solution:
	def mergeOverlap(self, arr):
		#Code here
			n = len(arr)
			
			if n == 1:
				return arr
				
			arr.sort(key = lambda x:x[0])
			
			i = 1
			
			result = []
			result.append(arr[0])
			while i < n:
				
				start = arr[i][0]
				end = arr[i][1]

				if result[-1][1] >= start:
					result[-1][1] = max(result[-1][1], end)
				else:
					result.append(arr[i])
				i += 1	
						
			return result


s = Solution()
arr = [[1,3],[2,4],[5,7],[6,8]]
print(s.mergeOverlap(arr)) # [[1, 4], [5, 8]]
arr = [[1,3],[7,9],[4,6],[10,13]]
print(s.mergeOverlap(arr)) # [[1, 3], [4, 6], [7, 9], [10, 13]]