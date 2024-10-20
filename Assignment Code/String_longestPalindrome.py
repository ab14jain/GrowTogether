class Solution:
	# @param A : string
	# @return a strings
    def longestPalindrome(self, A):             
        n=len(A)
        ans = 0
        final_l = 0
        final_r = 0
        p_array = []
        for c in range(n):
            l=c
            r=c

            while(l >= 0 and r < n):
                if (A[l] != A[r]):
                    break
                
                l -= 1
                r += 1

            
            new_range = r - l - 1
            if ans < new_range:
                ans = new_range
                final_l = l
                final_r = r

        for c in range(n):
            l=c
            r=c+1

            while(l >= 0 and r < n):
                if (A[l] != A[r]):
                    break
                
                l -= 1
                r += 1

            new_range = r - l - 1
            if ans < new_range:
                ans = new_range
                final_l = l
                final_r = r

        for k in range(final_l + 1, final_r):
            p_array.append(A[k])

        return "".join(p_array)


# Test cases
s = Solution()
print(s.longestPalindrome("abbabba")) # abbabba
print(s.longestPalindrome("aaaabaaa")) # aaabaaa
print(s.longestPalindrome("abba")) # abba
print(s.longestPalindrome("abb")) # bb
print(s.longestPalindrome("adaebcdfdcbetgg")) # bb