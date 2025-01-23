
from collections import defaultdict


class Solution:

    def solve(self, A):

        mp = {}
        mp_stack = defaultdict(list)
        max_freq = -1


        def push(x):           

            mp[x] = mp.get(x, 0) + 1

            # if mp[x] in mp_stack:                
            #     mp_stack[mp[x]].append(x)
            # else:
            #     mp_stack[mp[x]] = [x]
            mp_stack[mp[x]].append(x)

            nonlocal max_freq
            max_freq = max(max_freq, mp[x])

            return -1
        
        def remove():
            nonlocal max_freq, mp, mp_stack
            if mp_stack[max_freq]:
                top_freq = mp_stack[max_freq].pop()
                mp[top_freq] -= 1
                if (len(mp_stack[max_freq]) == 0):
                    max_freq -= 1               

                return top_freq
        
        res = []
        for i in A:
            action = i[0]
            x = i[1]

            if action == 1:
                res.append(push(x))
            
            if action == 2:
                res.append(remove())

        return res
        

s = Solution()
# print(s.solve([[1,5],[1,7],[1,5],[1,7],[1,4],[1,5],[2,0],[2,0],[2,0],[2,0]]))
# print(s.solve([[1,2],[2,0],[1,2],[1,7],[2,0],[2,0],[1,4],[1,1],[1,7]]))
print(s.solve([[1,52],[2,0],[1,33],[1,73],[1,51],[1,60],[2,0],[1,59],[1,21],[1,46],[1,27],[2,0],[2,0],[1,46],[1,68],[1,88],[1,10],
               [1,84],[1,63],[1,15],[1,13],[2,0],[2,0],[2,0],[1,81],[2,0],[2,0],[2,0],[1,63]]))
