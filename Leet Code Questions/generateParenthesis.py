#https://www.scaler.com/academy/mentee-dashboard/class/325292/assignment/problems/139?navref=cl_tt_nv

class Solution:
	# @param A : integer
	# @return a list of strings
	def generateParenthesis(self, A):
        
            ans = []
            res = []
            def gen_paren(A,ans,o,c):
                nonlocal res
                if len(ans) == 2*A:
                    cpy = ans[:]
                    res.append(cpy)
                    return

                if o < A:
                    #ans = ans + "("
                    gen_paren(A, ans + "(", o+1, c)

                if o > c:
                    #ans = ans + ")"
                    gen_paren(A, ans + ")", o, c+1)

            gen_paren(A,"",0,0)
            return res
     
s=Solution()
print(s.generateParenthesis(3))