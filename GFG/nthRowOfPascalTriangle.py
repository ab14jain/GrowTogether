# https://www.geeksforgeeks.org/problems/pascal-triangle0652/1

#User function Template for python3
class Solution:

	def nthRowOfPascalTriangle(self, n):
	    # code here
         
            def fact(n):
                if n <= 1:
                    return 1
                
                return n*fact(n-1)
            
            def nC(n,k):
                return fact(n)//(fact(k)*fact(n-k))
            
            ans = []
            for i in range(n):
                ans.append(nC(n-1,i))

            return ans
     
s=Solution()
print(s.nthRowOfPascalTriangle(5))