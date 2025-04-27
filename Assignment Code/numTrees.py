class Solution:
	# @param A : integer
	# @return an integer
	def numTrees(self, A):
            
            c =[0]*(A+1)
            c[0] = 1
            c[1] = 1
            treeCount = 0
            for num in range(2, A+1):                
                tSum = 0
                j = num-1
                for i in range(j+1):
                    tSum += c[i]*c[j]
                    j -= 1
                
                c[num] = tSum
            
            return c[A]
     
s=Solution()
print(s.numTrees(3))
print(s.numTrees(4))