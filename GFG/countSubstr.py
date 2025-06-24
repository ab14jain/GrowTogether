from collections import defaultdict


class Solution:
    def countSubstr (self, s, k):
        # Code here

        # Approach 1 - Brute Force 
        # TLE => 1010 /1117
        # Time Complexity	O(n³)
        # Space Complexity	O(k)
 
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
        # Time Complexity	O(n²)
        # Space Complexity	O(k)
 
        # n = len(s)
        # count = 0
        # for i in range(n):
        #     mp = defaultdict(int)
        #     for j in range(i,n):
        #         mp[s[j]] += 1
        #         if len(mp) == k:
        #             count += 1


        # return count
    
        # Approach 3: Optimized
        
        def count_k_substr(k):
            
            n = len(s)
            
            l = 0
            r = 0
            mp = defaultdict(int)
            count = 0
            while r < n:
                mp[s[r]] += 1
                while len(mp) > k:                    
                    mp[s[l]] -= 1
                    if mp[s[l]] == 0:
                        mp.pop(s[l])
                    l += 1
                

                count += r-l+1
                r += 1

            return count


        
        return count_k_substr(k) - count_k_substr(k-1)



            
                

                



        
        
s=Solution()
print(s.countSubstr("abc", 2))
print(s.countSubstr("aba", 2))
print(s.countSubstr("aa", 1))


