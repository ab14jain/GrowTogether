import time


class Solution:
    # @param A : long
    # @param B : integer
     # @return an long
    def solve(self, A, B):
        start_time = time.time()
        bit_arr = list(bin(A)[2:])
        n = len(bit_arr)
        i = 0

        while i < B:
            if bit_arr[n-i-1] == '1':
                bit_arr[n-i-1] = '0'
            
            i += 1

        
        bin_to_dec = int("".join(bit_arr),2)
        print("--- %s seconds ---" % (time.time() - start_time))
        return bin_to_dec

        #2nd Approach
        
        # temp_A = A
        # subtract = 0
        # count = 0
        # while count < B:            
        #     if A & 1 == 1:
        #         subtract += (1 << count)
        #     A = A >> 1
        #     count += 1
        # print("--- %s seconds ---" % (time.time() - start_time))
        # return temp_A - subtract
    


# Driver code
s = Solution()
print(s.solve(2147483648,4)) # 80
print(s.solve(214748,4)) # 80
print(s.solve(93,4)) # 80
print(s.solve(53,5)) # 80
print(s.solve(25,3)) # 3
print(s.solve(37,3)) # 1