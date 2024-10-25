class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        j = 0
        n = len(s)
        s_arr = list(s)
        while j <= n:
            if j == n or s_arr[j] == " ":  
                space_j = j              
                while i < j:
                    temp = s_arr[j - 1]
                    s_arr[j - 1] = s_arr[i]
                    s_arr[i] = temp
                    i += 1
                    j -= 1
                i = space_j + 1
                j = i
            else:
                j += 1
        
        return "".join(s_arr)
        

# Time complexity: O(n)
# Space complexity: O(n)
# where n is the length of the input string s

s = Solution()
print(s.reverseWords("Let's take LeetCode contest")) # "s'teL ekat edoCteeL tsetnoc"
print(s.reverseWords("Mr Ding")) # "rM gniD"    
print(s.reverseWords("Let'stakeLeetCodecontest")) # "rM gniD"    