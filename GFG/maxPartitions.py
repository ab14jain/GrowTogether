#https://www.geeksforgeeks.org/problems/maximize-partitions-in-a-string/1

class Solution:
    def maxPartitions(self , s):
        # code here
        mp = {}
        n = len(s)
        for i in range(n):         
            mp[s[i]] = i

        i = 0        
        end = mp[s[0]]
        count = 0
        while i < n:
            end = max(end, mp[s[i]])
            if i == end:
                count += 1
            i += 1
        
        return count


s=Solution()
print(s.maxPartitions("aaa"))
print(s.maxPartitions("acbbcc"))
print(s.maxPartitions("ababcbacadefegdehijhklij"))
