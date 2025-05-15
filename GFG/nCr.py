# https://www.geeksforgeeks.org/problems/ncr1019/1

class Solution:
    def nCr(self, n, r):
        # code here

        def fact(n):

            if n <= 1:
                return 1
            
            return n*fact(n-1)
        

        return fact(n)//(fact(n-r)*fact(r))
    
s=Solution()
print(s.nCr(5,2))
print(s.nCr(2,4))
print(s.nCr(100,2))