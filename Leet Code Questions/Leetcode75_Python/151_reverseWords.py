class Solution:
    def reverseWords(self, s: str) -> str: 
        reverse_str = []       
        for s in s.split(" ")[::-1]:                   
            if s != "":
                reverse_str.append(s)
        return " ".join(reverse_str)
    


test = Solution()
print(test.reverseWords("the sky is blue")) # "blue is sky the"
print(test.reverseWords("  hello world  ")) # "world hello"
print(test.reverseWords("a good   example")) # "example good a"
print(test.reverseWords("  Bob    Loves  Alice   ")) # "Alice Loves Bob"