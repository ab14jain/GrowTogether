from collections import deque
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        queue = deque()
        freq = {}
        result = []
        
        for ch in A:            
            freq[ch] = freq.get(ch, 0) + 1
            queue.append(ch)            
            
            while queue and freq[queue[0]] > 1:
                queue.popleft()            
            
            if queue:
                result.append(queue[0])
            else:
                result.append("#")
        
        return ''.join(result)
    

# Time complexity: O(n)
# Space complexity: O(n)

s=Solution()
A="abadbc"
print(s.solve(A)) # aaaa##
A="abcabc"
print(s.solve(A)) # aaabc#
A="jpxvxivxkkthvpqhhhjuzhkegnzqriokhsgea"
print(s.solve(A)) # jjjjjjjjjjjjjjjjjjiiiiiiiiiiitttttttt
print(s.solve('xxikrwmjvsvckfrqxnibkcasompsuyuogauacjrr')) # x#iiiiiiiiiiiiiiiiwwwwwwwwwwwwwwwwwwwwww
