#https://www.scaler.com/academy/mentee-dashboard/class/325330/homework/problems/4366?navref=cl_tt_lst_nm

from collections import deque


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        n = len(A)

        deque_max = deque()
        deque_min = deque()
        ans_max = []
        ans_min = []
        for i in range(B):
            while deque_max and A[i] >= A[deque_max[-1]]:
                deque_max.pop()
            while deque_min and A[i] <= A[deque_min[-1]]:
                deque_min.pop()

            deque_max.append(i)
            deque_min.append(i)

        ans_max.append(A[deque_max[0]])
        ans_min.append(A[deque_min[0]])

        i = 1 
        j = B

        while j < n:
            if deque_max[0] == i - 1:
                deque_max.popleft()

            while deque_max and A[j] > A[deque_max[-1]]:
                deque_max.pop()

            deque_max.append(j)

            ans_max.append(A[deque_max[0]])

            i += 1
            j += 1

        
        i = 1
        j = B

        while j < n:
            if deque_min[0] == i - 1:
                deque_min.popleft()

            while deque_min and A[j] < A[deque_min[-1]]:
                deque_min.pop()

            deque_min.append(j)

            ans_min.append(A[deque_min[0]])

            i += 1
            j += 1             

        total = 0
        for i in range(len(ans_max)):
            total += ans_max[i] + ans_min[i]
        
        return total
    
# Time complexity: O(N)
# Space complexity: O(N)
# The above code is an implementation of the sliding window maximum problem.

s= Solution()
A = [2,5,-1,7,-3,-1,-2]
B = 4
print(s.solve(A,B)) #[3, 3, 5, 5, 6, 7]
A = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3
print(s.solve(A,B)) #[3, 3, 5, 5, 6, 7]
