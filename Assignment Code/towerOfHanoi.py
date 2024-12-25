#https://www.scaler.com/academy/mentee-dashboard/class/325304/assignment/problems/15010?navref=cl_tt_lst_nm

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def towerOfHanoi(self, A):
        result = []
        def toh(n, fromm, to, aux):
            if n == 1:
                #print("move disk",n,"from rod", fromm, "to rod",to)
                actions = [n,fromm,to]
                result.append(actions)
                return result
            toh(n-1, fromm, aux, to)
            #print("move disk",n,"from rod", fromm, "to rod",to)
            actions = [n,fromm,to]
            result.append(actions)
           
            toh(n-1, aux, to, fromm)
            return result

        return toh(A, 1, 3, 2)

s=Solution()
print(s.towerOfHanoi(1))
print(s.towerOfHanoi(2)) # [[1, 1, 2], [2, 1, 3], [1, 2, 3]]
print(s.towerOfHanoi(3)) # [[1, 1, 3], [2, 1, 2], [1, 3, 2], [3, 1, 3], [1, 2, 1], [2, 2, 3], [1, 1, 3]]
print(s.towerOfHanoi(4)) # [[1, 1, 2], [2, 1, 3], [1, 2, 3], [3, 1, 2], [1, 3, 1], [2, 3, 2], [1, 1, 2], [4, 1, 3], [1, 2, 3], [2, 2, 1], [1, 3, 1], [3, 2, 3], [1, 1, 2], [2, 1, 3], [1, 2, 3]]