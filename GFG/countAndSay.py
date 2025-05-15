# https://www.geeksforgeeks.org/problems/decode-the-pattern1138/1
class Solution:
    def countAndSay(self, n):
        # code here

        result = '1'

        for i in range(1, n):
            
            res_len = len(result)            
            start = 0
            prev = result[start]
            count = 0 
            j = 0
            while j < res_len:                
                curr = result[j]
                while curr == prev and j < res_len:                    
                    count += 1
                    prev = curr
                    j += 1
                    if j < res_len:
                        curr = result[j]
                
                result = str(count) + '' + prev
                j += 1
            
        
        return result
        

s=Solution()
print(s.countAndSay(4))



                