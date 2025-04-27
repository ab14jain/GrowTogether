from collections import defaultdict
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        color_freq_map = defaultdict(int)  
        ball_color_map = {}  
        ans = []

        for i in range(n):
            ball, color = queries[i]

            
            if ball in ball_color_map:
                prev_color_ball = ball_color_map[ball]
                color_freq_map[prev_color_ball] -= 1  
                if color_freq_map[prev_color_ball] == 0:
                    del color_freq_map[prev_color_ball]  

            
            ball_color_map[ball] = color
            color_freq_map[color] += 1

            
            ans.append(len(color_freq_map))

        return ans