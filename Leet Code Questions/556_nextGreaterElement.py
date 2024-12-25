class Solution:
    def nextGreaterElement(self, n: int) -> int:
        stack = []       
        nums = [int(i) for i in str(n)]
        n = len(nums)
        result = nums[:]

        for i in range(n-1,-1,-1):              
            isBreak = False
            while stack and nums[stack[-1]] > nums[i]:                  
                next_greater = -1
                for k in range(n-1,i,-1):
                    if nums[k] > nums[i]:
                        next_greater = k
                        break
                
                temp = nums[i]
                nums[i] = nums[next_greater]
                nums[next_greater] = temp


                sorted_nums = sorted(nums[i+1:])                
                result[i] = nums[i]
                result[i+1:] = sorted_nums
                isBreak = True
                break
            
            if isBreak:
                break
            stack.append(i)
        
            if i == 0:
                return -1
        result = int(''.join([str(i) for i in result]))
        
        return result if result < 2**31 else -1
    
    
    
s = Solution()
print(s.nextGreaterElement(12443322))
# 13222344
# 13223344
print(s.nextGreaterElement(1234))
print(s.nextGreaterElement(4321))
print(s.nextGreaterElement(21))
print(s.nextGreaterElement(12))
print(s.nextGreaterElement(214743864))#214744368
                                      #214744368
print(s.nextGreaterElement(214748364))#214748436
                                    #  214748436