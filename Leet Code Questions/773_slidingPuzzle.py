class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:

        start = ""
        for r in range(2):
            for c in range(3):
                start += str(board[r][c])
        
        target = "123450"
        if start == target:
            return 0
        
        moves = [[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]
        visited = set()
        visited.add(start)
        queue = [start]
        level = 0
        while queue:
            size = len(queue)
            for i in range(size):
                current = queue.pop(0)
                if current == target:
                    return level
                zero = current.index("0")
                for move in moves[zero]:
                    new_board = list(current)
                    new_board[zero],new_board[move] = new_board[move],new_board[zero]
                    new_board = "".join(new_board)
                    if new_board not in visited:
                        visited.add(new_board)
                        queue.append(new_board)
            level += 1
        
        return -1
    
s=Solution()
print(s.slidingPuzzle([[4,1,2],[5,0,3]])) # 5
# print(s.slidingPuzzle([[1,2,3],[4,0,5]])) # 1
# print(s.slidingPuzzle([[1,2,3],[5,4,0]])) # -1


                
                

