class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):        

        n = len(A)
        i = 0
        j = n-1
        count = 0

        while i < j:
            sum = A[i] + A[j]
            if sum == B:
                if A[i] == A[j]:
                    count += ((j-i+1)*(j-i+1-1))//2
                    break
                else:
                    ele1 = A[i]
                    ele2 = A[j]
                    cnt1 = 0
                    cnt2 = 0

                    while ele1 == A[i]:
                        cnt1 += 1
                        i += 1
                        
                    while ele2 == A[j]:
                        cnt2 += 1
                        j -= 1

                    count += cnt1*cnt2

            elif sum < B:
                i += 1
            else:
                j -= 1

        return count
s=Solution()                
# print(s.solve([1,2,3,4,5],5))
# print(s.solve([1,2,3,4,5],9))
# print(s.solve([5,10,20,100,105],205))
# print(s.solve([1,1,1],2))
# print(s.solve([1,1,1,1],2))
# print(s.solve([1,3,4,4,5,6,7,7,7,8,9],11))
print(s.solve([1,3,4,4,5,6,7,7,7,8,9],14))