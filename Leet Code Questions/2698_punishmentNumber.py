class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def digit_sum_partition(i, curr, target, num):            
            if i == len(num) and curr == target:
                return True

            for j in range(i, len(num)):
                num[i:j+1]
                if digit_sum_partition(j+1, curr+int(num[i:j+1]), target, num):
                    return True
            
            return False

        punishment_num = 0
        for i in range(1,n+1):  
            if digit_sum_partition(0, 0, i, str(i*i)):
                punishment_num += (i*i)
        return punishment_num
    

s=Solution()
print(s.punishmentNumber(10))
print(s.punishmentNumber(37))