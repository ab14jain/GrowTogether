#https://www.scaler.com/academy/mentee-dashboard/class/325358/homework/problems/516?navref=cl_tt_lst_nm

from collections import defaultdict


class Solution:
	# @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return an integer
	def solve(self, A, B, C):

            if B == C:
                return 1
            
            adj = defaultdict(list)
            visisted = [False]*(len(A)+1)
            
            for i in range(len(A)):
                adj[A[i]].append(i+1)

            
            def dfs(node):
                
                stack = []
                stack.append(node)

                while stack:
                    curr = stack.pop()
                    visisted[curr] = True
                    for nbr in adj[curr]:                         
                         if not visisted[nbr]:
                            if nbr == B:  
                                return 1
                            stack.append(nbr)
                return 0

            return dfs(C)

s=Solution()
print(s.solve([1], 1, 1))
print(s.solve([1,1,2], 1, 2))
print(s.solve([1,1,2], 2, 1))

            