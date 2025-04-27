class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        
        def recur(i, ways, arr):

            if i == A:
                ways += 1

            
            pair = recur(i+1, )
            alone = recur()