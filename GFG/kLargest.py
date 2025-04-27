import heapq


class Solution:
	def kLargest(self, arr, k):
		# Your code here

        # Approach 1: Using sorting		
            # arr.sort(reverse=True)
            # return arr[:k]
      
        # Approach 2: Using heap		
            # max_heap = []

            # for num in arr:
            #     heapq.heappush(max_heap, -num)

            # res = []

            # for i in range(k):
            #     res.append(-heapq.heappop(max_heap)) 
            
            # return res
        
        # Approach 3: Quick Select

            n = len(arr)
            k = n - k # coz arr will be sorted in ascending order so largest will be from the end

            def quick_select(left, right):
                pivot = arr[right]
                p = left

                for i in range(left, right):
                    if arr[i] <= pivot:
                        arr[i], arr[p] = arr[p], arr[i]
                        p += 1
                
                arr[p], arr[right] = arr[right], arr[p]

                if p > k:
                    return quick_select(left, p-1)
                elif p < k:
                    return quick_select(p+1, right)
                else:
                    return       


            quick_select(0, n-1)
            res = arr[k:]
            res.sort(reverse=True)
            return res


      

s=Solution()
# print(s.kLargest([12,5,787,1,23], 2))
print(s.kLargest([12,5,787,1,2,23], 4))