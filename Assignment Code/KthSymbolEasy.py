from collections import deque


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        q = deque()
        ans = []
        q.append('0')
        while A > 0:
            ans.append("".join(q))
            size = len(q)
            while size:
                char = q.popleft()                
                if char == '0':
                    q.append('0')
                    q.append('1')
                else:
                    q.append('1')
                    q.append('0')

                size -= 1
            A -= 1
        
        return ans[A-1][B]
    

s=Solution()
# print(s.solve(3,0))
# print(s.solve(4,4))
print(s.solve(12,2047))
print(s.solve(14,4))