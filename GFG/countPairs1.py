#https://www.geeksforgeeks.org/problems/count-pairs-sum-in-matrices4332/1

class Solution:
	def countPairs(self, mat1, mat2, x):
		# code here

            # Approach 1- Brute Force 
            # TC - n^4 ~ 100^4 ~ 10^8
            # TLE 1010 /1115
            r1 = len(mat1)
            c1 = len(mat1[0])

            r2 = len(mat2)
            c2 = len(mat2[0])
            pairCount = 0

            # for i in range(r1):
            #     for j in range(c1):

            #         if mat1[i][j] < x:
            #             y = x-mat1[i][j]

            #             for a in range(r2):
            #                 for b in range(c2):
            #                     if y == mat2[a][b]:
            #                         pairCount += 1

            # return pairCount

            def binarySearch(mat, val):
                n = len(mat)
                l = 0
                h = n*n - 1

                while l <= h:
                    mid = l + (h-l)//2
                    r = mid//n
                    c = mid%n

                    if mat[r][c] == val:
                        return True
                    elif mat[r][c] < val:
                        l = mid + 1
                    else:
                        h = mid - 1
                    
                return False
                 

            for i in range(r1):
                for j in range(c1):
                    if mat1[i][j] < x: 
                        y = x - mat1[i][j]

                        if binarySearch(mat2, y):
                            pairCount += 1

            return pairCount
     

s=Solution()
print(s.countPairs([[1, 5, 6], [8, 10, 11], [15, 16, 18]],[[2, 4, 7], [9, 10, 12], [13, 16, 20]],21))
                                    