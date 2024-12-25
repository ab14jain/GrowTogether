class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        rem = []
        n = len(A)        

        for i in range(n):
            rem.append(A[i] % B)
        
        rem_count = [0]*B

        for i in range(n):
            r2 = (B - rem[i]) % B
            count += rem_count[r2]
            rem_count[rem[i]] += 1   

        count = count % (10**9 + 7)
        return count


s=Solution()
print(s.solve([1,2,3,4,5],2)) # 4
# print(s.solve([5, 17, 100, 11],28)) # 1
# print(s.solve([5, 17, 100, 11],28)) # 1