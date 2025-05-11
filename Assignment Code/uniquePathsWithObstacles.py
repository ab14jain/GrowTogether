#https://www.scaler.com/academy/mentee-dashboard/class/325348/assignment/problems/8?navref=cl_tt_lst_nm

class Solution:
	# @param A : list of list of integers
	# @return an integer
	def uniquePathsWithObstacles(self, A):

            # m = len(A)
            # n = len(A[0])
            # path_count = 0
            # dp = [[[-1]*n] for _ in range(m)]

            # def vaildIndex(si, se):
            #     if si >= 0 and si < m and se >= 0 and se < n:
            #         return True
                 
            #     return False

            # def count_path(si, se, di, de):

            #     if not vaildIndex(si,se):
            #         return 
                
            #     if A[si][se] == 1:
            #         return 
                
            #     nonlocal path_count
            #     if si == di and se == de:
            #         path_count += 1
            #         return
                
            #     count_path(si+1, se, di, de)
            #     count_path(si, se+1, di, de)
                
            

            # count_path(0, 0, m-1, n-1)
            # return path_count
			

            # Iterative --> Bottom Up Approach
            m = len(A)
            n = len(A[0])
            dp = [[0]*n for _ in range(m)]            
            
            for i in range(m):
                for j in range(n):                     
                    if i == 0 or j == 0:
                        if A[i][j] != 1:
                            dp[i][j] = 1                        
                            if i > 0 and dp[i-1][j] == 0:
                                dp[i][0] = 0
                            elif j > 0 and dp[i][j-1] == 0:
                                dp[0][j] = 0                  
                    else:
                        if A[i][j] != 1:
                            dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    

            # print(dp)
            return dp[m-1][n-1]

s=Solution()
print(s.uniquePathsWithObstacles([[1, 0]]))
print(s.uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
     ]))
                
print(s.uniquePathsWithObstacles([
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
     ]))
                