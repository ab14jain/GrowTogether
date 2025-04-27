#https://www.scaler.com/academy/mentee-dashboard/class/325292/assignment/problems/138?navref=cl_tt_nv

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def permute(self, A):

            n = len(A)
            ans = [0]*n
            res = []
            used = [False]*n

            def get_pernute(A, ans, idx, n, used):
                nonlocal res
                if idx == n:
                    cpy = ans[:]
                    res.append(cpy)
                    return

                for i in range(n):
                    if used[i] == False:
                        used[i] = True
                        ans[idx] = A[i]
                        get_pernute(A, ans, idx+1, n, used)
                        used[i] = False

            get_pernute(A, ans, 0, n, used)

            return res
     
s=Solution()
print(s.permute([1,2,3]))