class Solution:
    def finalString(self, s: str) -> str:
        i = 0
        j = 0
        n = len(s)
        s_arr = list(s)
        while j < n:
            if s_arr[j] == "i":  
                space_j = j                             
                while i < j:
                    temp = s_arr[j - 1]
                    s_arr[j - 1] = s_arr[i]
                    s_arr[i] = temp
                    i += 1
                    j -= 1
                temp_str_pre = s_arr[0:space_j]
                temp_str_post = s_arr[space_j+1:n] 
                s_arr = temp_str_pre + temp_str_post + ['']                
                i = 0
                j = space_j
                          
            else:
                j += 1
        
        return "".join(s_arr)

# Time complexity: O(n)
# Space complexity: O(n)
# where n is the length of the input string s

s = Solution()
print(s.finalString("string")) # "strng"
print(s.finalString("striing")) # "strng"
print(s.finalString("striiing")) # "rtsng"
print(s.finalString("striiiing")) # "strng"
