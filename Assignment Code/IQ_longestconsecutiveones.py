class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        str_A = list(A)
        n = len(str_A)

        no_of_ones = 0
        for i in str_A:
            if i == '1':
                no_of_ones += 1  

        if no_of_ones == n:
            return n
        
        max_seq = 0 
        for i in range(n):

            if(str_A[i] == '0'):
                l = 0
                r = 0
                j = i + 1
                while j < n:
                    if str_A[j] == '1':
                        r += 1
                    else:
                        break
                    
                    j += 1
                j = i - 1
                while j > -1:
                    if str_A[j] == '1':
                        l += 1
                    else:
                        break
                    
                    j -= 1                
                
                if l+r == no_of_ones:
                    max_seq = max(max_seq, l+r)
                else:
                    max_seq = max(max_seq, l+r+1)

        return max_seq
                
s = Solution()
# print(s.solve("000000000000000")) # 0
# print(s.solve("111111111111111")) # 15
# print(s.solve("111011101")) # 7
# print(s.solve("01110110110")) # 6
print(s.solve("00000011111111")) # 8