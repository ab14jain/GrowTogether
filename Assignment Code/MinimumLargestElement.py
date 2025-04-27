import heapq


class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def solve(self, A, B):
		
            min_heap = []
            state = []
            n = len(A)
            for i in range(n):
                state.append(A[i])
                heapq.heappush(min_heap, (2*A[i], i))

            
            for i in range(B):                 
                top, i = heapq.heappop(min_heap)
                state[i] = top
                heapq.heappush(min_heap, (top+A[i], i))               
            
            state.sort(reverse=True)
            return state[0]


s=Solution()
print(s.solve([2918,5180,4023,3172,2867,6108,414,9809,8419,2838,1171,7449,8930,1939,2393,2396,6969,7951,9009,1668,1836,1286,982,2571,7299,9898,1105,6232,8134,905,1648,5139,798,4776,9589,7616,9487,2107,5518,9979,8227,8023,592,2830,2598,7238,4123,9607,4070,5152,4883,1551,9602,8739], 150))
#10535
print(s.solve([1,2,3,4], 3))
print(s.solve([5, 1, 4, 2], 5))
		

