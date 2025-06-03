from collections import defaultdict


class Solution:
    def countSubstr (self, s, k):
        # Code here

        # Approach 1 - Brute Force 
        # TLE => 1010 /1117
 
        # n = len(s)
        # count = 0
        # for i in range(n-k+1):
        #     for j in range(k, n+1):
        #         unq = set(s[i:j])
        #         if len(unq) == k:
        #             count += 1

        # return count

        # Approach 2 - Optmized with hashmap
        # TLE => 1010 /1117
 
        n = len(s)
        count = 0
        for i in range(n):
            mp = defaultdict(int)
            for j in range(i,n):
                mp[s[j]] += 1
                if len(mp) == k:
                    count += 1


        return count
    
        # Approach 2:
        # chars_seen = set()
        # n = len(s)       

        # i = 0
        # j = 0
        
        # uniqe_count = 0    
        # freq = [0]*26   

        # while j < n:
        #     while len(chars_seen) <= k and j < n:
        #         chars_seen.add(s[j])
        #         freq[ord(s[j]) - ord('a')] += 1
        #         j += 1
            
        #     uniqe_count += ((j-i)*(j-i-1))//2
        #     i += 1
            

        # return uniqe_count


        def count(s, k):
            n = len(s)
            ans = 0

            # Use sliding window technique
            freq = [0] * 26
            distinctCnt = 0
            i = 0

            for j in range(n):

                # Expand window and add character
                freq[ord(s[j]) - ord('a')] += 1
                if freq[ord(s[j]) - ord('a')] == 1:
                    distinctCnt += 1

                # Shrink window if distinct characters exceed k
                while distinctCnt > k:
                    freq[ord(s[i]) - ord('a')] -= 1
                    if freq[ord(s[i]) - ord('a')] == 0:
                        distinctCnt -= 1
                    i += 1

                # Add number of valid substrings ending at j
                ans += j - i + 1

            return ans
        
        n = len(s)
        ans = 0

        # Subtract substrings with at most 
        # k-1 distinct characters from substrings
        # with at most k distinct characters
        ans = count(s, k) - count(s, k - 1)

        return ans

    # # Function to find the number of substrings
    # # with exactly k Distinct characters.
    # def countSubstr(s, k):
    #     n = len(s)
    #     ans = 0

    #     # Subtract substrings with at most 
    #     # k-1 distinct characters from substrings
    #     # with at most k distinct characters
    #     ans = count(s, k) - count(s, k - 1)

    #     return ans
        
s=Solution()
print(s.countSubstr("abc", 2))
print(s.countSubstr("aba", 2))
print(s.countSubstr("aa", 1))


