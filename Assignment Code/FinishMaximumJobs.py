class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        jobs = []
        n = len(A)
        for i in range(n):
            jobs.append([A[i], B[i]])
            
        jobs.sort(key = lambda x:x[1])

        count = 0
        last_job = 0
        for i in range(n):
            curr_job = jobs[i]
            if curr_job[0] >= last_job:
                count += 1
                last_job = curr_job[1]

        return count

    
s=Solution()
print(s.solve([1,5,7,1],[7,8,8,8]))
print(s.solve([3,2,6],[9,8,9]))