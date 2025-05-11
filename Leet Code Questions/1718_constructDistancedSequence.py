from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:  

        def backtrack(i, n, res, used_nums):

            if i >= len(res):
                return True
            
            if res[i] != 0:
                return backtrack(i+1, n, res, used_nums)
            
            for num in range(n, 0, -1):
                if num in used_nums:
                    continue
                
                used_nums.add(num)
                res[i] = num

                if num == 1:
                    if backtrack(i+1, n, res, used_nums):
                        return True
                else:
                    j = res[i] + i

                    if j < len(res) and res[j] == 0:
                        res[j] = num
                        if backtrack(i+1, n , res, used_nums):
                            return True
                        
                        res[j] = 0

                used_nums.remove(num)
                res[i] = 0

            
            return False
                  
        res = [0]*(2*n-1)
        used_nums = set()
        i = 0

        backtrack(0, n, res, used_nums)

        return res
        # while res.count(0) != 0:
        #     for num in range(n, 0, -1):
        #         if num not in used_nums:                    
        #             if num == 1 and res.count(0) == 1:
        #                 first_idx = res.index(0) #i
        #                 res[first_idx] = num
        #                 used_nums.add(num)
        #                 i += 1
        #             else:
        #                 first_idx = res.index(0) #i
        #                 second_idx = first_idx + num
                        
        #                 if second_idx < (2*n-1):
        #                     if res[first_idx] == 0 and res[second_idx] == 0:
        #                         if num == 1:
        #                             res[first_idx] = num
        #                         else:
        #                             res[first_idx] = num
        #                             res[second_idx] = num
        #                         used_nums.add(num)
        #                         i += 1
        #                     else:            
        #                         continue
        #                 else:
        #                     continue

        # return res

s=Solution()
print(s.constructDistancedSequence(1))
print(s.constructDistancedSequence(2))
print(s.constructDistancedSequence(3))
print(s.constructDistancedSequence(4))
print(s.constructDistancedSequence(5))
print(s.constructDistancedSequence(6))
print(s.constructDistancedSequence(7))
print(s.constructDistancedSequence(8))
print(s.constructDistancedSequence(9))
print(s.constructDistancedSequence(10))
print(s.constructDistancedSequence(11))
print(s.constructDistancedSequence(12))
print(s.constructDistancedSequence(13))
print(s.constructDistancedSequence(14))
print(s.constructDistancedSequence(15))
print(s.constructDistancedSequence(16))
print(s.constructDistancedSequence(17))
print(s.constructDistancedSequence(18))
print(s.constructDistancedSequence(19))
print(s.constructDistancedSequence(20))

        