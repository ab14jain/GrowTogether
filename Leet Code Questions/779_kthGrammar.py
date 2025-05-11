from collections import deque
import math


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # q = deque()
        # ans = []
        # q.append(0)
        # count = n
        # while count > 0:
        #     ans.append(q)
        #     size = len(q)
        #     while size:
        #         char = q.popleft()                
        #         if char == 0:
        #             q.append(0)
        #             q.append(1)
        #         else:
        #             q.append(1)
        #             q.append(0)

        #         size -= 1
        #     count -= 1
        
        # return ans[n-1][k-1]

        # s = '0'
        # s_bin_arr = list(bin(0)[2:])
        # count = math.ceil(n/2)
        # while count > 0:
        #     temp = []
        #     for i in s_bin_arr:
        #         # result += '1' if i == '0' else '0'
        #         if i == '0':
        #             temp.append('1')
        #         else:
        #             temp.append('0')

        #     s_bin_arr.extend(temp)
        #     count -= 1

        # next_bit = (2**n) // 2

        # if (k-1) <= next_bit:
        #     return s_bin_arr[k-1]
        # else:
        #     if k % 2 == 1:
        #         if s_bin_arr[math.ceil(k/2)] == '0':
        #             return 0
        #         else:
        #             return 1
        #     else:
        #         if s_bin_arr[math.ceil(k/2)] == '0':
        #             return 1
        #         else:
        #             return 0      

        if n == 1:
            return 0

        prev = self.kthGrammar(n-1, math.ceil(k/2))         

        if prev == 1:
            return 1 if k%2 == 1 else 0
        else:
            return 0 if k%2 == 1 else 1

s=Solution()
print(s.kthGrammar(5,30))
print(s.kthGrammar(12,297))
print(s.kthGrammar(30,29744))