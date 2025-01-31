class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        
        transpose = []

        row = len(A)
        column = len(A[0]) 

        for c in range(column):
            r = 0
            col = []
            while(r < row):
                col.append(A[r][c])
                r += 1
            
            transpose.append(col)
            
        return transpose



sol = Solution()
#A = [[47,-59,20,33,20,-47,-87,-59,85],[8,-67,48,-10,-23,-68,-28,62,-94],[-50,77,-39,-57,15,71,44,13,-53],[-30,43,-92,-94,42,37,95,7,19],[-1,92,-85,20,-53,-16,31,-95,4],[-62,49,0,53,-93,-61,-49,86,97],[62,-26,-1,-38,59,-93,-93,12,-90],[78,85,90,89,-65,5,48,40,-86],[-79,-68,-89,90,-40,47,68,-25,92]]
# A = [[2,3,6,7],[2,3,4,5]]
# A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
A = [[1, 2],[1, 2],[1, 2]]
print(sol.solve(A)) # [15, 10, 13, 16]