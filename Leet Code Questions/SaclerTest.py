class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        
        if len(A) == 1:
            if B == 1 and A[0] == C:
                return 1
            else:
                return 0
        else:
            for i in range(len(A) - B):
                sum = 0
                curr_index = 0
                while(curr_index < B):
                    sum += A[i + curr_index]
                    curr_index += 1
                
                if sum == C:
                    return 1
        
        return 0

test = Solution()
print(test.solve([1, 2, 3, 4, 5], 2, 5)) # 1
print(test.solve([1, 2, 3, 4, 5], 2, 7)) # 0
print(test.solve([1, 2, 3, 4, 5], 4, 9)) # 1
print(test.solve([1, 2, 3, 4, 5], 2, 10)) # 0
print(test.solve([1, 2, 3, 4, 5], 2, 11)) # 0
print(test.solve([1, 2, 3, 4, 5], 2, 12)) # 0
print(test.solve([1, 2, 3, 4, 5], 2, 13)) # 0
print(test.solve([1, 2, 3, 4, 5], 2, 14)) # 0
print(test.solve([1, 2, 3, 4, 5], 2, 15)) # 0
