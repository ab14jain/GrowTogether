class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A = list(set(A))
        if len(A) > 1:
            max1 = A[0]
            max2 = A[1]

            if max2 > max1:
                max1 = max2

            for i in A:     
                if i > max1: 
                    max2 = max1
                    max1 = i
                elif i > max2 and i != max1:
                    max2 = i

            return max2
        else: 
            return -1

s= Solution()
# print(s.solve([13,7,16,18,14,17,18,8,10])) # 4
print(s.solve([10,10,9,8,1])) # 9
print(s.solve([4,4,4,4])) # -1
