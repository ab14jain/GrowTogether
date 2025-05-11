#https://www.scaler.com/academy/mentee-dashboard/class/325380/assignment/problems/125076?navref=cl_tt_nv

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def WaysToClimb(self, A):

        ans = []
        def path(steps,steps_count,ans):
            if steps_count > A:
                return
            if steps_count  == A:
                ans.append("".join(steps))

            steps.append("1")
            path(steps,steps_count+1,ans)
            steps.pop()

            steps.append("2")
            path(steps,steps_count+2,ans)
            steps.pop()

        path([],0,ans)

        return ans
    
s=Solution()
print(s.WaysToClimb(4))