#https://www.scaler.com/academy/mentee-dashboard/class/325342/homework/problems/4808?navref=cl_tt_nv

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):

        hash_A = {}
        set_B = set()

        for i in range(len(B)):
            set_B.add(B[i])

        for i in range(len(A)):
            if A[i] in hash_A:
                hash_A[A[i]] += 1
            else:
                hash_A[A[i]] = 1

        ans = []

        sorted_keys = sorted(hash_A)

        for num in B:
            if num in hash_A:
                count = hash_A[num]
                while count:
                    ans.append(num)
                    count -= 1 

        for key in sorted_keys:

            if key not in set_B:

                count = hash_A[key]
                while count:
                    ans.append(key)
                    count -= 1 

        return ans

s=Solution()
print(s.solve([1, 2, 8, 3, 4, 5, 4], [5, 4, 2]))
print(s.solve([5, 17, 100, 11], [1,100]))