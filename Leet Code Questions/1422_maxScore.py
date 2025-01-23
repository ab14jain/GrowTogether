class Solution:
    def maxScore(self, s: str) -> int:
        
        # max_score = 0
        # for i in range(1, len(s)):
        #     left = s[:i]
        #     right = s[i:]
            
        #     left_zeros = left.count('0')
        #     right_ones = right.count('1')

        #     max_score = max(max_score, left_zeros + right_ones)

        # return max_score

        max_score = 0
        prefix_one = [0] * len(s)

        for i in range(len(s)):
            if i == 0:                
                if s[i] == '1':
                    prefix_one[i] = 1
                else:
                    prefix_one[i] = 0
            else:
                prefix_one[i] = prefix_one[i - 1] + (1 if s[i] == '1' else 0)

        for i in range(1, len(s)):
            left_zeros = i - prefix_one[i - 1]
            right_ones = prefix_one[-1] - prefix_one[i - 1]

            max_score = max(max_score, left_zeros + right_ones)
                 

        return max_score
    
s=Solution()
print(s.maxScore("011101")) # 5
print(s.maxScore("00111")) # 5
print(s.maxScore("1111")) # 3
print(s.maxScore("00")) # 1
print(s.maxScore("010101")) # 4