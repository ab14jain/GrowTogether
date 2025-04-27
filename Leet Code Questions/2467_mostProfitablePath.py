from collections import defaultdict, deque
from typing import List


class Solution:    

    # def findBobPath(self, adj: List[List[int]], bob: int, parent: int, curr_path: List[int], bob_path: List[int]) -> bool:
    #     if bob == 0:
    #         bob_path.extend(curr_path)
    #         return True
    #     curr_path.append(bob)
    #     for nbr in adj[bob]:
    #         if nbr != parent and self.findBobPath(adj, nbr, bob, curr_path, bob_path):
    #             return True
    #     curr_path.pop()
    #     return False

    # def findMaxIncomeForAlice(self, adj: List[List[int]], alice: int, parent: int, amount: List[int]) -> int:
    #     max_income = float('-inf')
    #     for nbr in adj[alice]:
    #         if nbr != parent:
    #             income = self.findMaxIncomeForAlice(adj, nbr, alice, amount)
    #             if income + amount[alice] > max_income:
    #                 max_income = income + amount[alice]
    #     return max_income if max_income != float('-inf') else amount[alice]

    # def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
    #     n = len(amount)
    #     adj = [[] for _ in range(n)]
    #     for edge in edges:
    #         adj[edge[0]].append(edge[1])
    #         adj[edge[1]].append(edge[0])

    #     curr_path, bob_path = [], []
    #     self.findBobPath(adj, bob, -1, curr_path, bob_path)

    #     size = len(bob_path)
    #     i = 0
    #     for i in range(size // 2):
    #         amount[bob_path[i]] = 0
    #     if size % 2 == 1:
    #         amount[bob_path[i]] = 0
    #     else:
    #         amount[bob_path[i]] //= 2

    #     return self.findMaxIncomeForAlice(adj, 0, -1, amount)

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
               
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        bob_path = {}

        def dfs(src, prev, time):
            if src == 0:
                bob_path[src] = time
                return True
            
            for nbr in adj[src]:
                if nbr == prev:
                    continue

                if dfs(nbr, src, time+1):
                    bob_path[src] = time
                    return True

            return False
        dfs(bob, -1, 0)

        q = deque([(0, 0, -1, amount[0])])
        res = float('-inf')

        while q:
            node, time, parent, profit = q.popleft()         
            
            for nbr in adj[node]:
                if nbr == parent:
                    continue
                nbr_profit = amount[nbr]
                nbr_time = time + 1
                if nbr in bob_path:
                    if nbr_time > bob_path[nbr]:
                        nbr_profit = 0
                    
                    if nbr_time == bob_path[nbr]:
                        nbr_profit = nbr_profit // 2

                q.append((nbr, nbr_time, node, profit+nbr_profit))
                if len(adj[nbr]) == 1:
                    res = max(res, profit+nbr_profit)
        return res


s=Solution()
print(s.mostProfitablePath([[0,1],[1,2],[1,3],[3,4]],3,[-2,4,2,-4,6]))



        