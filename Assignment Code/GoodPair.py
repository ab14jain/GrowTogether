
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dictA = {i: 0 for i in A}
        for i in A:
            dictA[i] += 1
                        
        for i in A:
            dictA[i] -= 1
            diff = abs(i - B)
            if diff in dictA and dictA[diff] > 0:
                return 1

        return 0    
        
s= Solution()
print(s.solve([1, 2, 3, 4, 5], 3)) # 1