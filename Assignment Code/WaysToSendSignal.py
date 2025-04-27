class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        # res = []
        # def recur(signal, ans, count):

        #     if ans and signal == ans[-1] and ans[-1] == "ON":
        #         return 0
            
        #     if len(ans) == A:                
        #         count[0] += 1
        #         return count[0]

            
        #     ans.append(signal)            
        #     return recur("ON", ans, count) + recur("OFF", ans,count)
        
        # ans = [0]
        # total = recur("ON", ["ON"],ans) + recur("OFF", ["OFF"],ans)

        # return ans[0]
        MOD = 10**9+7
        if A == 1:
            return 2  # "0", "1"
        if A == 2:
            return 3  # "00", "01", "10"

        return (self.solve(A - 1) + self.solve(A - 2)) % MOD

s=Solution()
# print(s.solve(2))
print(s.solve(3))