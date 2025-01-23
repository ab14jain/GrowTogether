class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(1,n):
            # Update the row with the previous row values, if the current cell is 1, assume as histogram
            for j in range(m):
                if matrix[i][j] == "1":
                    matrix[i][j] = int(matrix[i-1][j]) + 1  
                else:
                    matrix[i][j] = 0  


        # Function to find the largest rectangle in a histogram
        def largestRectangleArea(matrix):
            n = len(matrix)
            NSL = [-1]*len(matrix)
            NSR = [n]*n

            stack = []

            for i in range(n):
                while stack and matrix[stack[-1]] >= matrix[i]:
                    stack.pop()

                if stack:
                    NSL[i] = stack[-1]

                stack.append(i)

            stack = []
            for i in range(n-1,-1,-1):
                while stack and matrix[stack[-1]] >= matrix[i]:
                    stack.pop()

                if stack:
                    NSR[i] = stack[-1]

                stack.append(i)


            max_area = 0
            for i in range(n):
                max_area = max(max_area, int(matrix[i])*(NSR[i]-NSL[i]-1))
            return max_area
        
        max_area = 0
        for i in range(n):
            max_area = max(max_area, largestRectangleArea(matrix[i]))
        return max_area
    

s=Solution()
print(s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))