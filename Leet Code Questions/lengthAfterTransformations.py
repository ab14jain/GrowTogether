class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        s_arr = list(s)
        while t > 0:
            
            n = len(s_arr)
            i = 0
            temp_arr = []
           
            while i < n:
                if i < n-1 and s_arr[i] == 'z':
                    temp_arr.append('a')                    
                    temp_arr.append('b')
                    i += 2
                else:
                    temp_arr.append(s_arr[i])
                    i += 1

            s_arr = temp_arr

            
            
            t -= 1
        
        return (len(s_arr) % (10**9 + 7))