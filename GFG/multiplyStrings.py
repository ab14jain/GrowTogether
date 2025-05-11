class Solution:
    def multiplyStrings(self, s1, s2):
        # code here
        # return the product string

        sum = 0
        n = len(s1)
        m = len(s2)

        if n < m:    
            for i in range(n):
                prod = int(s1[i])
                for j in range(m):
                    prod *= int(s2[j])
                
                sum += prod
        else:
            for i in range(m):
                prod = int(s2[i])
                for j in range(n):
                    prod *= int(s1[j])
                
                sum += prod

        return str(sum)
    
s=Solution()
print(s.multiplyStrings("0033", "2"))

