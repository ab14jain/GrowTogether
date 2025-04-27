#https://www.scaler.com/academy/mentee-dashboard/class/325292/homework/problems/147?navref=cl_tt_lst_nm

class Solution:
	# @param A : string
	# @return a list of strings
	def letterCombinations(self, A):

            num_char_map = {
                '0' : '0',
                '1' : '1',
                '2' : 'abc',
                '3' : 'def',
                '4' : 'ghi',
                '5' : 'jkl',
                '6' : 'mno',
                '7' : 'pqrs',
                '8' : 'tuv',
                '9' : 'wxyz',
            }            
            res = []
            def generate(A, ans, idx, n):

                nonlocal res
                if len(ans) == n:
                    cpy = ans[:]
                    res.append(cpy)
                    return

                for i in num_char_map[A[idx]]:
                    generate(A,ans+i,idx+1,n)

            generate(A, "", 0, len(A))

            return res

s=Solution()
print(s.letterCombinations("9620981496"))
print(s.letterCombinations("012"))
print(s.letterCombinations("012"))