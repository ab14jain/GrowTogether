from collections import deque
from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        
        # def bfs(start, status, candies, keys, containedBoxes):

        #     q = deque()
        #     q.append(start)
        #     candies_count = 0
        #     visited = set()
        #     closed = set()
        #     while q:
        #         curr = q.popleft()
        #         # candies_count += candies[curr]
        #         # for cdbox in containedBoxes[curr]:
        #         #     if cdbox not in visited:
        #         #         if status[cdbox] == 1:
        #         #             # candies_count += candies[cdbox]
        #         #             visited.add(cdbox)
                        
        #         #         for key in keys[cdbox]:
        #         #             if status[key] == 0:
        #         #                 # candies_count += candies[key]
        #         #                 visited.add(key)

        #         #         q.append(cdbox)

        #         if status[curr] == 1:
        #             candies_count += candies[curr]
        #             visited.add(curr)
        #         else:
        #             closed.add(curr)

                
        #         for cdbox in containedBoxes[curr]:
        #             # if cdbox not in visited:
        #             #     if status[cdbox] == 1:
        #             #         # candies_count += candies[cdbox]
        #             #         visited.add(cdbox)
                        
        #             #     for key in keys[cdbox]:
        #             #         if status[key] == 0:
        #             #             # candies_count += candies[key]
        #             #             visited.add(key)

        #             q.append(cdbox)
                
        #         for key in keys[curr]:
        #             if key in closed:
        #                 candies_count += candies[key]
        #                 closed.remove(key)
                        
            
        #     return candies_count


        # total_candies = 0

        # for start in range(len(initialBoxes)):  
        #     total_candies = max(total_candies, bfs(start, status, candies, keys, containedBoxes))

        # return total_candies


        n = len(status)
        
        q = deque(initialBoxes)
        closed = set()
        total = 0
        
        while q:
            curr = q.popleft()
            
            if status[curr] == 0:
                closed.add(curr)
                continue
            
            for open in keys[curr]:
                status[open] = 1
                if open in closed:
                    q.append(open)
                    closed.remove(open)
            
            total += candies[curr]
            for nbr in containedBoxes[curr]:
                q.append(nbr)
        
        return total
    

s=Solution()
# print(s.maxCandies(status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]))
print(s.maxCandies(status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]))
        


