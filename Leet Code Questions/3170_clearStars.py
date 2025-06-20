class Solution:
    def clearStars(self, s: str) -> str:
        
        n = len(s)
        chars = list(s)
        min_char_index = [-1]*n
        min_char_index[0] = 0

        for i in range(1, n):
            if s[i] != '*':
                if ord(s[min_char_index[i-1]]) >= ord(s[i]):
                    min_char_index[i] = i
                else:
                    min_char_index[i] = min_char_index[i-1]
            else:
                min_char_index[i] = min_char_index[i-1]

        print(min_char_index)
        for i in range(n):
            if s[i] == '*':
              chars[min_char_index[i]] = '#'

        
        return "".join(chars).replace('#', '').replace('*', '')

s=Solution()
print(s.clearStars("d*o**"))
# print(s.clearStars("aaba*"))
# print(s.clearStars("aababc*"))
            

        