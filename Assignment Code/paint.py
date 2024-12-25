#https://www.scaler.com/academy/mentee-dashboard/class/325324/assignment/problems/271?navref=cl_tt_lst_nm

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):       

        C = [i*B for i in C]
        n = len(C)

        low = max(C)
        high = sum(C)
        mod = 10000003

        while low < high:
            mid = low + (high - low)//2
            painters = 1
            curr = 0

            for i in range(n):
                task_cost = C[i]
                if curr + task_cost > mid:
                    painters += 1
                    curr = task_cost
                else:
                    curr += task_cost

            if painters <= A:
                high = mid
            else:
                low = mid + 1
            
        return (low%mod)

# Time complexity: O(nlogn)

# Space complexity: O(1)

s=Solution()
print(s.paint(2, 5, [1, 10])) # 50
print(s.paint(10, 1, [1, 8, 11, 3])) # 11
            
            