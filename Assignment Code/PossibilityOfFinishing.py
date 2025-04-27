#https://www.scaler.com/academy/mentee-dashboard/class/325372/assignment/problems/377?navref=cl_tt_nv

from collections import defaultdict, deque


class Solution:
	# @param A : integer
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
	def solve(self, A, B, C):
		
            adj = defaultdict(list)
            courses = [0]*(A+1)
            for i in range(len(B)):
                adj[B[i]].append(C[i])
                courses[C[i]] += 1

            
            q = deque()
            ans = []
            for i in range(1, A+1):
                if courses[i] == 0:
                    q.append(i)

            while q:
                curr = q.popleft()
                ans.append(curr)
                for nbr in adj[curr]:
                    courses[nbr] -= 1

                    if courses[nbr] == 0:
                        q.append(nbr)

            if len(ans) == A:
                return 1
            
            return 0
s=Solution()
print(s.solve(8, [1,2,3,4,5,8],[2,3,4,5,6,7]))
print(s.solve(3, [1,2],[2,3]))
print(s.solve(2, [1,2],[2,1]))


