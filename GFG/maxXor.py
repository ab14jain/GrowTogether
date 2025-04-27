class Solution:
    def maxXor(self, arr):
        #code here
        # n = len(arr)
        # max_xor = float('-inf')
        # for i in range(n):
        #     for j in range(i+1, n):
        #         max_xor = max(max_xor, arr[i]^arr[j])

        # return max_xor

        res = 0
        mask = 0

        # to store all unique bits
        s = set()

        for i in range(30, -1, -1):

            # set the i-th bit in mask
            mask |= (1 << i)

            for num in arr:

                # keep prefix of all elements
                # till the i-th bit
                s.add(num & mask)

            cur = res | (1 << i)

            for prefix in s:
                if cur ^ prefix in s:
                    res = cur
                    break

            s.clear()

        return res
    
s=Solution()
print(s.maxXor( [25, 10, 2, 8, 5, 3]))
print(s.maxXor( [1, 2, 3, 4, 5, 6, 7]))