#https://www.scaler.com/academy/mentee-dashboard/class/313144/homework/problems/94299?navref=cl_tt_lst_nm

class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def insert(self, A, B):
        AB =  []
        for a in A:
            AB.append(a)
        AB.append(B)
        
        AB.sort(key = lambda x : x[0])
        
        s1 = AB[0][0]
        e1 = AB[0][1]
        result = []
        for i in range(1, len(AB)):
            s_curr = AB[i][0]
            e_curr = AB[i][1]
            if e1 >= s_curr and e_curr >= s1:
                e1 = max(e1, e_curr)
                s1 = min(s1, s_curr)
            else:
                result.append([s1, e1])
                s1 = s_curr
                e1 = e_curr

        result.append([s1, e1])   

        return result
    

# Test cases
s = Solution()
print(s.insert([[1, 3], [6, 9]], [2, 5])) # [[1, 5], [6, 9]]
