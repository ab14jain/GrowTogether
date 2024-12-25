from collections import defaultdict, deque


class Solution:
    def minimumDiameterAfterMerge(self, edges1: list[list[int]], edges2: list[list[int]]) -> int:

        m = len(edges1) + 1
        n = len(edges2) + 1

        adj_list1 = defaultdict(list)
        adj_list2 = defaultdict(list)

        for u, v in edges1:
            adj_list1[u].append(v)
            adj_list1[v].append(u)
        
        for u, v in edges2:
            adj_list2[u].append(v)
            adj_list2[v].append(u)

        #get diameter of using dfs from node 0

        def get_diameter(adj_list):
            def dfs(node, parent, depth):
                nonlocal max_depth, max_node
                if depth > max_depth:
                    max_depth = depth
                    max_node = node
                
                for nei in adj_list[node]:
                    if nei != parent:
                        dfs(nei, node, depth + 1)
            
            max_depth = 0
            max_node = 0
            dfs(0, -1, 0)
            
            max_depth = 0
            dfs(max_node, -1, 0)
            
            return max_depth
        

        dia1 = get_diameter(adj_list1)
        dia2 = get_diameter(adj_list2)
        
        return max(dia1, dia2, (dia1 + 1) // 2 + (dia2 + 1) // 2 + 1)
    

# Time: O(N)
# Space: O(N)

# 1
# 2 3
# 4 5 6 7
# 8 9 10 11 12 13 14 15
# 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
s=Solution()
tree1 = [(0, 1), (1, 2), (1, 3)]  # Tree 1 edges
tree2 = [(0, 1), (1, 2)]  # Tree 2 edges
print(s.minimumDiameterAfterMerge(tree1, tree2))  # Output the minimum diameter

    