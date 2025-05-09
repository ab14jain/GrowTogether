class Solution:    

    def dfs (self, row, col, grid, dp, m, n):
        if(dp[row][col] != -1):
            return dp[row][col]

        moves = [-1,0,1]
        count = 0
        for move in moves:
            r = row + move
            c = col + 1
            if r >= 0 and r < m and c >= 0 and c < n and grid[r][c] > grid[row][col]:
                count = max(count, (1 + self.dfs(r,c,grid,dp, m, n)))
        
        dp[row][col] = count
        return count
    
    def maxMoves(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0        

        dp = [[-1]*n for _ in range(m)]

        for row in range(m):
            result = max(result, self.dfs(row, 0, grid,dp, m, n))
        
        return result        


s=Solution()

print(s.maxMoves([[1000000,92910,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068],
                  [1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118]])) # 2
# print(s.maxMoves([[1,2,3],[4,5,6],[7,8,9]])) # 0
# print(s.maxMoves([[1,10,6,7,9,10,4,9]])) # 3