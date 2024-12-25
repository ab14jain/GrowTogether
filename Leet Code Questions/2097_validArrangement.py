from collections import defaultdict


class Solution:
    def __init__(self):
        self.adj = defaultdict(list)
        self.inDegree = defaultdict(int)
        self.outDegree = defaultdict(int)

    def get_start_point(self):
        start_node = None
        for node in self.outDegree:
            if self.outDegree[node] - self.inDegree[node] == 1:
                return node  
            if self.outDegree[node] > 0:
                start_node = node
        return start_node  
    
    def get_eulerian_path(self, curr, eulerian_path):
        while self.outDegree[curr] > 0:
            self.outDegree[curr] -= 1
            next_node = self.adj[curr][self.outDegree[curr]]
            self.get_eulerian_path(next_node, eulerian_path)
        eulerian_path.append(curr)

    def validArrangement(self, pairs):
        for from_node, to_node in pairs:
            self.adj[from_node].append(to_node)
            self.outDegree[from_node] += 1
            self.inDegree[to_node] += 1

        start_node = self.get_start_point() 

        eulc_path = []
        self.get_eulerian_path(start_node, eulc_path)

        ans = []
        for i in range(len(eulc_path) - 1, 0, -1):
            ans.append([eulc_path[i], eulc_path[i - 1]])
        return ans
        
          
    
s=Solution()
print(s.validArrangement([[1,2],[2,3],[3,4],[1,4]])) # [[1,2],[2,3],[3,4],[1,4]]
print(s.validArrangement([[1,2],[2,3],[3,4],[4,1]])) # [[1,2],[2,3],[3,4],[4,1]]
print(s.validArrangement([[1,2],[2,3],[3,4],[4,5],[5,1]])) # [[1,2],[2,3],[3,4],[4,5],[5,1]]