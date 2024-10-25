
import collections


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # char_counter = collections.Counter(pattern)    
        # s_array = list(s.split(" "))
        # word_counter = {}

        # for ss in s_array:
        #     if ss in word_counter:
        #         word_counter[ss] =  word_counter[ss] + 1
        #     else:
        #         word_counter[ss] = 1
                
        # if len(char_counter) != len(word_counter):
        #     return False
        # seen = []
        # for i in char_counter:
        #     temp_key = False
        #     for j in word_counter:
        #         if char_counter[i] == word_counter[j] and j not in seen:
        #             temp_key = True
        #             seen.append(j)
        #             break
            
        #     if temp_key == False:
        #         return False
        
        # return True

        i = 0
        j = 0

        word_map= {}
        s_array = list(s.split(" "))
        if len(pattern) != len(s_array):
            return False

        while i < len(pattern) and j < len(s_array):
            if pattern[i] not in word_map:
                if s_array[j] in word_map.values():
                    return False
                word_map[pattern[i]] = s_array[j]
            else:
                if word_map[pattern[i]] != s_array[j]:
                    return False
            i += 1
            j += 1
        
        return True
    

# Time complexity: O(n)
# Space complexity: O(n)
s = Solution()

pattern = "ab"
# text = "dog cat cat dog"
text = "xy"

print(s.wordPattern(pattern, text)) # True