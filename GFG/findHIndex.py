# https://www.geeksforgeeks.org/problems/find-h-index--165609/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card

#User function Template for python3
class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here

        n = len(citations)
        freq = [0] * (n + 1)

        for i in range(n):
            if citations[i] >= n:
                freq[n] += 1
            else:
                freq[citations[i]] += 1
        
        sum = 0
        id = n

        while id >= 0:  
            sum += freq[id]
            if sum >= id:
                return id
            id -= 1
        
        return 0


s=Solution()
print(s.hIndex([5, 0, 2, 0, 2])) # 2
print(s.hIndex([6, 0, 3, 5, 3])) # 2
print(s.hIndex([4, 4, 0, 0])) # 2
print(s.hIndex([1, 3, 1])) # 1
print(s.hIndex([1, 1, 1])) # 1
print(s.hIndex([1, 1, 1, 1])) # 1
print(s.hIndex([1, 1, 1, 1, 1])) # 1