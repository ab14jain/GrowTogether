class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        result = [0]*len(B)        
        for b in range(len(B)):
            count = 0           
            r1 = B[b][0]
            r2 = B[b][1] + 1
            for a in range(r1, r2):
                if A[a] % 2 == 0:
                    count += 1 
            result[b] = count
        
        return result

test = Solution()
print(test.solve([1, 2, 3, 4, 5], [[1, 2], [3, 4]])) # [1, 1]
print(test.solve([1, 2, 3, 4, 5], [[0, 4], [2, 4]])) # [2, 1]
print(test.solve([1, 2, 3, 4, 5], [[0, 4], [0, 4]])) # [2, 2]
print(test.solve([1, 2, 3, 4, 5], [[0, 4], [0, 3]])) # [2, 2]