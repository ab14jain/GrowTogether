class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):

        # row = len(A)
        # column = len(A[0]) 
        # coll_sum =[]
        # for c in range(column):
        #     r = 0
        #     col_sum = 0
        #     while(r < row):
        #         col_sum += A[r][c]
        #         r += 1
            
        #     coll_sum.append(col_sum)

        # return coll_sum

        # input_d = input().split(" ")
        
        # row = int(input_d[0])
        # column = int(input_d[1])

        # diagnoal_sum = 0
        # r = 0
        # c = 0
        # while r < row:
        #     diagonal_index = r * column + c + 2
        #     diagnoal_sum += int(input_d[diagonal_index])
        #     r += 1
        #     c += 1

        # return diagnoal_sum


        row = len(A)
        diagnoal_sum = 0
        r = 0
        while r < row:            
            diagnoal_sum += A[r][r]
            r += 1

        return diagnoal_sum
            



sol = Solution()
A = [[47,-59,20,33,20,-47,-87,-59,85],[8,-67,48,-10,-23,-68,-28,62,-94],[-50,77,-39,-57,15,71,44,13,-53],[-30,43,-92,-94,42,37,95,7,19],[-1,92,-85,20,-53,-16,31,-95,4],[-62,49,0,53,-93,-61,-49,86,97],[62,-26,-1,-38,59,-93,-93,12,-90],[78,85,90,89,-65,5,48,40,-86],[-79,-68,-89,90,-40,47,68,-25,92]]
print(sol.solve(A)) # [15, 10, 13, 16]