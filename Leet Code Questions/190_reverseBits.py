class Solution:
    def reverseBits(self, n: int) -> int:        
        binary_32_bit = list(format(n, '032b'))
        len_arr_n = len(binary_32_bit)
        i = 0
        j = len_arr_n - 1
        
        while i < j:
            temp = binary_32_bit[i]
            binary_32_bit[i] = binary_32_bit[j]
            binary_32_bit[j] = temp

            i += 1
            j -= 1
        
        bin_str = "".join(binary_32_bit)
        ans = int(bin_str,2)
        return ans


s=Solution()
print(s.reverseBits(43261596)) # 964176192
print(s.reverseBits(4294967293)) # 3221225471
print(s.reverseBits(0)) # 0
print(s.reverseBits(1)) # 2147483648
print(s.reverseBits(2147483648)) # 1
print(s.reverseBits(3)) # 3221225471