#https://www.scaler.com/academy/mentee-dashboard/class/325342/homework/problems/1226/?navref=cl_pb_nv_tb

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # r = 0
        # n = len(A)
        # count = 0
        # for i in range(n):
        #     curr_set = set()
        #     curr_set.add(A[i])
        #     count += 1
        #     r = i + 1
        #     while r < n:
        #         if A[r] not in curr_set:
        #             curr_set.add(A[i])
        #             r += 1
        #             count += 1
        #         else:
        #             break            
            

        # return count

        # [1,1,3]
        #  l
        #  r
        l = 0
        r = 0    
        n = len(A)
        h_map = {}
        ans = 0
        MOD = 1000000007
        while r < n:
            if A[r] in h_map:
                while l < r:
                    if A[l] == A[r]:                        
                        l += 1
                        break
                    
                    del h_map[A[l]]
                    l += 1               
            else:
                h_map[A[r]] = 1
            
            ans = (ans+(r-l+1))%MOD
            r += 1          

        return ans%MOD


s=Solution()
print(s.solve([93,9,12,32,97,75,32,77,40,79,61,42,57,19,64,16,86,47,41,67,76,63,24,10,25,96,1,30,73,91,70,65,53,75,5,19,65,6,96,33,73,55,4,90,72,83,54,78,67,56,8,70,43,63]))
#775
print(s.solve([1,1,3]))
print(s.solve([2,1,2]))