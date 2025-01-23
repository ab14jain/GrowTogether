from collections import deque
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def slidingMaximum(self, A, B):
		
            n = len(A)
            deque_max = deque()

            ans_max = []
            
            for i in range(B):                
                while deque_max and A[deque_max[-1]] <= A[i]:
                    deque_max.pop()
                deque_max.append(i)
            
            ans_max.append(A[deque_max[0]])

            i = 1
            j = B

            while j < n:

                if deque_max[0] == i - 1:
                    deque_max.popleft()
                 
                while deque_max and A[deque_max[-1]] <= A[j]:
                    deque_max.pop()
                
                deque_max.append(j)
            
                ans_max.append(A[deque_max[0]])

                i += 1
                j += 1

            return ans_max
     
# Time complexity: O(n)
# Space complexity: O(k) where k is the size of the window


s=Solution()
A=[1, 3, -1, -3, 5, 3, 6, 7]
B=3
print(s.slidingMaximum(A,B))
