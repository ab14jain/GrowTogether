#https://www.scaler.com/academy/mentee-dashboard/class/325296/assignment/problems/317?navref=cl_tt_lst_nm

class Solution:
	# @param A : string
	# @return an integer
	def findRank(self, A):

            char_arr = list(A)
            n = len(char_arr)
            fact = [0]*(n+1)
            fact[0] = 1

            for i in range(1,n+1):
                fact[i] = i * fact[i-1]

            rank = 0
            for i in range(n):
                char = char_arr[i]
                odr_char = ord(char)
                count = 0
                for j in range(i+1, n):     
                    if odr_char > ord(char_arr[j]):
                        count += 1                
                rank += (count *fact[(n-i-1)])

            return (rank + 1)
     

s=Solution()
print(s.findRank('dfche'))
print(s.findRank('bfah'))
print(s.findRank('acb'))
print(s.findRank('abcdefghk'))
print(s.findRank('deghacz'))
            