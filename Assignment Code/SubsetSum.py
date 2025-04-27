#https://www.scaler.com/academy/mentee-dashboard/class/325380/assignment/problems/124896?navref=cl_tt_nv

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def SubsetSum(self, A, B):

        # A = [3, 34, -3, 12, 5, 2]
        # B = 9
        n = len(A)
        ans = []
        def has_sum(arr, idx, desired_sum, subset, ans):

            if idx > n - 1:
                if sum(subset) == B:
                    cpy = subset[:]
                    ans.append("#".join(map(str,cpy)))
                return

            
            #print(sum(subset))
            if sum(subset) == B:
                cpy = subset[:]
                ans.append("#".join(map(str,cpy)))
                return
            
            subset.append(arr[idx])
            has_sum(arr, idx+1, desired_sum, subset, ans)
            subset.pop()
            has_sum(arr, idx+1, desired_sum, subset, ans)


        has_sum(A, 0, B, [], ans)

        return 1 if len(ans) > 0 else 0
        

s=Solution()
print(s.SubsetSum([-5, 3], 0))
# print(s.SubsetSum([3, 34, -3, 12, 5, 4], 9))
# print(s.SubsetSum([-8, 34, 4, 0, -5, -2], -20))