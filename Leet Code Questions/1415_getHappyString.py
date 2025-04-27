from collections import deque


class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        q = deque()

        q.append('a')
        q.append('b')
        q.append('c')
        ans = []
        while q:
            curr = q.popleft()
            if len(curr) == n:
                ans.append(curr)
                continue
                
            if curr[-1] == 'a':                
                q.append(curr+'b')
                q.append(curr+'c')
            elif curr[-1] == 'b':               
                q.append(curr+'a')
                q.append(curr+'c')
            elif curr[-1] == 'c':
                q.append(curr+'a')
                q.append(curr+'b')

        if k > len(ans):
            return ""
        return ans[k-1]

s=Solution()
print(s.getHappyString(1,3))
print(s.getHappyString(1,4))
print(s.getHappyString(3,9))