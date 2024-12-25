class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        # if k == 0:
        #     return 0

        # if n < 3:
        #     return -1       
        
        char_map = {'a':0,'b':0,'c':0}
        for i in range(len(s)):
            char_map[s[i]] += 1       

        if char_map['a'] < k or char_map['b'] < k or char_map['c'] < k:
            return -1
        
        i = 0
        j = 0
        not_deleted_window = 0
        while j < n:
            
            if s[j] == 'a':
                char_map['a'] -= 1
            elif s[j] == 'b':
                char_map['b'] -= 1
            else:
                char_map['c'] -= 1
            
            while i <= j and (char_map['a'] < k or char_map['b'] < k or char_map['c'] < k):
                if s[i] == 'a':
                    char_map['a'] += 1
                elif s[i] == 'b':
                    char_map['b'] += 1
                else:
                    char_map['c'] += 1
                i += 1
            

            not_deleted_window = max(not_deleted_window, j - i + 1)
            j += 1

        
        return (n - not_deleted_window)       

        
# Time complexity: O(n)
# Space complexity: O(1)

s=Solution()
print(s.takeCharacters("aaabb", 3)) # -1
print(s.takeCharacters("abaccc", 3)) # -1
print(s.takeCharacters("abcabc", 3)) # -1
print(s.takeCharacters("aaabb", 2)) # -1
print(s.takeCharacters("aaabb", 1)) # -1
print(s.takeCharacters("aaabb", 0)) # 0
