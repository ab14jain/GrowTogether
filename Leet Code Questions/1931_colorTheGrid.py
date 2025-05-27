class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:

        coll_states = []
        MOD = 10**9 + 7
        
        def recur_state(i, prev, ans):

            if i == m:
               coll_states.append(ans)
               return

            if prev == "R":
               recur_state(i+1, "G", ans+"G") 
               recur_state(i+1, "B", ans+"B") 
            elif prev == "G":
               recur_state(i+1, "R", ans+"R") 
               recur_state(i+1, "B", ans+"B")
            elif prev == "B":
                recur_state(i+1, "R", ans+"R") 
                recur_state(i+1, "G", ans+"G")
            else:
                recur_state(i+1, "R", ans+"R") 
                recur_state(i+1, "G", ans+"G")
                recur_state(i+1, "B", ans+"B")

        recur_state(0, "", "")

        def solve(rem_col, prev_idx):
            
            if rem_col == 0:
                return 1
            
            if dp[rem_col][prev_idx] != -1:
               return dp[rem_col][prev_idx]
            
            ways = 0
            pre_state = coll_states[prev_idx]


            for i in range(len(coll_states)):
                if i == prev_idx:
                    continue

                curr = coll_states[i]
                isvalid = True

                for j in range(m):
                    if pre_state[j] == curr[j]:
                        isvalid = False
                        break

                
                if isvalid:
                    ways = (ways + solve(rem_col-1, i))%MOD

            dp[rem_col][prev_idx] = ways
        
            return ways




        # "['RGR', 'RGB', 'RBR', 'RBG', 'GRG', 'GRB', 'GBR', 'GBG', 'BRG', 'BRB', 'BGR', 'BGB']"
        
        state_count = len(coll_states)
        count = 0
        dp = [[-1]*(state_count+1) for _ in range(n)]

        for i in range(state_count):
            count = (count + solve(n-1, i))%MOD

        # for k in range(1, n):
        #     for i in range(state_count):
        #         for j in range(i+1, state_count):
        #             if coll_states[i] != coll_states[j]:
        #                 count += 1

        return count
    
s=Solution()
# print(s.colorTheGrid(1,1))
# print(s.colorTheGrid(1,2))
# print(s.colorTheGrid(1,3))
print(s.colorTheGrid(2,37))
print(s.colorTheGrid(5,5))