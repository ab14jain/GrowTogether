class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xor = 0
        for num in nums:
            xor ^= num
        
        bit_str = bin(xor)[2:]
        
        first_set_bit_index = 0
        
        for i in bit_str[::-1]:
            if i == '0':
                first_set_bit_index += 1
            else:
                break

        set_numbers = 0
        unset_numbers = 0
        for num in nums:
            if num == num | (1 << first_set_bit_index):
                set_numbers ^= num
            else:
                unset_numbers ^= num

        return [set_numbers, unset_numbers]