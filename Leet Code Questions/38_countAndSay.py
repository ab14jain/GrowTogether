class Solution:
    def countAndSay(self, n: int) -> str:
        
        # def intToMap(st):
        #     mp = []
        #     n = len(st)
            
        #     if n == 1:
        #         return [['1', 1]]
        #     prev = st[0]
        #     i = 1
        #     count = 1
        #     while i < n:
                
        #         while i < n and prev == st[i]:
        #            prev = st[i]
        #            count += 1
        #            i += 1
                
        #         mp.append([prev, count])
        #         if i < n:
        #             prev = st[i]
        #         count = 1
        #         i += 1
            
        #     return mp
        
        # def mapToInt(mp):

        #     st = []
        #     n = len(mp)
        #     for i in range(n):
        #         st.append(str(mp[i][1]))
        #         st.append(mp[i][0])

        #     return "".join(st)
        # print(mapToInt(intToMap("21")))

        # prev = "1"
        # res_st = "1"
        # res_mp = []
        # for i in range(1, n):    
        #     if i % 2 == 1:
        #         res_st = intToMap("1" + res_st)     
        #         res_mp = mapToInt(res_st)
        #     else:
        #         res_st = mapToInt(res_st)
        #         res_st = intToMap("1" + res_st)  
        #     # res_st = mapToInt(intToMap(res_st))
        #     # res_st = "1" + res_st

        # return res_st


        if n == 1:
            return "1"
        
        prev = self.countAndSay(n - 1)
        result = ""
        count = 1

        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                result += str(count) + prev[i - 1]
                count = 1
        
        result += str(count) + prev[-1]
        return result
s=Solution()
print(s.countAndSay(4))



            