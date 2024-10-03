import math
from string import ascii_lowercase


class Solution:
    def kthCharacter(self, k: int) -> str:    
        # word ='a'
        # n = math.ceil(math.sqrt(k))
        # for i in range(n):
        #     temp_word = word
        #     for j in word:
        #         temp_word = temp_word + chr(ord(j) + 1)
            
        #     word = temp_word
                        
        # return word[k-1]
        # print((k-1).bit_count())
        # return ascii_lowercase[(k-1).bit_count()]
        lowercase_letter = 'abcdefghijklmnopqrstuvwxyz'
        bit = bin(k -1)
        bit_count = 0

        for i in bit:
            if i == '1':
                bit_count += 1

        char = lowercase_letter[bit_count]
        return char

s = Solution()
print(s.kthCharacter(11))  # k