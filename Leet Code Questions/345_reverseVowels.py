class Solution:
    def reverseVowels(self, s: str) -> str:
        s_arr = list(s)
        lower_case = ['a', 'e', 'i', 'o', 'u']
        upper_case = ['A', 'E', 'I', 'O', 'U']
        l = 0
        r = len(s) - 1

        while l < r:
            if s_arr[l] in lower_case or s_arr[l] in upper_case:            
                if s_arr[r] in lower_case or s_arr[r] in upper_case:
                    temp = s_arr[l]
                    s_arr[l] = s_arr[r]
                    s_arr[r] = temp
                    l += 1
                    r -= 1
                else:
                    r -= 1
            else:
                l += 1
        
        
        return "".join(s_arr)
    

# Time complexity: O(n)
# Space complexity: O(n)
# where n is the length of the input string s

s = Solution()
print(s.reverseVowels("hello")) # "holle"
print(s.reverseVowels("leetcode")) # "leotcede"
print(s.reverseVowels("aA")) # "Aa"