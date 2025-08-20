from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        bin_arr = bin(n)[2:]
        bin_arr = bin_arr[::-1]

        power = []
        for i in range(len(bin_arr)):
            if bin_arr[i] == '1':
                power.append(2**i)

        
        prefix_sum = [0]*len(power)
        prefix_sum[0] = power[0]
        for i in range(1, len(power)):
            prefix_sum[i] = prefix_sum[i-1] * power[i]
            
        result = []
        for i in queries:
            left = i[0]
            right = i[1]
            if left == 0:
                result.append(prefix_sum[right] % 1000000007)
            else:
                result.append((prefix_sum[right] // prefix_sum[left-1]) % 1000000007)

        return result
    
s=Solution()
print(s.productQueries(15, [[0,1],[2,2],[0,3]])) # [2,4,60]
print(s.productQueries(2, [[0,0]])) # [2]
print(s.productQueries(1, [[0,0]])) # [1]
