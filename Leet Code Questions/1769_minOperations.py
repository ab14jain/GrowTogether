class Solution:
    def minOperations(self, boxes: str) -> list[int]:


        # n = len(boxes)
        # ans = [0]*n
        # for i in range(n):            
        #     for j in range(n):
        #         if boxes[j] == '1':
        #             ans[i] += abs(i-j)
        
        # return ans

        n = len(boxes)
        total_balls = 0
        t_sum = 0
        ans = [0]*n
        for i in range(n):            
            if boxes[i] == '1':
                total_balls += 1
                t_sum += i

        left_ones_contri = 0
        right_ones_contri = total_balls

        # ans[0] = t_sum
        # if boxes[0] == '1':
        #     left_ones_contri += 1
        #     right_ones_contri -= 1

        for i in range(n):   
            if i == 0:
                ans[i] = t_sum
            else:   
                t_sum = t_sum + left_ones_contri - right_ones_contri
                ans[i] = t_sum

            if boxes[i] == '1':
                left_ones_contri += 1
                right_ones_contri -= 1

        return ans      


s=Solution()
print(s.minOperations("110")) # [1,1,3]
print(s.minOperations("001011")) # [11,8,5,4,3,4]
        