#https://www.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1
class Solution:

    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
        # Approach 1
        # return s1 in s2 + s2
        # if len(s1) != len(s2):
        #     return False
        # s1 = s1 + s1
        # return s2 in s1

        # Approach 2
        # return len(s1) == len(s2) and s1 in s2 + s2
        # n = len(s1)
        # for i in range(n):
        #     if s1 == s2:
        #         return True
        #     s1 = s1[-1] + s1[:-1]

        # return False

        # Approach 3
        # lst1 = list(s1)
        # n = len(s1)
        # i = 1

        # while i <= n:
        #     first = lst1[0]
        #     j = 0
        #     while j < n-1:
        #         lst1[j] = lst1[j+1]
        #         j += 1

        #     lst1[j] = first

        #     if "".join(lst1) == s2:
        #         return True

        #     i += 1

        # return False

        # Approach 4
        # using KMP algorithm

        def computeLPS(pat):
            n = len(pat)
            lps = [0] * n
            patLen = 0
            lps[0] = 0
            i = 1
            while i < n:
                if pat[i] == pat[patLen]:
                    patLen += 1
                    lps[i] = patLen
                    i += 1
                else:
                    if patLen != 0:
                        patLen = lps[patLen - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        if len(s1) != len(s2):
            return False
        
        txt = s1 + s1
        pat = s2
        n = len(txt)
        m = len(pat)
        lps = computeLPS(pat)
    
        i = 0 
        j = 0
        while i < n:
            if pat[j] == txt[i]:
                j += 1
                i += 1

            if j == m:
                return True
            elif i < n and pat[j] != txt[i]:                
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return False

    
s=Solution()
print(s.areRotations("ABCD","CDAB")) #1
print(s.areRotations("AAB","AB")) #0
print(s.areRotations("AAB","BAA")) #1
print(s.areRotations("AAB","ABA")) #1