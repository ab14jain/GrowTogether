class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:

        n = len(s)
        prefix_sum = [0]*n
        for shift in shifts:
            start = shift[0]
            end = shift[1]
            direction = shift[2]

            if direction == 0:
                prefix_sum[start] -= 1
            else:
                prefix_sum[start] += 1

            if end+1 < n:
                prefix_sum[end+1] += 1 if direction == 0 else -1
        
        for i in range(1,n):
            prefix_sum[i] += prefix_sum[i-1]

        result = []
        for i in range(n):
            result.append(chr((ord(s[i])-97+prefix_sum[i])%26+97))
        return "".join(result)
    
s=Solution()
print(s.shiftingLetters("abc",[[0,1,0],[1,2,1],[0,2,1]])) # "ace"
print(s.shiftingLetters("abc",[[0,1,0],[1,2,1],[0,3,0]])) # "cee"
print(s.shiftingLetters("dztz",[[0,0,0],[1,1,1]])) # "catz"
print(s.shiftingLetters("dztz",[[0,0,0],[1,1,1],[0,0,1]])) # "dbua"