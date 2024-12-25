class Solution:
    def validQueries(self, text : str, pattern : str, q : int, queries : List[List[int]]) -> int:
        # code here
        
        pattern_hash = {}
        
        for i in pattern:
            if i in pattern_hash:
                pattern_hash[i] = pattern_hash[i] + 1
            else:
                pattern_hash[i] = 1
        
        count = 0
        for q in range(len(queries)):
            l = queries[q][0]
            r = queries[q][1]
            
            temp_str_hash = {}
            for i in range(len(text)):
                if i < l or i > r:
                    if text[i] in temp_str_hash:
                        temp_str_hash[text[i]] = temp_str_hash[text[i]] + 1
                    else:
                        temp_str_hash[text[i]] = 1
            
            for k in pattern_hash:
                if k in temp_str_hash:
                    temp_str_hash[k] = temp_str_hash[k] - 1
                else:
                    temp_str_hash[k] = - 1
            
            has_all_keys = True
            keysList = list(temp_str_hash.keys())
            if len(keysList) > 0:
                for m in temp_str_hash:
                    if temp_str_hash[m] < 0:
                        has_all_keys = False
                        break
            else:
                has_all_keys = False
            
            if has_all_keys:
                count += 1
                
        
        return count

# Time complexity: O(n)
# Space complexity: O(n)
#
s = Solution()
print(s.validQueries('ekskrxkgvfji', 'jvvkkf', 54, [[0, 3], [1, 3]])) # 2
